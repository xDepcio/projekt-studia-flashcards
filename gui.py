from PySide2.QtWidgets import (
    QApplication, QHBoxLayout, QVBoxLayout, QWidget, QSlider, QSpinBox,
    QMainWindow, QListWidgetItem, QGraphicsScene, QGraphicsSimpleTextItem
)
from PySide2.QtCore import Qt
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


class AirQualityWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.stats = Stats('stats.json')
        self.stats.load_stats()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.state_obj = {}
        self._setupCategories()
        self._setupMainNav()
        self._setupStatsPage()

    def _setupCategories(self):
        cards = import_cards('cards.json')
        card_collections = get_categorized_cards_collections(cards)
        for card_collection in card_collections:
            collection_item = QListWidgetItem(card_collection.category)
            collection_item.card_collection = card_collection
            self.ui.categoriesField.addItem(collection_item)

        self.ui.categoriesField.itemClicked.connect(self._selectCategory)
        self.ui.categoriesField.item(0).setSelected(True)
        self._selectCategory(self.ui.categoriesField.item(0))
        self.ui.answerInput.textChanged.connect(self._handleInputChange)

    def _selectCategory(self, category):
        card_collection = category.card_collection
        self.ui.state_obj['current_collection'] = card_collection
        self._draw_new_card(card_collection)
        self.ui.choosenCategoryHeader.setText(
            f'Wybrana kategoria: {card_collection.category}'
        )

    def _draw_new_card(self, card_collection):
        card = card_collection.draw_cards(1)[0]
        self.ui.cardName.setText(card.learning_lang_value)
        self.ui.flashcardButton.setText('Sprawdź')
        self.ui.answerFeedbackLabel.setText('')
        self.ui.answerInput.setText('')
        self.ui.flashcardButton.clicked.connect(self._handleAnswer)
        self.ui.state_obj['current_card'] = card

    def _handleAnswer(self):
        card = self.ui.state_obj['current_card']
        answer = self.ui.answerInput.text().strip()
        is_answer_correct = card.evaluate_answer(answer)
        self.__format_answer_label(is_answer_correct)
        self._save_answer(is_answer_correct, card)
        self.ui.flashcardButton.setText('Następna')
        self.ui.flashcardButton.clicked.disconnect(self._handleAnswer)
        self.ui.flashcardButton.clicked.connect(self._handleNextCardClick)

    def _handleInputChange(self):
        if self.ui.answerInput.text() == '':
            self.ui.flashcardButton.setDisabled(True)
        else:
            self.ui.flashcardButton.setDisabled(False)

    def __format_answer_label(self, is_answer_correct):
        card = self.ui.state_obj['current_card']
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

    def _save_answer(self, is_answer_correct, card):
        date = datetime.fromtimestamp(time())
        date = f'{date.year}-{date.month}-{date.day} {date.hour}:{date.minute}'

        self.stats.data['answers'][
            'totalCorrect' if is_answer_correct else 'totalWrong'
            ] += 1
        self.stats.data['answers'][
            'correct' if is_answer_correct else 'wrong'
            ].append(
            {
                "originLang": card.origin_lang_value,
                "learningLang": card.learning_lang_value,
                "date": date
            }
        )
        self.stats.save_stats()

    def _handleNextCardClick(self):
        curr_card_collection = self.ui.state_obj['current_collection']
        self.ui.flashcardButton.clicked.disconnect(self._handleNextCardClick)
        self._draw_new_card(curr_card_collection)

    def _setupMainNav(self):
        self.ui.trainButton.clicked.connect(
            lambda: self.ui.pagesStack.setCurrentIndex(0))
        self.ui.examButton.clicked.connect(
            lambda: self.ui.pagesStack.setCurrentIndex(1))
        self.ui.statsButton.clicked.connect(
            lambda: self.ui.pagesStack.setCurrentIndex(2))

    def _setupStatsPage(self):
        self._setupPlotCanvas()
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
        readings_correct = self.stats.accum_answers('correct')
        for reading in readings_correct:
            reading_date = datetime.strptime(reading[0], '%Y-%m-%d %H')
            x = (reading_date - epoch).total_seconds()*1000
            series.append(x, reading[1])
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
        readings_wrong = self.stats.accum_answers('wrong')
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
