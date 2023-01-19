# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'createCardDialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(582, 371)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setAutoFillBackground(False)
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 9)
        self.widget_7 = QWidget(Dialog)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy1)
        self.verticalLayout_4 = QVBoxLayout(self.widget_7)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.widget_3 = QWidget(self.widget_7)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy1.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy1)
        self.widget_3.setStyleSheet(u"background-color: white;\n"
"border-top-left-radius: 9px;\n"
"border-top-right-radius: 9px;")
        self.verticalLayout = QVBoxLayout(self.widget_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 35, -1, -1)
        self.widget = QWidget(self.widget_3)
        self.widget.setObjectName(u"widget")
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(26, 26, 26);")

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(26, 26, 26);")

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(26, 26, 26);")

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.widget_3)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.originNameInput = QLineEdit(self.widget_2)
        self.originNameInput.setObjectName(u"originNameInput")
        self.originNameInput.setFont(font)
        self.originNameInput.setStyleSheet(u"border-radius: 4px;\n"
"border: 1px solid rgb(146, 146, 146);\n"
"padding: 4px;\n"
"background-color: rgb(246, 246, 246);\n"
"")

        self.horizontalLayout_2.addWidget(self.originNameInput)

        self.learnNameInput = QLineEdit(self.widget_2)
        self.learnNameInput.setObjectName(u"learnNameInput")
        self.learnNameInput.setFont(font)
        self.learnNameInput.setStyleSheet(u"border-radius: 4px;\n"
"border: 1px solid rgb(146, 146, 146);\n"
"padding: 4px;\n"
"background-color: rgb(246, 246, 246);\n"
"")

        self.horizontalLayout_2.addWidget(self.learnNameInput)

        self.categoryInput = QLineEdit(self.widget_2)
        self.categoryInput.setObjectName(u"categoryInput")
        self.categoryInput.setFont(font)
        self.categoryInput.setStyleSheet(u"border-radius: 4px;\n"
"border: 1px solid rgb(146, 146, 146);\n"
"padding: 4px;\n"
"background-color: rgb(246, 246, 246);\n"
"")

        self.horizontalLayout_2.addWidget(self.categoryInput)


        self.verticalLayout.addWidget(self.widget_2)


        self.verticalLayout_4.addWidget(self.widget_3)

        self.widget_5 = QWidget(self.widget_7)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy1.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy1)
        self.widget_5.setStyleSheet(u"background-color: white;\n"
"border-bottom-left-radius: 9px;\n"
"border-bottom-right-radius: 9px;")
        self.verticalLayout_2 = QVBoxLayout(self.widget_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 38)
        self.label_6 = QLabel(self.widget_5)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(9)
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"color: rgb(26, 26, 26);")

        self.verticalLayout_2.addWidget(self.label_6)

        self.widget_4 = QWidget(self.widget_5)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy1.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy1)
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.widget_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: rgb(26, 26, 26);")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.horizontalSlider = QSlider(self.widget_4)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setCursor(QCursor(Qt.ArrowCursor))
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setValue(10)
        self.horizontalSlider.setSliderPosition(10)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QSlider.NoTicks)

        self.horizontalLayout_3.addWidget(self.horizontalSlider)

        self.label_4 = QLabel(self.widget_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(26, 26, 26);")

        self.horizontalLayout_3.addWidget(self.label_4)


        self.verticalLayout_2.addWidget(self.widget_4)


        self.verticalLayout_4.addWidget(self.widget_5)


        self.verticalLayout_3.addWidget(self.widget_7)

        self.widget_6 = QWidget(Dialog)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy1.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy1)
        self.horizontalLayout_4 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.btnImport = QPushButton(self.widget_6)
        self.btnImport.setObjectName(u"btnImport")
        self.btnImport.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnImport.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(62, 162, 255);\n"
"	border: none;\n"
"	color: \"white\";\n"
"	padding-bottom: 7px;\n"
"	padding-top: 7px;\n"
"	padding-right: 15px;\n"
"	padding-left: 15px;\n"
"	border-radius: 5;\n"
"	font-weight: 500;\n"
"	font-size: 13px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(42, 142, 255);\n"
"}")

        self.horizontalLayout_4.addWidget(self.btnImport)

        self.btnBox = QDialogButtonBox(self.widget_6)
        self.btnBox.setObjectName(u"btnBox")
        self.btnBox.setCursor(QCursor(Qt.ArrowCursor))
        self.btnBox.setStyleSheet(u"color: rgb(26, 26, 26);")
        self.btnBox.setOrientation(Qt.Horizontal)
        self.btnBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.horizontalLayout_4.addWidget(self.btnBox)


        self.verticalLayout_3.addWidget(self.widget_6)


        self.retranslateUi(Dialog)
        self.btnBox.accepted.connect(Dialog.accept)
        self.btnBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Nazwa po Polsku:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Nazwa po Angielsku:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Kategorie rozdzielone \",\":", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Cz\u0119sto\u015b\u0107 wy\u015bwietlania:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Bardzo \u017cadko", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Bardzo cz\u0119sto", None))
        self.btnImport.setText(QCoreApplication.translate("Dialog", u"Importuj z pliku", None))
    # retranslateUi

