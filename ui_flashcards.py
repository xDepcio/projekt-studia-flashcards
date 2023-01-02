# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'flashcards.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(588, 702)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_11 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.trainButton = QPushButton(self.centralwidget)
        self.trainButton.setObjectName(u"trainButton")
        font = QFont()
        font.setBold(True)
        font.setWeight(62)
        self.trainButton.setFont(font)
        self.trainButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.trainButton.setStyleSheet(u"background-color: rgb(62, 162, 255);\n"
"border: none;\n"
"color: \"white\";\n"
"padding-bottom: 10px;\n"
"padding-top: 10px;\n"
"border-radius: 9;\n"
"font-weight: 500;\n"
"font-size: 16px;")

        self.horizontalLayout.addWidget(self.trainButton)

        self.examButton = QPushButton(self.centralwidget)
        self.examButton.setObjectName(u"examButton")
        self.examButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.examButton.setStyleSheet(u"background-color: rgb(62, 162, 255);\n"
"border: none;\n"
"color: \"white\";\n"
"padding-bottom: 10px;\n"
"padding-top: 10px;\n"
"border-radius: 9;\n"
"font-weight: 500;\n"
"font-size: 16px;")

        self.horizontalLayout.addWidget(self.examButton)

        self.statsButton = QPushButton(self.centralwidget)
        self.statsButton.setObjectName(u"statsButton")
        self.statsButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.statsButton.setStyleSheet(u"background-color: rgb(62, 162, 255);\n"
"border: none;\n"
"color: \"white\";\n"
"padding-bottom: 10px;\n"
"padding-top: 10px;\n"
"border-radius: 9;\n"
"font-weight: 500;\n"
"font-size: 16px")

        self.horizontalLayout.addWidget(self.statsButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.pagesStack = QStackedWidget(self.centralwidget)
        self.pagesStack.setObjectName(u"pagesStack")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_4 = QHBoxLayout(self.page)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(False)
        font1.setWeight(50)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(77, 77, 77);\n"
"")

        self.verticalLayout_2.addWidget(self.label)

        self.categoriesField = QListWidget(self.page)
        self.categoriesField.setObjectName(u"categoriesField")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.categoriesField.sizePolicy().hasHeightForWidth())
        self.categoriesField.setSizePolicy(sizePolicy)
        self.categoriesField.setStyleSheet(u"QListWidget\n"
"{\n"
"	border : 2px solid rgb(62, 162, 255);\n"
"	background-color: 'white';\n"
"}\n"
"QListWidget QScrollBar\n"
"{\n"
"	background : lightblue;\n"
"}\n"
"QListView::item:selected\n"
"{\n"
"	background-color: rgb(222, 222, 222);\n"
"}\n"
"QListView::item\n"
"{\n"
"	padding-top: 7px;\n"
"	padding-bottom: 7px;\n"
"   color: rgb(77, 77, 77);\n"
"}\n"
"QListView\n"
"{\n"
"	outline: 0;\n"
"   font-size: 16px;\n"
"   font-weight: 450;\n"
"}")

        self.verticalLayout_2.addWidget(self.categoriesField)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.widget = QWidget(self.page)
        self.widget.setObjectName(u"widget")
        self.widget.setCursor(QCursor(Qt.ArrowCursor))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.choosenCategoryHeader = QLabel(self.widget)
        self.choosenCategoryHeader.setObjectName(u"choosenCategoryHeader")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.choosenCategoryHeader.sizePolicy().hasHeightForWidth())
        self.choosenCategoryHeader.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(10)
        self.choosenCategoryHeader.setFont(font2)

        self.verticalLayout_3.addWidget(self.choosenCategoryHeader)

        self.cardName = QLabel(self.widget)
        self.cardName.setObjectName(u"cardName")
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(False)
        font3.setWeight(50)
        self.cardName.setFont(font3)
        self.cardName.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.cardName)

        self.answerFeedbackLabel = QLabel(self.widget)
        self.answerFeedbackLabel.setObjectName(u"answerFeedbackLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.answerFeedbackLabel.sizePolicy().hasHeightForWidth())
        self.answerFeedbackLabel.setSizePolicy(sizePolicy2)
        self.answerFeedbackLabel.setMinimumSize(QSize(0, 70))
        font4 = QFont()
        font4.setBold(False)
        font4.setWeight(50)
        self.answerFeedbackLabel.setFont(font4)
        self.answerFeedbackLabel.setStyleSheet(u"padding: 10px;\n"
"font-size: 18px;\n"
"font-weight: 400;")
        self.answerFeedbackLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.answerFeedbackLabel)

        self.flashcardsInputsContainer = QWidget(self.widget)
        self.flashcardsInputsContainer.setObjectName(u"flashcardsInputsContainer")
        sizePolicy1.setHeightForWidth(self.flashcardsInputsContainer.sizePolicy().hasHeightForWidth())
        self.flashcardsInputsContainer.setSizePolicy(sizePolicy1)
        self.flashcardsInputsContainer.setBaseSize(QSize(0, 0))
        self.horizontalLayout_3 = QHBoxLayout(self.flashcardsInputsContainer)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.answerInput = QLineEdit(self.flashcardsInputsContainer)
        self.answerInput.setObjectName(u"answerInput")

        self.horizontalLayout_3.addWidget(self.answerInput)

        self.flashcardButton = QPushButton(self.flashcardsInputsContainer)
        self.flashcardButton.setObjectName(u"flashcardButton")
        self.flashcardButton.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.flashcardButton)


        self.verticalLayout_3.addWidget(self.flashcardsInputsContainer)


        self.horizontalLayout_4.addWidget(self.widget)

        self.pagesStack.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_6 = QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_2 = QWidget(self.page_2)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.horizontalLayout_6 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.testEasyBtn = QPushButton(self.widget_2)
        self.testEasyBtn.setObjectName(u"testEasyBtn")
        self.testEasyBtn.setStyleSheet(u"color: rgb(62, 162, 255);\n"
"border-radius: 5px;\n"
"background-color: 'white';\n"
"border: 2px solid rgb(62, 162, 255);\n"
"padding: 7px;\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"font-weight: 500;")

        self.horizontalLayout_6.addWidget(self.testEasyBtn)

        self.testMediumBtn = QPushButton(self.widget_2)
        self.testMediumBtn.setObjectName(u"testMediumBtn")
        self.testMediumBtn.setStyleSheet(u"color: rgb(62, 162, 255);\n"
"border-radius: 5px;\n"
"background-color: 'white';\n"
"border: 2px solid rgb(62, 162, 255);\n"
"padding: 7px;\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"font-weight: 500;")

        self.horizontalLayout_6.addWidget(self.testMediumBtn)

        self.testHardBtn = QPushButton(self.widget_2)
        self.testHardBtn.setObjectName(u"testHardBtn")
        self.testHardBtn.setStyleSheet(u"color: rgb(62, 162, 255);\n"
"border-radius: 5px;\n"
"background-color: 'white';\n"
"border: 2px solid rgb(62, 162, 255);\n"
"padding: 7px;\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"font-weight: 500;")

        self.horizontalLayout_6.addWidget(self.testHardBtn)

        self.horizontalSpacer = QSpacerItem(118, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.testStartBtn = QPushButton(self.widget_2)
        self.testStartBtn.setObjectName(u"testStartBtn")
        self.testStartBtn.setEnabled(False)
        self.testStartBtn.setStyleSheet(u"QPushButton:enabled {\n"
"color: rgb(62, 162, 255);\n"
"border-radius: 5px;\n"
"background-color: 'white';\n"
"border: 2px solid rgb(62, 162, 255);\n"
"padding: 7px;\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"font-weight: 500;\n"
"}\n"
"QPushButton:disabled {\n"
"color: rgb(62, 162, 255);\n"
"border-radius: 5px;\n"
"background-color: 'white';\n"
"border: 2px solid rgb(62, 162, 255);\n"
"padding: 7px;\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"font-weight: 500;\n"
"border: 2px solid rgb(118, 152, 184);\n"
"color: rgb(118, 152, 184);\n"
"background-color: rgb(227, 227, 227);\n"
"}")

        self.horizontalLayout_6.addWidget(self.testStartBtn)


        self.verticalLayout_6.addWidget(self.widget_2)

        self.testTimerLabel = QLabel(self.page_2)
        self.testTimerLabel.setObjectName(u"testTimerLabel")
        font5 = QFont()
        font5.setPointSize(20)
        self.testTimerLabel.setFont(font5)
        self.testTimerLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.testTimerLabel)

        self.testStack = QStackedWidget(self.page_2)
        self.testStack.setObjectName(u"testStack")
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_8 = QVBoxLayout(self.page_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.testsMainDisplay = QWidget(self.page_6)
        self.testsMainDisplay.setObjectName(u"testsMainDisplay")
        self.verticalLayout_7 = QVBoxLayout(self.testsMainDisplay)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.testCardLabel = QLabel(self.testsMainDisplay)
        self.testCardLabel.setObjectName(u"testCardLabel")
        self.testCardLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.testCardLabel)

        self.widget_4 = QWidget(self.testsMainDisplay)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy1.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy1)
        self.horizontalLayout_7 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.testCardInput = QLineEdit(self.widget_4)
        self.testCardInput.setObjectName(u"testCardInput")

        self.horizontalLayout_7.addWidget(self.testCardInput)

        self.testCardBtn = QPushButton(self.widget_4)
        self.testCardBtn.setObjectName(u"testCardBtn")
        self.testCardBtn.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_7.addWidget(self.testCardBtn)


        self.verticalLayout_7.addWidget(self.widget_4)


        self.verticalLayout_8.addWidget(self.testsMainDisplay)

        self.testStack.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.verticalLayout_10 = QVBoxLayout(self.page_7)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_3 = QWidget(self.page_7)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_9 = QVBoxLayout(self.widget_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.examScoreHeader = QLabel(self.widget_3)
        self.examScoreHeader.setObjectName(u"examScoreHeader")
        self.examScoreHeader.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.examScoreHeader)

        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_9.addWidget(self.label_3)

        self.examAnswerScroll = QScrollArea(self.widget_3)
        self.examAnswerScroll.setObjectName(u"examAnswerScroll")
        self.examAnswerScroll.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 98, 28))
        self.horizontalLayout_2 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.scrollItemsHolder = QWidget(self.scrollAreaWidgetContents)
        self.scrollItemsHolder.setObjectName(u"scrollItemsHolder")

        self.horizontalLayout_2.addWidget(self.scrollItemsHolder)

        self.examAnswerScroll.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_9.addWidget(self.examAnswerScroll)


        self.verticalLayout_10.addWidget(self.widget_3)

        self.testStack.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.testStack.addWidget(self.page_8)

        self.verticalLayout_6.addWidget(self.testStack)

        self.pagesStack.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_4 = QVBoxLayout(self.page_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.statsAnswersBtn = QPushButton(self.page_3)
        self.statsAnswersBtn.setObjectName(u"statsAnswersBtn")
        self.statsAnswersBtn.setStyleSheet(u"color: rgb(62, 162, 255);\n"
"border-radius: 5px;\n"
"background-color: 'white';\n"
"border: 2px solid rgb(62, 162, 255);\n"
"padding: 5px;\n"
"font-weight: 500;")

        self.horizontalLayout_5.addWidget(self.statsAnswersBtn)

        self.statsTestsBtn = QPushButton(self.page_3)
        self.statsTestsBtn.setObjectName(u"statsTestsBtn")
        self.statsTestsBtn.setStyleSheet(u"color: rgb(62, 162, 255);\n"
"border-radius: 5px;\n"
"background-color: 'white';\n"
"border: 2px solid rgb(62, 162, 255);\n"
"padding: 5px;\n"
"font-weight: 500;")

        self.horizontalLayout_5.addWidget(self.statsTestsBtn)

        self.statsOtherBtn = QPushButton(self.page_3)
        self.statsOtherBtn.setObjectName(u"statsOtherBtn")
        self.statsOtherBtn.setStyleSheet(u"color: rgb(62, 162, 255);\n"
"border-radius: 5px;\n"
"background-color: 'white';\n"
"border: 2px solid rgb(62, 162, 255);\n"
"padding: 5px;\n"
"font-weight: 500;")

        self.horizontalLayout_5.addWidget(self.statsOtherBtn)

        self.refreshStatsBtn = QPushButton(self.page_3)
        self.refreshStatsBtn.setObjectName(u"refreshStatsBtn")
        self.refreshStatsBtn.setMaximumSize(QSize(50, 27))
        self.refreshStatsBtn.setStyleSheet(u"color: rgb(62, 162, 255);\n"
"border-radius: 5px;\n"
"background-color: rgb(62, 162, 255);\n"
"border: 2px solid rgb(62, 162, 255);\n"
"padding: 5px;\n"
"font-weight: 500;")
        icon = QIcon()
        icon.addFile(u"storage/icons/refresh.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.refreshStatsBtn.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.refreshStatsBtn)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.statsStack = QStackedWidget(self.page_3)
        self.statsStack.setObjectName(u"statsStack")
        self.statsStack.setAutoFillBackground(False)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_5 = QVBoxLayout(self.page_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.correctPlot = QWidget(self.page_4)
        self.correctPlot.setObjectName(u"correctPlot")

        self.verticalLayout_5.addWidget(self.correctPlot)

        self.wrongPlot = QWidget(self.page_4)
        self.wrongPlot.setObjectName(u"wrongPlot")

        self.verticalLayout_5.addWidget(self.wrongPlot)

        self.statsStack.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.horizontalLayout_8 = QHBoxLayout(self.page_5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.prevExamsList = QListWidget(self.page_5)
        self.prevExamsList.setObjectName(u"prevExamsList")
        sizePolicy.setHeightForWidth(self.prevExamsList.sizePolicy().hasHeightForWidth())
        self.prevExamsList.setSizePolicy(sizePolicy)

        self.horizontalLayout_8.addWidget(self.prevExamsList)

        self.scrollArea = QScrollArea(self.page_5)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 98, 28))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.examsHistoryHolder = QWidget(self.scrollAreaWidgetContents_2)
        self.examsHistoryHolder.setObjectName(u"examsHistoryHolder")

        self.verticalLayout_12.addWidget(self.examsHistoryHolder)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_8.addWidget(self.scrollArea)

        self.statsStack.addWidget(self.page_5)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.statsStack.addWidget(self.page_9)

        self.verticalLayout_4.addWidget(self.statsStack)

        self.pagesStack.addWidget(self.page_3)

        self.verticalLayout.addWidget(self.pagesStack)


        self.verticalLayout_11.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 588, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.pagesStack.setCurrentIndex(1)
        self.testStack.setCurrentIndex(2)
        self.statsStack.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.trainButton.setText(QCoreApplication.translate("MainWindow", u"Trenuj", None))
        self.examButton.setText(QCoreApplication.translate("MainWindow", u"Test", None))
        self.statsButton.setText(QCoreApplication.translate("MainWindow", u"Statystyki", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Kategorie", None))
        self.choosenCategoryHeader.setText(QCoreApplication.translate("MainWindow", u"Wybrana kategoria:", None))
        self.cardName.setText(QCoreApplication.translate("MainWindow", u"Airplane", None))
        self.answerFeedbackLabel.setText("")
        self.flashcardButton.setText(QCoreApplication.translate("MainWindow", u"Sprawd\u017a", None))
        self.testEasyBtn.setText(QCoreApplication.translate("MainWindow", u"\u0141atwy", None))
        self.testMediumBtn.setText(QCoreApplication.translate("MainWindow", u"\u015aredni", None))
        self.testHardBtn.setText(QCoreApplication.translate("MainWindow", u"Trudny", None))
        self.testStartBtn.setText(QCoreApplication.translate("MainWindow", u"Rozpocznij", None))
        self.testTimerLabel.setText("")
        self.testCardLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.testCardBtn.setText(QCoreApplication.translate("MainWindow", u"Dalej", None))
        self.examScoreHeader.setText(QCoreApplication.translate("MainWindow", u"Wynik: 14/20 pkt. (70%)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Twoje odpowiedzi:", None))
        self.statsAnswersBtn.setText(QCoreApplication.translate("MainWindow", u"Odpowiedzi", None))
        self.statsTestsBtn.setText(QCoreApplication.translate("MainWindow", u"Testy", None))
        self.statsOtherBtn.setText(QCoreApplication.translate("MainWindow", u"Inne", None))
        self.refreshStatsBtn.setText("")
    # retranslateUi