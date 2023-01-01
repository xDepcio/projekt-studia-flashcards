from PySide2.QtWidgets import (
    QApplication, QHBoxLayout, QVBoxLayout, QWidget, QSlider, QSpinBox,
    QMainWindow, QListWidgetItem, QGraphicsScene, QGraphicsSimpleTextItem,
    QSizePolicy, QLabel
)
from PySide2.QtCore import Qt, SignalInstance, Signal, QMetaMethod, QTimer
from PySide2.QtCharts import QtCharts
from PySide2.QtGui import QPixmap, QPainter, QBrush, QColor
import sys
from matplotlib import pyplot as plt
from io import BytesIO
from datetime import datetime
from ui_flashcards import Ui_MainWindow
from utils import export_cards, import_cards, get_categorized_cards_collections
from stylesheets import StyleSheet
from stats import Stats
from time import time
from exam import Exam


class AirQualityWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.stats = Stats('stats.json')
        self.stats.load_stats()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.vbox_exam_answers = QVBoxLayout(self.ui.scrollItemsHolder)
        self.ui.vbox_exam_history = QVBoxLayout(self.ui.examsHistoryHolder)
        self.state = {}
        self._setupCategories()
        self._setupMainNav()
        self._setupStatsPage()
        self._setupExamsPage()

    def _setupCategories(self):
        cards = import_cards('cards.json')
        card_collections = get_categorized_cards_collections(cards)
        for card_collection in card_collections:
            collection_item = QListWidgetItem(card_collection.category)
            collection_item.card_collection = card_collection
            self.ui.categoriesField.addItem(collection_item)
            if card_collection.category == 'Wszystkie':
                self.state['allCardsCollection'] = card_collection

        self.ui.categoriesField.itemClicked.connect(self._selectCategory)
        self.ui.categoriesField.item(0).setSelected(True)
        self._selectCategory(self.ui.categoriesField.item(0))
        self.ui.answerInput.textChanged.connect(self._handleInputChange)
        self.ui.flashcardButton.clicked.connect(self._handleAnswer)

    def _selectCategory(self, category):
        card_collection = category.card_collection
        self.state['current_collection'] = card_collection
        self._draw_new_card(card_collection)
        self.ui.choosenCategoryHeader.setText(
            f'Wybrana kategoria: {card_collection.category}'
        )

    def _handleStartTestClick(self):
        self.ui.testEasyBtn.setDisabled(True)
        self.ui.testMediumBtn.setDisabled(True)
        self.ui.testHardBtn.setDisabled(True)
        self.ui.testStartBtn.setDisabled(True)
        self.ui.testStack.setCurrentIndex(0)
        self.ui.testCardInput.textChanged.connect(self._handleTestInputChange)
        self.ui.testCardBtn.clicked.connect(self._handleNextExamQuestion)
        all_cards_collection = self.state['allCardsCollection']
        cards = all_cards_collection.draw_cards(
            self.state['test_question_num'], False
        )
        exam = Exam(cards, 0)
        self.state['currExam'] = exam
        self._setupTestTimer()
        self._draw_exam_card()

    def _setupTestTimer(self):
        self.state['time_left'] = self.state['test_time_limit']
        timer = QTimer()
        timer.setInterval(1000)
        self.state['activated_timer'] = timer

        def timer_callback():
            print('called cb')
            minutes, seconds = divmod(self.state['time_left'], 60)
            self.ui.testTimerLabel.setText("{:d}:{:02d}".format(minutes, seconds))
            if self.state['time_left'] == 0:
                timer.stop()
                self._test_timer_ended()
            self.state['time_left'] -= 1

        timer.timeout.connect(timer_callback)
        timer.start()

    def _test_timer_ended(self):
        self.ui.testTimerLabel.setText('Koniec')
        cards = [*self.state['currExam'].unanswered_cards]
        for card in cards:
            self.state['currExam'].answer_card(card, '')
        self._handleEndExam()

    def _draw_exam_card(self):
        self.ui.testCardInput.setText('')
        card = self.state['currExam'].draw_card()
        if self.state['currExam'].is_completed:
            self.state['activated_timer'].stop()
            self._handleEndExam()
            return
        self.ui.testCardLabel.setText(card.learning_lang_value)
        self.state['currExamCard'] = card
        print(' ')
        print(self.state)
        print('-------------------')
        print(self.state['currExam'])
        print(' ')

    def _handleEndExam(self):
        self.stats.save_exam(self.state['currExam'])
        result = self.state['currExam'].generate_result()
        print(result)
        self.ui.testStack.setCurrentIndex(1)
        self.ui.examScoreHeader.setText(
            f"Wynik: {result['correct']}/{result['total']} pkt. ({result['percentage']}%)"
        )
        self._display_exam_result_in_layout(result, self.ui.vbox_exam_answers, self.ui.scrollItemsHolder)
        self.ui.testCardInput.textChanged.disconnect(self._handleTestInputChange)
        self.ui.testCardBtn.clicked.disconnect(self._handleNextExamQuestion)
        self.ui.testEasyBtn.setDisabled(False)
        self.ui.testMediumBtn.setDisabled(False)
        self.ui.testHardBtn.setDisabled(False)
        self.ui.testStartBtn.setDisabled(False)

    def _display_exam_result_in_layout(self, result, layout, widget_holder):
        if self.state.get('attachedExamAnswerWidget'):
            print('+++++++++++++++++++++')
            for child in widget_holder.children():
                print(type(child))
                print(type(child) == QWidget)
                if type(child) == QWidget:
                    child.setParent(None)
                # self.ui.vbox_exam_answers.removeWidget(child)
            print('+++++++++++++++++++++')
        for answer in result['answers']:

            answer_widget = QWidget(widget_holder)
            layout.addWidget(answer_widget)
            answer_vbox_layout = QVBoxLayout(answer_widget)
            self.state['attachedExamAnswerWidget'] = answer_widget

            # answer_widget.deleteLater()
            # answer_vbox_layout.deleteLater()

            question_label = QLabel(
                f'Pytanie: {answer["toBeGuessed"]}',
                answer_widget
            )
            correct_answer_label = QLabel(
                f'Odpowiedź: {answer["expected"]}',
                answer_widget
            )
            given_answer_label = QLabel(
                f'Twoja odpowiedź: {answer["given"]}',
                answer_widget
            )
            status_label = QLabel(
                f'{"dobrze" if answer["isCorrect"] else "źle"}',
                answer_widget
            )
            answer_vbox_layout.addWidget(question_label)
            answer_vbox_layout.addWidget(correct_answer_label)
            answer_vbox_layout.addWidget(given_answer_label)
            answer_vbox_layout.addWidget(status_label)

    def _handleTestInputChange(self):
        if self.ui.testCardInput.text() == '':
            self.ui.testCardBtn.setDisabled(True)
        else:
            self.ui.testCardBtn.setDisabled(False)

    def _handleNextExamQuestion(self):
        user_input = self.ui.testCardInput.text()
        card = self.state['currExamCard']
        self.state['currExam'].answer_card(card, user_input)
        self._draw_exam_card()

    def _setupExamsPage(self):
        self.ui.testEasyBtn.clicked.connect(self._handleTestDiffBtn1Click)
        self.ui.testMediumBtn.clicked.connect(self._handleTestDiffBtn2Click)
        self.ui.testHardBtn.clicked.connect(self._handleTestDiffBtn3Click)
        self.ui.testStartBtn.clicked.connect(self._handleStartTestClick)

    def _handleTestDiffBtn1Click(self):
        self.state['testDiffBtn'] = 'easy'
        self.__setSelectedBtnUi()

    def _handleTestDiffBtn2Click(self):
        self.state['testDiffBtn'] = 'medium'
        self.__setSelectedBtnUi()

    def _handleTestDiffBtn3Click(self):
        self.state['testDiffBtn'] = 'hard'
        self.__setSelectedBtnUi()

    def __setSelectedBtnUi(self):
        print(StyleSheet.btnExamSelected)
        self.ui.testStartBtn.setDisabled(False)
        self.ui.testEasyBtn.setStyleSheet(
            StyleSheet.btnExamSelected if self.state['testDiffBtn'] == 'easy'
            else StyleSheet.btnExamNotSelected
        )
        self.ui.testMediumBtn.setStyleSheet(
            StyleSheet.btnExamSelected if self.state['testDiffBtn'] == 'medium'
            else StyleSheet.btnExamNotSelected
        )
        self.ui.testHardBtn.setStyleSheet(
            StyleSheet.btnExamSelected if self.state['testDiffBtn'] == 'hard'
            else StyleSheet.btnExamNotSelected
        )
        self._handleSetExamDiff(self.state['testDiffBtn'])

    def _handleSetExamDiff(self, difficulty):
        info_str = ''
        if difficulty == 'easy':
            info_str = "Czas: 3min     Ilość pytań: 5"
            self.state['test_time_limit'] = 60 * 3
            self.state['test_question_num'] = 5
        elif difficulty == 'medium':
            info_str = "Czas: 2min     Ilość pytań: 10"
            self.state['test_time_limit'] = 60 * 2
            self.state['test_question_num'] = 10
        elif difficulty == 'hard':
            info_str = "Czas: 1min     Ilość pytań: 15"
            self.state['test_time_limit'] = 60 * 1
            self.state['test_question_num'] = 15

        self.ui.testTimerLabel.setText(info_str)

    def _draw_new_card(self, card_collection):
        print(card_collection.cards)
        card = card_collection.draw_cards(1)[0]
        self.ui.cardName.setText(card.learning_lang_value)
        self.ui.flashcardButton.setText('Sprawdź')
        self.ui.answerFeedbackLabel.setText('')
        self.ui.answerInput.setText('')
        # self.ui.flashcardButton.clicked.connect(self._handleAnswer)
        self.state['current_card'] = card

    def _handleAnswer(self):
        card = self.state['current_card']
        input_str = self.ui.answerInput.text().strip()
        answer = card.answer(input_str)
        self.__format_answer_label(answer.is_correct)
        print('------executed------')
        self.stats.save_answer(answer)
        self.ui.flashcardButton.setText('Następna')
        self.ui.flashcardButton.clicked.disconnect(self._handleAnswer)
        self.ui.flashcardButton.clicked.connect(self._handleNextCardClick)

    def _handleInputChange(self):
        if self.ui.answerInput.text() == '':
            self.ui.flashcardButton.setDisabled(True)
        else:
            self.ui.flashcardButton.setDisabled(False)

    def __format_answer_label(self, is_answer_correct):
        card = self.state['current_card']
        if is_answer_correct:
            self.ui.answerFeedbackLabel.setText('Dobrze :)')
            self.ui.answerFeedbackLabel.setStyleSheet(
                StyleSheet.correctAnswerLabel
                )
        else:
            self.ui.answerFeedbackLabel.setText(
                f'Źle! poprawna odpowiedź\n{card.origin_lang_value}'
                )
            self.ui.answerFeedbackLabel.setStyleSheet(
                StyleSheet.wrongAnswerLabel
                )
        font = self.ui.answerFeedbackLabel.font()
        font.setPixelSize(18)
        self.ui.answerFeedbackLabel.setFont(font)

    def _handleNextCardClick(self):
        curr_card_collection = self.state['current_collection']
        self.ui.flashcardButton.clicked.disconnect(self._handleNextCardClick)
        self.ui.flashcardButton.clicked.connect(self._handleAnswer)
        self._draw_new_card(curr_card_collection)

    def _setupMainNav(self):
        self.ui.trainButton.clicked.connect(
            lambda: self.ui.pagesStack.setCurrentIndex(0))
        self.ui.examButton.clicked.connect(
            lambda: self.ui.pagesStack.setCurrentIndex(1))
        self.ui.statsButton.clicked.connect(
            lambda: self.ui.pagesStack.setCurrentIndex(2))

    def _setupStatsPage(self):
        self.ui.statsAnswersBtn.clicked.connect(
            lambda: self.ui.statsStack.setCurrentIndex(0))
        self.ui.statsTestsBtn.clicked.connect(
            lambda: self.ui.statsStack.setCurrentIndex(1))
        self.ui.statsOtherBtn.clicked.connect(
            lambda: self.ui.statsStack.setCurrentIndex(2))
        self._setupPlotCanvas()
        self.ui.refreshStatsBtn.clicked.connect(self._refreshStats)
        self._setupStatsAnswersPage()
        self._setupStatsExamsPage()

    def _refreshStats(self):
        self._setupStatsAnswersPage()
        self.ui.prevExamsList.clear()
        self.stats.load_stats()
        self._setupStatsExamsPage()

    def __deleteWidgetChilds(self, widget, child_type):
        self.ui.prevExamsList.clear()
        # print(type(self.ui.prevExamsList.item(1)))
        # for i in range(self.ui.prevExamsList.count()):
        #     item = self.ui.prevExamsList.item(i)
        #     item.setParent(None)
        #     print(i)

    def _setupStatsExamsPage(self):
        prev_exams = self.stats.get_exams()
        print(prev_exams)
        for exam in prev_exams:
            exam_head_str = f"{exam['correct']}/{exam['total']} pkt. ({exam['percentage']}%), {exam['date']}"
            list_item = QListWidgetItem(exam_head_str)
            self.ui.prevExamsList.addItem(list_item)
            list_item.exam = exam
        self.ui.prevExamsList.itemClicked.connect(self._selectExam)
        # self.ui.categoriesField.item(0).setSelected(True)
        # self._selectExam(self.ui.categoriesField.item(0))
        # self.ui.answerInput.textChanged.connect(self._handleInputChange)

    def _selectExam(self, exam):
        self._display_exam_result_in_layout(exam.exam, self.ui.vbox_exam_history, self.ui.examsHistoryHolder)

    def _setupStatsAnswersPage(self):
        # self._setupPlotCanvas()
        if self.ui.plotCorrect:
            self.ui.plotCorrect.deleteLater()
            del self.ui.plotCorrect
        if self.ui.plotWrong:
            self.ui.plotWrong.deleteLater()
            del self.ui.plotWrong

        self.ui.plotCorrect = QtCharts.QChartView()
        self.ui.plotCorrect.setRenderHint(QPainter.Antialiasing)
        self.ui.plotCanvasLayoutCorrect.addWidget(self.ui.plotCorrect)
        series = QtCharts.QLineSeries()
        series.setName('Poprawne odpowiedzi')
        epoch = datetime.utcfromtimestamp(0)
        date_answ_count_correct = self.stats.get_date_answers_count('correct')
        for date, count in date_answ_count_correct:
            reading_date = datetime.strptime(date, '%Y-%m-%d %H')
            x = (reading_date - epoch).total_seconds()*1000
            series.append(x, count)
        self.ui.plotCorrect.chart().addSeries(series)
        dateAxisCorrect = QtCharts.QDateTimeAxis()
        valueAxisCorrect = QtCharts.QValueAxis()
        self.ui.plotCorrect.chart().addAxis(dateAxisCorrect, Qt.AlignBottom)
        self.ui.plotCorrect.chart().addAxis(valueAxisCorrect, Qt.AlignLeft)
        series.attachAxis(dateAxisCorrect)
        series.attachAxis(valueAxisCorrect)

        self.ui.plotWrong = QtCharts.QChartView()
        self.ui.plotWrong.setRenderHint(QPainter.Antialiasing)
        self.ui.plotCanvasLayoutWrong.addWidget(self.ui.plotWrong)
        series = QtCharts.QLineSeries()
        series.setName('Niepoprawne odpowiedzi')
        epoch = datetime.utcfromtimestamp(0)
        readings_wrong = self.stats.get_date_answers_count('wrong')
        print(readings_wrong)
        for reading in readings_wrong:
            reading_date = datetime.strptime(reading[0], '%Y-%m-%d %H')
            x = (reading_date - epoch).total_seconds()*1000
            series.append(x, reading[1])
        self.ui.plotWrong.chart().addSeries(series)
        dateAxisWrong = QtCharts.QDateTimeAxis()
        valueAxisWrong = QtCharts.QValueAxis()
        self.ui.plotWrong.chart().addAxis(dateAxisWrong, Qt.AlignBottom)
        self.ui.plotWrong.chart().addAxis(valueAxisWrong, Qt.AlignLeft)
        series.attachAxis(dateAxisWrong)
        series.attachAxis(valueAxisWrong)

    def _setupPlotCanvas(self):
        self.ui.plotCanvasLayoutCorrect = QVBoxLayout(self.ui.correctPlot)
        self.ui.plotCorrect = None
        self.ui.plotCanvasLayoutWrong = QVBoxLayout(self.ui.wrongPlot)
        self.ui.plotWrong = None

    # def _setupStationList(self):
    #     stations = get_stations()
    #     self._scene = QGraphicsScene()
    #     self.ui.stationMap.setScene(self._scene)
    #     self.ui.stationMap.setRenderHint(QPainter.Antialiasing)
    #     for station in stations:
    #         item = QListWidgetItem(str(station))
    #         item.station = station
    #         self.ui.stations.addItem(item)
    #         lat, lon = station.pos()
    #         marker = self._scene.addEllipse(-5, -5, 10, 10)
    #         marker.setBrush(QBrush(Qt.red))
    #         marker.setPos(lon*100, -lat*100)
    #         marker.setFlag(marker.ItemIgnoresTransformations)
    #         text_item = QGraphicsSimpleTextItem(str(station), marker)
    #         text_item.setPos(10, -10)
    #         font = text_item.font()
    #         font.setPixelSize(font.pointSize()+2)
    #         text_item.setFont(font)
    #         item.text_item = text_item

        # self.ui.stations.itemDoubleClicked.connect(self._selectStation)
    #     self.ui.stations.itemClicked.connect(self._highlightStation)
    #     self.ui.sensors.itemClicked.connect(self._selectSensor)
    #     self._highlighted_item = None

    # def _selectStation(self, item):
    #     self.ui.stack.setCurrentIndex(1)
    #     stationName = item.station.name()
    #     self.ui.stationName.setText(stationName)
    #     sensors = item.station.sensors()
    #     self.ui.sensors.clear()
    #     for sensor in sensors:
    #         sensor_item = QListWidgetItem(sensor.name())
    #         sensor_item.sensor = sensor
    #         self.ui.sensors.addItem(sensor_item)

    # def _highlightStation(self, item):
    #     if self._highlighted_item:
    #         font = self._highlighted_item.font()
    #         font.setBold(False)
    #         self._highlighted_item.setFont(font)
    #         self._highlighted_item.setBrush(Qt.black)

    #     text_item = item.text_item
    #     font = text_item.font()
    #     font.setBold(True)
    #     text_item.setFont(font)
    #     text_item.setBrush(Qt.red)
    #     self._highlighted_item = text_item

    # def _selectSensor(self, item):
    #     sensor = item.sensor
    #     if self.ui.plot:
    #         self.ui.plot.deleteLater()
    #         del self.ui.plot
    #     self.ui.plot = QtCharts.QChartView()
    #     self.ui.plot.setRenderHint(QPainter.Antialiasing)
    #     self.ui.plotCanvasLayout.addWidget(self.ui.plot)
    #     readings = sensor.readings()
    #     series = QtCharts.QLineSeries()
    #     series.setName(sensor.name())
    #     epoch = datetime.utcfromtimestamp(0)
    #     for reading in readings:
    #         if reading.value is not None:
    #             x = (reading.date - epoch).total_seconds()*1000
    #             series.append(x, reading.value)
    #     self.ui.plot.chart().addSeries(series)
    #     dateAxis = QtCharts.QDateTimeAxis()
    #     valueAxis = QtCharts.QValueAxis()
    #     self.ui.plot.chart().addAxis(dateAxis, Qt.AlignBottom)
    #     self.ui.plot.chart().addAxis(valueAxis, Qt.AlignLeft)
    #     series.attachAxis(dateAxis)
    #     series.attachAxis(valueAxis)

    # def _setupPlotCanvas(self):
    #     self.ui.plotCanvasLayout = QVBoxLayout(self.ui.plotContainer)
    #     self.ui.plot = None


def guiMain(args):
    app = QApplication(args)
    window = AirQualityWindow()
    window.show()
    return app.exec_()


if __name__ == '__main__':
    guiMain(sys.argv)
