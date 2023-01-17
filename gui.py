from PySide2.QtWidgets import (
    QApplication, QVBoxLayout, QWidget, QMainWindow,
    QListWidgetItem, QLabel, QMessageBox, QFileDialog
)
from PySide2.QtCore import Qt, QTimer
from PySide2.QtCharts import QtCharts
from PySide2.QtGui import QColor
import sys
from datetime import datetime
from ui_flashcards import Ui_MainWindow
from stylesheets import StyleSheet
from time import time
from utils import (
    export_cards_to_json,
    import_cards,
    get_categorized_cards_collections,
    remove_card, export_cards_to_csv
)
from stats import Stats
from exam import Exam
from config import Config
from card_dialog_gui import CreateCardDialog
import os


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

    def _setupCategories(self):
        """Fills List Widget with card categories"""
        cards = import_cards(Config.CARDS_PATH)
        card_collections = get_categorized_cards_collections(cards)
        for card_collection in card_collections:
            collection_item = QListWidgetItem(card_collection.category)
            collection_item.card_collection = card_collection
            self.ui.categoriesField.addItem(collection_item)
            if card_collection.category == 'Wszystkie':
                self.state['allCardsCollection'] = card_collection
                self._selectCategory(collection_item)
        self.ui.categoriesField.item(0).setSelected(True)

    def _connectCategoriesBtns(self):
        """Connects buttons on Train page to callbacks"""
        self.ui.categoriesField.itemClicked.connect(self._selectCategory)
        self.ui.answerInput.textChanged.connect(self._handleInputChange)
        self.ui.flashcardButton.clicked.connect(self._handleAnswer)
        self.ui.btnDelCard.clicked.connect(self._handleDeleteCard)
        self.ui.btnExport.clicked.connect(self._handleExportCategory)

    def _handleExportCategory(self):
        """Handles user click of export button"""
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(
            None,
            "Eksportuj fiszki",
            "",
            "Text Files (*.txt);;JSON Files (*.json)",
            options=options
        )
        base, ext = os.path.splitext(file_path)
        if ext == '.json':
            export_cards_to_json(
                file_path, self.ui.btnExport.CardCollection.cards
            )
        if ext == '.txt':
            export_cards_to_csv(
                file_path, self.ui.btnExport.CardCollection.cards
            )

    def _handleDeleteCard(self):
        """Handles user click of delete card button"""
        card = self.state['current_card']
        remove_card(card)
        self.ui.categoriesField.clear()
        self._setupCategories()
        self._selectCategory(self.ui.categoriesField.item(0))

    def _setupUseTimer(self):
        """Initiates timer to count app use time"""
        self.state['sessionStartTime'] = time()
        app = QApplication.instance()
        app.lastWindowClosed.connect(self._saveUseTime())

    def _saveUseTime(self):
        """Saves app use time"""
        session_time = time() - self.state['sessionStartTime']
        self.stats.save_use_time(session_time)
        self.state['sessionStartTime'] = time()

    def _shouldShowPopup(self) -> bool:
        """Checks if reminder to take an exam should be shown"""
        show_after = Config.POPUP_ANSWERS_COUNT
        if self.stats.answers_since_last_exam() == show_after:
            return True
        return False

    def _showReminderPopup(self):
        """Shows reminder to take an exam"""
        msg = QMessageBox()
        msg.setWindowTitle(Config.POPUP_TITLE)
        msg.setText(Config.POPUP_MSG)
        msg.exec_()

    def _selectCategory(self, category):
        """Handles user click on certain category in list widget"""
        card_collection = category.card_collection
        self.state['current_collection'] = card_collection
        self._draw_new_card(card_collection)
        self.ui.choosenCategoryHeader.setText(
            f'Wybrana kategoria: {card_collection.category}'
        )
        self.ui.btnExport.CardCollection = card_collection

    def _handleStartTestClick(self):
        """Handles user click on start exam button"""
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
        exam = Exam(cards)
        self.state['currExam'] = exam
        self._setupTestTimer()
        self._draw_exam_card()

    def _setupTestTimer(self):
        """Initiates timer to show remaining exam time left"""
        self.state['time_left'] = self.state['test_time_limit']
        timer = QTimer()
        timer.setInterval(1000)
        self.state['activated_timer'] = timer

        def timer_callback():
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
        """Callback to when timer counted to 0,
        Ends current exam"""
        self.ui.testTimerLabel.setText('Koniec')
        cards = [*self.state['currExam'].unanswered_cards]
        for card in cards:
            self.state['currExam'].answer_card(card, '')
        self._handleEndExam()

    def _draw_exam_card(self):
        """Draws new exam card from current exam"""
        self.ui.testCardInput.setText('')
        card = self.state['currExam'].draw_card()
        self.ui.testCardLabel.setText(card.learning_lang_value)
        self.state['currExamCard'] = card

    def _handleEndExam(self):
        """Callback to run when user has ended an exam.
        Saves an exam result and displays It"""
        self.state['activated_timer'].stop()
        self.stats.save_exam(self.state['currExam'])
        result = self.state['currExam'].generate_result()
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
        """Handles drawing exam result in widget placed at layout"""
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
        """Disables and enables next question button in exams page
        based on user input"""
        if self.ui.testCardInput.text() == '':
            self.ui.testCardBtn.setDisabled(True)
        else:
            self.ui.testCardBtn.setDisabled(False)

    def _handleNextExamQuestion(self):
        """Handles user click of next question button on exam page"""
        user_input = self.ui.testCardInput.text()
        card = self.state['currExamCard']
        self.state['currExam'].answer_card(card, user_input)
        if self.state['currExam'].is_completed:
            self._handleEndExam()
        else:
            self._draw_exam_card()

    def _setupExamsPage(self):
        """Connects callback to buttons on exam page"""
        self.ui.testEasyBtn.clicked.connect(self._handleTestDiffBtn1Click)
        self.ui.testMediumBtn.clicked.connect(self._handleTestDiffBtn2Click)
        self.ui.testHardBtn.clicked.connect(self._handleTestDiffBtn3Click)
        self.ui.testStartBtn.clicked.connect(self._handleStartTestClick)

    def _handleTestDiffBtn1Click(self):
        """Handles easy difficulty button click"""
        self.state['testDiffBtn'] = 'easy'
        self.__setSelectedBtnUi()

    def _handleTestDiffBtn2Click(self):
        """Handles medium difficulty button click"""
        self.state['testDiffBtn'] = 'medium'
        self.__setSelectedBtnUi()

    def _handleTestDiffBtn3Click(self):
        """Handles hard difficulty button click"""
        self.state['testDiffBtn'] = 'hard'
        self.__setSelectedBtnUi()

    def __setSelectedBtnUi(self):
        """Changes difficulty buttons styles based
        on which one is selected"""
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
        """Changes exam setup variables based on which
        difficulty is choosen"""
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
        """Draws new card on training page"""
        card = card_collection.draw_cards(1)[0]
        self.ui.cardName.setText(card.learning_lang_value)
        self.ui.flashcardButton.setText('Sprawdź')
        self.ui.answerFeedbackLabel.setText('')
        self.ui.answerInput.setText('')
        self.state['current_card'] = card

    def _handleAnswer(self):
        """Handles user click of check answer button
        on training page"""
        card = self.state['current_card']
        input_str = self.ui.answerInput.text().strip()
        answer = card.answer(input_str)
        self.__format_answer_label(answer.is_correct)
        self.stats.save_answer(answer)

        if self._shouldShowPopup():
            self._showReminderPopup()

        self.ui.flashcardButton.setText('Następna')
        self.ui.flashcardButton.clicked.disconnect(self._handleAnswer)
        self.ui.flashcardButton.clicked.connect(self._handleNextCardClick)

    def _handleInputChange(self):
        """Disables and enables check answer button on training page
        based on user input"""
        if self.ui.answerInput.text() == '':
            self.ui.flashcardButton.setDisabled(True)
        else:
            self.ui.flashcardButton.setDisabled(False)

    def __format_answer_label(self, is_answer_correct):
        """Draws prompt based on correctness of user answer
        on training page"""
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
        """Handles user click of next question button
        on training page"""
        curr_card_collection = self.state['current_collection']
        self.ui.flashcardButton.clicked.disconnect(self._handleNextCardClick)
        self.ui.flashcardButton.clicked.connect(self._handleAnswer)
        self._draw_new_card(curr_card_collection)

    def _setupMainNav(self):
        """Connects callbacks to main navigation buttons.
        Each callback takes user to another app page"""
        self.ui.trainButton.clicked.connect(
            lambda: self.ui.pagesStack.setCurrentIndex(0))
        self.ui.examButton.clicked.connect(
            lambda: self.ui.pagesStack.setCurrentIndex(1))
        self.ui.statsButton.clicked.connect(
            lambda: self.ui.pagesStack.setCurrentIndex(2))

    def _setupStatsPage(self):
        """Connects buttons on stats page to
        callbacks and calls setup for sub stats-pages"""
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
        """Draws misc statistics data on "others" sub-page on stats page"""
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
        days_str = '' if days == 0 else f"{days} d "
        hours_str = '' if hours == 0 else f"{hours} h "
        minutes_str = '' if minutes == 0 else f"{minutes} m "
        self.ui.labelAppUseTime.setText(days_str + hours_str + minutes_str)

    def _refreshStats(self):
        """Re-initaites sub pages on stats page (displays up to date data)"""
        self._saveUseTime()
        self.stats.reload_stats()
        self._setupStatsMiscPage()
        self._setupStatsAnswersPage()
        self.ui.prevExamsList.clear()
        self._setupStatsExamsPage()

    def _setupStatsExamsPage(self):
        """Fills exams list widget on stats sub page with previously
        taken exams"""
        prev_exams = self.stats.get_exams()
        for exam in prev_exams:
            points = f"{exam['correct']}/{exam['total']}"
            percentage = f"{exam['percentage']}%"
            exam_head_str = f"{points} pkt. ({percentage}), {exam['date']}"
            list_item = QListWidgetItem(exam_head_str)
            self.ui.prevExamsList.addItem(list_item)
            list_item.exam = exam
        self.ui.prevExamsList.itemClicked.connect(self._selectExam)

    def _selectExam(self, exam):
        """Handles user click on certain exam in exams list widget
        on stats sub page"""
        self._display_exam_result_in_layout(
            exam.exam, self.ui.vbox_exam_history, self.ui.examsHistoryHolder
        )

    def _handleSliderChange(self):
        """Handles user change of slider position on stats
        "answers" sub page"""
        value = self.ui.daysSlider.value()
        self.state['daysRange'] = value
        self.ui.daysShownLabel.setText(
            f"Wyświetlane ostatnie: {value} dni"
        )
        self._refreshStats()

    def _setupStatsAnswersPage(self):
        """Draws plot with user answers history on "answers" stats sub page"""
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
        """Adds layout to drawn plot on stats "answers" sub page"""
        self.ui.plotCanvasLayoutCorrect = QVBoxLayout(self.ui.correctPlot)
        self.ui.plotCorrect = None


def guiMain(args):
    app = QApplication(args)
    window = FlashcardsWindow()
    window.show()
    return app.exec_()


if __name__ == '__main__':
    guiMain(sys.argv)
