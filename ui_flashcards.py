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
        MainWindow.resize(681, 699)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_11 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_15 = QWidget(self.centralwidget)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(62, 162, 255);\n"
"	border: none;\n"
"	color: \"white\";\n"
"	padding-bottom: 10px;\n"
"	padding-top: 10px;\n"
"	border-radius: 9;\n"
"	font-weight: 500;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(42, 142, 255);\n"
"}")
        self.horizontalLayout_17 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.trainButton = QPushButton(self.widget_15)
        self.trainButton.setObjectName(u"trainButton")
        font = QFont()
        font.setBold(True)
        font.setWeight(62)
        self.trainButton.setFont(font)
        self.trainButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.trainButton.setStyleSheet(u"")

        self.horizontalLayout_17.addWidget(self.trainButton)

        self.examButton = QPushButton(self.widget_15)
        self.examButton.setObjectName(u"examButton")
        self.examButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.examButton.setStyleSheet(u"")

        self.horizontalLayout_17.addWidget(self.examButton)

        self.statsButton = QPushButton(self.widget_15)
        self.statsButton.setObjectName(u"statsButton")
        self.statsButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.statsButton.setStyleSheet(u"")

        self.horizontalLayout_17.addWidget(self.statsButton)


        self.horizontalLayout.addWidget(self.widget_15)


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

        self.widget_16 = QWidget(self.page)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setMinimumSize(QSize(0, 0))
        font2 = QFont()
        font2.setPointSize(8)
        self.widget_16.setFont(font2)
        self.widget_16.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(62, 162, 255);\n"
