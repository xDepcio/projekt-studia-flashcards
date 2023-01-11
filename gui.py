from PySide2.QtWidgets import (
    QApplication, QHBoxLayout, QVBoxLayout, QWidget, QSlider, QSpinBox,
    QMainWindow, QListWidgetItem, QGraphicsScene, QGraphicsSimpleTextItem,
    QSizePolicy, QLabel, QMessageBox
)
from PySide2.QtCore import Qt, SignalInstance, Signal, QMetaMethod, QTimer
from PySide2.QtCharts import QtCharts
from PySide2.QtGui import QPixmap, QPainter, QBrush, QColor
import sys
from matplotlib import pyplot as plt
from io import BytesIO
from datetime import datetime
from ui_flashcards import Ui_MainWindow
from stylesheets import StyleSheet
from time import time
from utils import (
    export_cards,
    import_cards,
    get_categorized_cards_collections,
    add_card,
    remove_card
)
from stats import Stats
from exam import Exam
from config import Config
from card_dialog_gui import CreateCardDialog
from card import Card


class FlashcardsWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.stats = Stats(Config.STATS_PATH)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.vbox_exam_answers = QVBoxLayout(self.ui.scrollItemsHolder)
        self.ui.vbox_exam_history = QVBoxLayout(self.ui.examsHistoryHolder)
        self.state = {}
        self._setupCategories()
        self._connectCategoriesBtns()
        self._setupMainNav()
        self._setupStatsPage()
        self._setupExamsPage()
        self._setupUseTimer()
        self._setupCardAddDialog()

    def _setupCardAddDialog(self):
        self.card_dialog = CreateCardDialog(self)
        self.ui.btnAddCard.clicked.connect(lambda: self.card_dialog.show())
        self.card_dialog.ui.btnBox.accepted.connect(self._handleAddCard)

    def _handleAddCard(self):
        origin_name = self.card_dialog.ui.originNameInput.text()
        learn_name = self.card_dialog.ui.learnNameInput.text()
        category = self.card_dialog.ui.categoryInput.text().capitalize()
        pop = self.card_dialog.ui.horizontalSlider.value()/100
        add_card(origin_name, learn_name, category, pop)
        print('ADDING CARD')
        self.ui.categoriesField.clear()
        self._setupCategories()

    def _setupCategories(self):
        cards = import_cards(Config.CARDS_PATH)
        card_collections = get_categorized_cards_collections(cards)
        for card_collection in card_collections:
            collection_item = QListWidgetItem(card_collection.category)
            collection_item.card_collection = card_collection
            self.ui.categoriesField.addItem(collection_item)
            if card_collection.category == 'Wszystkie':
                self.state['allCardsCollection'] = card_collection
        self.ui.categoriesField.item(0).setSelected(True)

    def _connectCategoriesBtns(self):
        self.ui.categoriesField.itemClicked.connect(self._selectCategory)
        self.ui.answerInput.textChanged.connect(self._handleInputChange)
        self.ui.flashcardButton.clicked.connect(self._handleAnswer)
        self.ui.btnDelCard.clicked.connect(self._handleDeleteCard)

    def _handleDeleteCard(self):
        card = self.state['current_card']
        remove_card(card)
        self.ui.categoriesField.clear()
        self._setupCategories()
        self._draw_new_card(self.state['current_collection'])

    def _setupUseTimer(self):
        self.state['sessionStartTime'] = time()
        app = QApplication.instance()
        app.lastWindowClosed.connect(self._saveUseTime())

    def _saveUseTime(self):
        session_time = time() - self.state['sessionStartTime']
        self.stats.save_use_time(session_time)
        self.state['sessionStartTime'] = time()

    def _shouldShowPopup(self):
        show_after = Config.POPUP_ANSWERS_COUNT
        if self.stats.answers_since_last_exam() == show_after:
            return True
        return False

    def _showReminderPopup(self):
        msg = QMessageBox()
        msg.setWindowTitle(Config.POPUP_TITLE)
        msg.setText(Config.POPUP_MSG)
        msg.exec_()

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
            self.state['test_question_num'], True
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
            self.ui.testTimerLabel.setText(
                "{:d}:{:02d}".format(minutes, seconds)
            )
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

    def _handleEndExam(self):
        self.stats.save_exam(self.state['currExam'])
        result = self.state['currExam'].generate_result()
        print(result)
        self.ui.testStack.setCurrentIndex(1)
        prc = result['percentage']
        self.ui.examScoreHeader.setText(
            f"Wynik: {result['correct']}/{result['total']} pkt. ({prc}%)"
        )
        self._display_exam_result_in_layout(
            result, self.ui.vbox_exam_answers, self.ui.scrollItemsHolder
        )
        self.ui.testCardInput.textChanged.disconnect(
            self._handleTestInputChange
        )
        self.ui.testCardBtn.clicked.disconnect(self._handleNextExamQuestion)
        self.ui.testEasyBtn.setDisabled(False)
        self.ui.testMediumBtn.setDisabled(False)
        self.ui.testHardBtn.setDisabled(False)
        self.ui.testStartBtn.setDisabled(False)

    def _display_exam_result_in_layout(self, result, layout, widget_holder):
        if self.state.get('attachedExamAnswerWidget'):
            for child in widget_holder.children():
                if type(child) == QWidget:
                    child.setParent(None)

        for answer in result['answers']:

            answer_widget = QWidget(widget_holder)
            layout.addWidget(answer_widget)
            answer_vbox_layout = QVBoxLayout(answer_widget)
            self.state['attachedExamAnswerWidget'] = answer_widget

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
        self.state['current_card'] = card

    def _handleAnswer(self):
        card = self.state['current_card']
        input_str = self.ui.answerInput.text().strip()
        answer = card.answer(input_str)
        self.__format_answer_label(answer.is_correct)
        print('------executed------')
        self.stats.save_answer(answer)

        if self._shouldShowPopup():
            self._showReminderPopup()

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
        self.ui.daysSlider.valueChanged.connect(self._handleSliderChange)
        self.state['daysRange'] = Config.DEFAULT_DAYS_RANGE
        self._setupPlotCanvas()
        self.ui.refreshStatsBtn.clicked.connect(self._refreshStats)
        self._setupStatsAnswersPage()
        self._setupStatsExamsPage()
        self._setupStatsMiscPage()

    def _setupStatsMiscPage(self):
        self.ui.labelAllAnswers.setText(f"{self.stats.answers_count()}")
        self.ui.labelCorrectAnswers.setText(
            f"{self.stats.correct_answers_count()}"
        )
        self.ui.labelWrongAnswers.setText(
            f"{self.stats.wrong_answers_count()}"
        )
        self.ui.labelAccuracy.setText(f"{self.stats.answers_accuracy()}%")
        self.ui.labelExamsCount.setText(str(self.stats.exams_count()))
        self.ui.labelExamsAccuracy.setText(
            str(self.stats.exams_avg_accuracy()) + '%'
        )

        days, hours, minutes = self.stats.app_use_time()
        days_str = '' if days == 0 else f"{days} d"
        hours_str = '' if hours == 0 else f"{hours} h"
        minutes_str = '' if minutes == 0 else f"{minutes} m"
        self.ui.labelAppUseTime.setText(days_str + hours_str + minutes_str)

    def _refreshStats(self):
        self._saveUseTime()
        self.stats.reload_stats()
        self._setupStatsMiscPage()
        self._setupStatsAnswersPage()
        self.ui.prevExamsList.clear()
        self._setupStatsExamsPage()

    def _setupStatsExamsPage(self):
        prev_exams = self.stats.get_exams()
        print(prev_exams)
        for exam in prev_exams:
            points = f"{exam['correct']}/{exam['total']}"
            percentage = f"{exam['percentage']}%"
            exam_head_str = f"{points} pkt. ({percentage}), {exam['date']}"
            list_item = QListWidgetItem(exam_head_str)
            self.ui.prevExamsList.addItem(list_item)
            list_item.exam = exam
        self.ui.prevExamsList.itemClicked.connect(self._selectExam)

    def _selectExam(self, exam):
        self._display_exam_result_in_layout(
            exam.exam, self.ui.vbox_exam_history, self.ui.examsHistoryHolder
        )

    def _handleSliderChange(self):
        value = self.ui.daysSlider.value()
        self.state['daysRange'] = value
        self.ui.daysShownLabel.setText(
            f"Wyświetlane ostatnie: {value} dni"
        )
        self._refreshStats()

    def _setupStatsAnswersPage(self):
        if self.ui.plotCorrect:
            self.ui.plotCorrect.deleteLater()
            del self.ui.plotCorrect

        set0 = QtCharts.QBarSet('Poprawne')
        set1 = QtCharts.QBarSet('Niepoprawne')
        set0.setBrush(QColor(157, 216, 102))
        set0.setPen(Qt.NoPen)
        set1.setBrush(QColor(202, 71, 47))
        set1.setPen(Qt.NoPen)

        correct, wrong, dates = self.stats.get_answers_date_range_count(
            self.state['daysRange'], datetime.fromtimestamp(time())
        )

        set0.append(correct)
        set1.append(wrong)

        series = QtCharts.QStackedBarSeries()
        series.append(set0)
        series.append(set1)

        chart = QtCharts.QChart()
        chart.addSeries(series)
        chart.setTitle('Odpowiedzi')
        chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

        axisX = QtCharts.QBarCategoryAxis()
        axisX.append(dates)
        axisX.setLabelsAngle(90)
        chart.addAxis(axisX, Qt.AlignBottom)
        series.attachAxis(axisX)

        axisY = QtCharts.QValueAxis()
        chart.addAxis(axisY, Qt.AlignLeft)
        series.attachAxis(axisY)

        chartView = QtCharts.QChartView(chart)
        self.ui.plotCorrect = chartView
        self.ui.plotCanvasLayoutCorrect.addWidget(self.ui.plotCorrect)

    def _setupPlotCanvas(self):
        self.ui.plotCanvasLayoutCorrect = QVBoxLayout(self.ui.correctPlot)
        self.ui.plotCorrect = None

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
    window = FlashcardsWindow()
    window.show()
    return app.exec_()


if __name__ == '__main__':
    guiMain(sys.argv)
