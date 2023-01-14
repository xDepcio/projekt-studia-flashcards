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
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_3 = QWidget(Dialog)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.widget_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.widget_3)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.widget_3)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.originNameInput = QLineEdit(self.widget_2)
        self.originNameInput.setObjectName(u"originNameInput")

        self.horizontalLayout_2.addWidget(self.originNameInput)

        self.learnNameInput = QLineEdit(self.widget_2)
        self.learnNameInput.setObjectName(u"learnNameInput")

        self.horizontalLayout_2.addWidget(self.learnNameInput)

        self.categoryInput = QLineEdit(self.widget_2)
        self.categoryInput.setObjectName(u"categoryInput")

        self.horizontalLayout_2.addWidget(self.categoryInput)


        self.verticalLayout.addWidget(self.widget_2)


        self.verticalLayout_3.addWidget(self.widget_3)

        self.widget_5 = QWidget(Dialog)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.widget_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_6 = QLabel(self.widget_5)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.label_6)

        self.widget_4 = QWidget(self.widget_5)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.widget_4)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.horizontalSlider = QSlider(self.widget_4)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setValue(10)
        self.horizontalSlider.setSliderPosition(10)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QSlider.NoTicks)

        self.horizontalLayout_3.addWidget(self.horizontalSlider)

        self.label_4 = QLabel(self.widget_4)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)


        self.verticalLayout_2.addWidget(self.widget_4)


        self.verticalLayout_3.addWidget(self.widget_5)

        self.widget_6 = QWidget(Dialog)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.horizontalLayout_4 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btnImport = QPushButton(self.widget_6)
        self.btnImport.setObjectName(u"btnImport")

        self.horizontalLayout_4.addWidget(self.btnImport)

        self.btnBox = QDialogButtonBox(self.widget_6)
        self.btnBox.setObjectName(u"btnBox")
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
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Kategorie (rozdzielone przecinkami):", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Cz\u0119sto\u015b\u0107 wy\u015bwietlania:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Bardzo \u017cadko", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Bardzo cz\u0119sto", None))
        self.btnImport.setText(QCoreApplication.translate("Dialog", u"Importuj z pliku", None))
    # retranslateUi