"	border: none;\n"
"	color: \"white\";\n"
"	padding-bottom: 7px;\n"
"	padding-top: 7px;\n"
"	border-radius: 5;\n"
"	font-weight: 500;\n"
"	font-size: 13px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(42, 142, 255);\n"
"}")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.btnAddCard = QPushButton(self.widget_16)
        self.btnAddCard.setObjectName(u"btnAddCard")
        self.btnAddCard.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAddCard.setStyleSheet(u"")

        self.horizontalLayout_18.addWidget(self.btnAddCard)


        self.verticalLayout_2.addWidget(self.widget_16)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.widget = QWidget(self.page)
        self.widget.setObjectName(u"widget")
        self.widget.setCursor(QCursor(Qt.ArrowCursor))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widgetCatExportLabel = QWidget(self.widget)
        self.widgetCatExportLabel.setObjectName(u"widgetCatExportLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widgetCatExportLabel.sizePolicy().hasHeightForWidth())
        self.widgetCatExportLabel.setSizePolicy(sizePolicy1)
        self.widgetCatExportLabel.setStyleSheet(u"QPushButton {\n"
"color: rgb(62, 162, 255);\n"
"border-radius: 5px;\n"
"background-color: 'white';\n"
"border: 2px solid rgb(62, 162, 255);\n"
"padding: 7px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"font-weight: 500;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(42, 142, 255);\n"
"	color: white;\n"
"	border-color: rgb(42, 142, 255);\n"
"}")
        self.horizontalLayout_16 = QHBoxLayout(self.widgetCatExportLabel)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.choosenCategoryHeader = QLabel(self.widgetCatExportLabel)
        self.choosenCategoryHeader.setObjectName(u"choosenCategoryHeader")
        sizePolicy1.setHeightForWidth(self.choosenCategoryHeader.sizePolicy().hasHeightForWidth())
        self.choosenCategoryHeader.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.choosenCategoryHeader.setFont(font3)
        self.choosenCategoryHeader.setStyleSheet(u"color: rgb(77, 77, 77);\n"
"font-weight: 600;")

        self.horizontalLayout_16.addWidget(self.choosenCategoryHeader)

        self.btnExport = QPushButton(self.widgetCatExportLabel)
        self.btnExport.setObjectName(u"btnExport")
        self.btnExport.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_16.addWidget(self.btnExport)


        self.verticalLayout_3.addWidget(self.widgetCatExportLabel)

        self.cardName = QLabel(self.widget)
        self.cardName.setObjectName(u"cardName")
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(False)
        font4.setWeight(50)
        self.cardName.setFont(font4)
        self.cardName.setStyleSheet(u"background-color: white;\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"margin: 0 10px;\n"
"color: rgb(26, 26, 26);")
        self.cardName.setLineWidth(1)
        self.cardName.setAlignment(Qt.AlignCenter)
        self.cardName.setMargin(0)
        self.cardName.setIndent(-1)

        self.verticalLayout_3.addWidget(self.cardName)

        self.answerFeedbackLabel = QLabel(self.widget)
        self.answerFeedbackLabel.setObjectName(u"answerFeedbackLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.answerFeedbackLabel.sizePolicy().hasHeightForWidth())
        self.answerFeedbackLabel.setSizePolicy(sizePolicy2)
        self.answerFeedbackLabel.setMinimumSize(QSize(0, 70))
        font5 = QFont()
        font5.setBold(False)
        font5.setWeight(50)
        self.answerFeedbackLabel.setFont(font5)
        self.answerFeedbackLabel.setStyleSheet(u"padding: 10px;\n"
"font-size: 18px;\n"
"font-weight: 400;\n"
"background-color: white;\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"margin: 0 10px;")
        self.answerFeedbackLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.answerFeedbackLabel)

        self.flashcardsInputsContainer = QWidget(self.widget)
        self.flashcardsInputsContainer.setObjectName(u"flashcardsInputsContainer")
        sizePolicy1.setHeightForWidth(self.flashcardsInputsContainer.sizePolicy().hasHeightForWidth())
        self.flashcardsInputsContainer.setSizePolicy(sizePolicy1)
        self.flashcardsInputsContainer.setBaseSize(QSize(0, 0))
        self.flashcardsInputsContainer.setCursor(QCursor(Qt.PointingHandCursor))
        self.flashcardsInputsContainer.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.flashcardsInputsContainer)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget_17 = QWidget(self.flashcardsInputsContainer)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setMinimumSize(QSize(0, 0))
        self.widget_17.setStyleSheet(u"QPushButton {\n"
"color: rgb(62, 162, 255);\n"
"border-radius: 5px;\n"
"background-color: 'white';\n"
"border: 2px solid rgb(62, 162, 255);\n"
"padding: 7px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"font-weight: 500;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: rgb(203, 46, 46);\n"
"border-color: rgb(203, 46, 46);\n"
"}")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.btnDelCard = QPushButton(self.widget_17)
        self.btnDelCard.setObjectName(u"btnDelCard")
        self.btnDelCard.setStyleSheet(u"")

        self.horizontalLayout_19.addWidget(self.btnDelCard)


        self.horizontalLayout_3.addWidget(self.widget_17)

        self.answerInput = QLineEdit(self.flashcardsInputsContainer)
        self.answerInput.setObjectName(u"answerInput")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.answerInput.sizePolicy().hasHeightForWidth())
        self.answerInput.setSizePolicy(sizePolicy3)
        font6 = QFont()
        font6.setPointSize(11)
        self.answerInput.setFont(font6)
        self.answerInput.setStyleSheet(u"border-radius: 4px;\n"
"border: 1px solid rgb(146, 146, 146);")

        self.horizontalLayout_3.addWidget(self.answerInput)

        self.widget_18 = QWidget(self.flashcardsInputsContainer)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setMinimumSize(QSize(0, 0))
        self.widget_18.setStyleSheet(u"QPushButton:enabled {\n"
"color: rgb(62, 162, 255);\n"
"border-radius: 5px;\n"
"background-color: 'white';\n"
"border: 2px solid rgb(62, 162, 255);\n"
"padding: 7px;\n"
"font-weight: 500;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"color: rgb(62, 162, 255);\n"
"border-radius: 5px;\n"
"padding: 7px;\n"
"font-weight: 500;\n"
"border: 2px solid rgb(118, 152, 184);\n"
"color: rgb(118, 152, 184);\n"
"background-color: rgb(227, 227, 227);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(42, 142, 255);\n"
"	color: white;\n"
"	border-color: rgb(42, 142, 255);\n"
"}")
        self.horizontalLayout_20 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.flashcardButton = QPushButton(self.widget_18)
        self.flashcardButton.setObjectName(u"flashcardButton")
        self.flashcardButton.setEnabled(False)
        self.flashcardButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_20.addWidget(self.flashcardButton)


        self.horizontalLayout_3.addWidget(self.widget_18)


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
        self.widget_2.setStyleSheet(u"QPushButton:enabled {\n"
"color: rgb(62, 162, 255);\n"
"border-radius: 5px;\n"
"background-color: 'white';\n"
"border: 2px solid rgb(62, 162, 255);\n"
"padding: 7px;\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"font-weight: 500;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"color: rgb(62, 162, 255);\n"
"border-radius: 5px;\n"
"padding: 7px;\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"font-weight: 500;\n"
"border: 2px solid rgb(118, 152, 184);\n"
"color: rgb(118, 152, 184);\n"
"background-color: rgb(227, 227, 227);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(42, 142, 255);\n"
"	color: white;\n"
"	border-color: rgb(42, 142, 255);\n"
"}\n"
"")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.testEasyBtn = QPushButton(self.widget_2)
        self.testEasyBtn.setObjectName(u"testEasyBtn")
        self.testEasyBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.testEasyBtn.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.testEasyBtn)

        self.testMediumBtn = QPushButton(self.widget_2)
        self.testMediumBtn.setObjectName(u"testMediumBtn")
        self.testMediumBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.testMediumBtn.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.testMediumBtn)

        self.testHardBtn = QPushButton(self.widget_2)
        self.testHardBtn.setObjectName(u"testHardBtn")
        self.testHardBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.testHardBtn.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.testHardBtn)

        self.horizontalSpacer = QSpacerItem(118, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.testStartBtn = QPushButton(self.widget_2)
        self.testStartBtn.setObjectName(u"testStartBtn")
        self.testStartBtn.setEnabled(False)
        self.testStartBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.testStartBtn.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.testStartBtn)


        self.verticalLayout_6.addWidget(self.widget_2)

        self.testTimerLabel = QLabel(self.page_2)
        self.testTimerLabel.setObjectName(u"testTimerLabel")
        font7 = QFont()
        font7.setPointSize(20)
        self.testTimerLabel.setFont(font7)
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
        font8 = QFont()
        font8.setFamily(u"Arial")
        font8.setPointSize(20)
        self.testCardLabel.setFont(font8)
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
        sizePolicy3.setHeightForWidth(self.testCardInput.sizePolicy().hasHeightForWidth())
        self.testCardInput.setSizePolicy(sizePolicy3)
        self.testCardInput.setFont(font6)
        self.testCardInput.setStyleSheet(u"border-radius: 4px;\n"
"border: 1px solid rgb(146, 146, 146);")

        self.horizontalLayout_7.addWidget(self.testCardInput)

        self.testCardBtn = QPushButton(self.widget_4)
        self.testCardBtn.setObjectName(u"testCardBtn")
        self.testCardBtn.setMinimumSize(QSize(150, 0))
        self.testCardBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.testCardBtn.setStyleSheet(u"QPushButton:enabled {\n"
"color: rgb(62, 162, 255);\n"
"border-radius: 5px;\n"
"background-color: 'white';\n"
"border: 2px solid rgb(62, 162, 255);\n"
"padding: 7px;\n"
"font-weight: 500;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"color: rgb(62, 162, 255);\n"
"border-radius: 5px;\n"
"padding: 7px;\n"
"font-weight: 500;\n"
"border: 2px solid rgb(118, 152, 184);\n"
"color: rgb(118, 152, 184);\n"
"background-color: rgb(227, 227, 227);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(42, 142, 255);\n"
"	color: white;\n"
"	border-color: rgb(42, 142, 255);\n"
"}")

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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 605, 376))
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
        self.statsAnswersBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.statsAnswersBtn.setStyleSheet(u"QPushButton {\n"
"color: rgb(62, 162, 255);\n"
"border-radius: 5px;\n"
"background-color: 'white';\n"
"border: 2px solid rgb(62, 162, 255);\n"
"padding: 5px;\n"
"font-weight: 500;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(42, 142, 255);\n"
"color: white;\n"
"border-color: rgb(42, 142, 255);\n"
"}")

        self.horizontalLayout_5.addWidget(self.statsAnswersBtn)

        self.statsTestsBtn = QPushButton(self.page_3)
        self.statsTestsBtn.setObjectName(u"statsTestsBtn")
        self.statsTestsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.statsTestsBtn.setStyleSheet(u"QPushButton {\n"
"color: rgb(62, 162, 255);\n"
"border-radius: 5px;\n"
"background-color: 'white';\n"
"border: 2px solid rgb(62, 162, 255);\n"
"padding: 5px;\n"
"font-weight: 500;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(42, 142, 255);\n"
"color: white;\n"
"border-color: rgb(42, 142, 255);\n"
"}")

        self.horizontalLayout_5.addWidget(self.statsTestsBtn)

        self.statsOtherBtn = QPushButton(self.page_3)
        self.statsOtherBtn.setObjectName(u"statsOtherBtn")
        self.statsOtherBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.statsOtherBtn.setStyleSheet(u"QPushButton {\n"
"color: rgb(62, 162, 255);\n"
"border-radius: 5px;\n"
"background-color: 'white';\n"
"border: 2px solid rgb(62, 162, 255);\n"
"padding: 5px;\n"
"font-weight: 500;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(42, 142, 255);\n"
"color: white;\n"
"border-color: rgb(42, 142, 255);\n"
"}")

        self.horizontalLayout_5.addWidget(self.statsOtherBtn)

        self.refreshStatsBtn = QPushButton(self.page_3)
        self.refreshStatsBtn.setObjectName(u"refreshStatsBtn")
        self.refreshStatsBtn.setMaximumSize(QSize(50, 27))
        self.refreshStatsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.refreshStatsBtn.setStyleSheet(u"QPushButton {\n"
"color: rgb(62, 162, 255);\n"
"border-radius: 5px;\n"
"background-color: rgb(62, 162, 255);\n"
"border: 2px solid rgb(62, 162, 255);\n"
"padding: 5px;\n"
"font-weight: 500;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(42, 142, 255);\n"
"color: white;\n"
"border-color: rgb(42, 142, 255);\n"
"}")
        icon = QIcon()
        iconThemeName = u"document-new"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
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

        self.daysShownLabel = QLabel(self.page_4)
        self.daysShownLabel.setObjectName(u"daysShownLabel")
        sizePolicy1.setHeightForWidth(self.daysShownLabel.sizePolicy().hasHeightForWidth())
        self.daysShownLabel.setSizePolicy(sizePolicy1)
        font9 = QFont()
        font9.setPointSize(12)
        font9.setBold(False)
        font9.setWeight(50)
        self.daysShownLabel.setFont(font9)
        self.daysShownLabel.setStyleSheet(u"")
        self.daysShownLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.daysShownLabel)

        self.daysSlider = QSlider(self.page_4)
        self.daysSlider.setObjectName(u"daysSlider")
        self.daysSlider.setMinimum(7)
        self.daysSlider.setMaximum(60)
        self.daysSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_5.addWidget(self.daysSlider)

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
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 361, 491))
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
        self.verticalLayout_13 = QVBoxLayout(self.page_9)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.widget_5 = QWidget(self.page_9)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy1.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy1)
        self.widget_5.setAutoFillBackground(False)
        self.widget_5.setStyleSheet(u"background-color: white;\n"
"border-radius: 7px;")
        self.verticalLayout_16 = QVBoxLayout(self.widget_5)
        self.verticalLayout_16.setSpacing(6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.widget_6 = QWidget(self.widget_5)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy1.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy1)
        self.verticalLayout_14 = QVBoxLayout(self.widget_6)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.widget_7 = QWidget(self.widget_6)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy1.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy1)
        self.horizontalLayout_12 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_2 = QLabel(self.widget_7)
        self.label_2.setObjectName(u"label_2")
        font10 = QFont()
        font10.setFamily(u"Arial")
        font10.setPointSize(12)
        font10.setBold(False)
        font10.setWeight(50)
        self.label_2.setFont(font10)

        self.horizontalLayout_12.addWidget(self.label_2)

        self.labelAllAnswers = QLabel(self.widget_7)
        self.labelAllAnswers.setObjectName(u"labelAllAnswers")
        font11 = QFont()
        font11.setFamily(u"Arial")
        font11.setPointSize(12)
        self.labelAllAnswers.setFont(font11)

        self.horizontalLayout_12.addWidget(self.labelAllAnswers)


        self.verticalLayout_14.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.widget_6)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy1.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy1)
        self.horizontalLayout_11 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_5 = QLabel(self.widget_8)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font11)

        self.horizontalLayout_11.addWidget(self.label_5)

        self.labelCorrectAnswers = QLabel(self.widget_8)
        self.labelCorrectAnswers.setObjectName(u"labelCorrectAnswers")
        self.labelCorrectAnswers.setFont(font11)

        self.horizontalLayout_11.addWidget(self.labelCorrectAnswers)


        self.verticalLayout_14.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.widget_6)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy1.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy1)
        self.horizontalLayout_10 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_9 = QLabel(self.widget_9)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font11)

        self.horizontalLayout_10.addWidget(self.label_9)

        self.labelWrongAnswers = QLabel(self.widget_9)
        self.labelWrongAnswers.setObjectName(u"labelWrongAnswers")
        self.labelWrongAnswers.setFont(font11)

        self.horizontalLayout_10.addWidget(self.labelWrongAnswers)


        self.verticalLayout_14.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.widget_6)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy1.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy1)
        self.horizontalLayout_9 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_11 = QLabel(self.widget_10)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font11)

        self.horizontalLayout_9.addWidget(self.label_11)

        self.labelAccuracy = QLabel(self.widget_10)
        self.labelAccuracy.setObjectName(u"labelAccuracy")
        self.labelAccuracy.setFont(font11)

        self.horizontalLayout_9.addWidget(self.labelAccuracy)


        self.verticalLayout_14.addWidget(self.widget_10)


        self.verticalLayout_16.addWidget(self.widget_6)

        self.widget_13 = QWidget(self.widget_5)
        self.widget_13.setObjectName(u"widget_13")
        self.verticalLayout_17 = QVBoxLayout(self.widget_13)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.widget_14 = QWidget(self.widget_13)
        self.widget_14.setObjectName(u"widget_14")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_4 = QLabel(self.widget_14)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font11)

        self.horizontalLayout_14.addWidget(self.label_4)

        self.labelExamsCount = QLabel(self.widget_14)
        self.labelExamsCount.setObjectName(u"labelExamsCount")
        self.labelExamsCount.setFont(font11)

        self.horizontalLayout_14.addWidget(self.labelExamsCount)


        self.verticalLayout_17.addWidget(self.widget_14)

        self.widget_exams_misc = QWidget(self.widget_13)
        self.widget_exams_misc.setObjectName(u"widget_exams_misc")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_exams_misc)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_7 = QLabel(self.widget_exams_misc)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font11)

        self.horizontalLayout_15.addWidget(self.label_7)

        self.labelExamsAccuracy = QLabel(self.widget_exams_misc)
        self.labelExamsAccuracy.setObjectName(u"labelExamsAccuracy")
        self.labelExamsAccuracy.setFont(font11)

        self.horizontalLayout_15.addWidget(self.labelExamsAccuracy)


        self.verticalLayout_17.addWidget(self.widget_exams_misc)


        self.verticalLayout_16.addWidget(self.widget_13)

        self.widget_11 = QWidget(self.widget_5)
        self.widget_11.setObjectName(u"widget_11")
        sizePolicy1.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy1)
        self.verticalLayout_15 = QVBoxLayout(self.widget_11)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.widget_12 = QWidget(self.widget_11)
        self.widget_12.setObjectName(u"widget_12")
        sizePolicy1.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy1)
        self.horizontalLayout_13 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_13 = QLabel(self.widget_12)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font11)

        self.horizontalLayout_13.addWidget(self.label_13)

        self.labelAppUseTime = QLabel(self.widget_12)
        self.labelAppUseTime.setObjectName(u"labelAppUseTime")
        self.labelAppUseTime.setFont(font11)

        self.horizontalLayout_13.addWidget(self.labelAppUseTime)


        self.verticalLayout_15.addWidget(self.widget_12)


        self.verticalLayout_16.addWidget(self.widget_11)


        self.verticalLayout_13.addWidget(self.widget_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer)

        self.statsStack.addWidget(self.page_9)

        self.verticalLayout_4.addWidget(self.statsStack)

        self.pagesStack.addWidget(self.page_3)

        self.verticalLayout.addWidget(self.pagesStack)


        self.verticalLayout_11.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 681, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.pagesStack.setCurrentIndex(0)
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
        self.btnAddCard.setText(QCoreApplication.translate("MainWindow", u"Dodaj fiszke", None))
        self.choosenCategoryHeader.setText(QCoreApplication.translate("MainWindow", u"Wybrana kategoria:", None))
        self.btnExport.setText(QCoreApplication.translate("MainWindow", u"Eksportuj kategorie", None))
        self.cardName.setText(QCoreApplication.translate("MainWindow", u"Airplane", None))
        self.answerFeedbackLabel.setText("")
        self.btnDelCard.setText(QCoreApplication.translate("MainWindow", u"Usu\u0144 fiszke", None))
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
        self.daysShownLabel.setText(QCoreApplication.translate("MainWindow", u"Wy\u015bwietlane ostatnie: 7 dni", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Odpowiedzi:", None))
        self.labelAllAnswers.setText(QCoreApplication.translate("MainWindow", u"222", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Poprawne:", None))
        self.labelCorrectAnswers.setText(QCoreApplication.translate("MainWindow", u"122", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"B\u0142\u0119dne", None))
        self.labelWrongAnswers.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Celno\u015b\u0107:", None))
        self.labelAccuracy.setText(QCoreApplication.translate("MainWindow", u"88%", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Rozwi\u0105zane testy:", None))
        self.labelExamsCount.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u015aredni wynik testu:", None))
        self.labelExamsAccuracy.setText(QCoreApplication.translate("MainWindow", u"40.0%", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Czas nauki:", None))
        self.labelAppUseTime.setText(QCoreApplication.translate("MainWindow", u"25 h", None))
    # retranslateUi

