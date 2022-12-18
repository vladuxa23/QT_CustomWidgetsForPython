# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'circular_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QFrame, QGridLayout, QLabel,
                               QVBoxLayout)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(145, 144)
        Form.setMinimumSize(QSize(145, 144))
        Form.setMaximumSize(QSize(145, 144))
        self.verticalLayout_5 = QVBoxLayout(Form)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.circularProgressBarBase = QFrame(Form)
        self.circularProgressBarBase.setObjectName(u"circularProgressBarBase")
        self.circularProgressBarBase.setFrameShape(QFrame.NoFrame)
        self.circularProgressBarBase.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.circularProgressBarBase)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.circularBg = QFrame(self.circularProgressBarBase)
        self.circularBg.setObjectName(u"circularBg")
        self.circularBg.setStyleSheet(u"")
        self.circularBg.setFrameShape(QFrame.NoFrame)
        self.circularBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.circularBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.circularProgress = QFrame(self.circularBg)
        self.circularProgress.setObjectName(u"circularProgress")
        self.circularProgress.setMaximumSize(QSize(122, 122))
        self.circularProgress.setStyleSheet(u"")
        self.circularProgress.setFrameShape(QFrame.NoFrame)
        self.circularProgress.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.circularProgress)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.container = QFrame(self.circularProgress)
        self.container.setObjectName(u"container")
        self.container.setStyleSheet(u"#container{\n"
"	border-radius: 52px;\n"
"	background-color: rgb(77, 77, 127);\n"
"}\n"
"\n"
"#container:hover{\n"
"	border-radius: 52px;\n"
"	background-color: rgb(138, 99, 255);\n"
"}\n"
"")
        self.container.setFrameShape(QFrame.NoFrame)
        self.container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelTitle = QLabel(self.container)
        self.labelTitle.setObjectName(u"labelTitle")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        self.labelTitle.setFont(font)
        self.labelTitle.setStyleSheet(u"#labelTitle{background-color: none;\n"
"color: #FFFFFF}")
        self.labelTitle.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelTitle, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.verticalLayout_2.addWidget(self.container)


        self.verticalLayout_3.addWidget(self.circularProgress)


        self.verticalLayout_4.addWidget(self.circularBg)


        self.verticalLayout_5.addWidget(self.circularProgressBarBase)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.labelTitle.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:400; color:#fff;\">\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c</span></p><p><span style=\" font-weight:400; color:#fff;\"> \u0437\u0430\u043f\u0440\u043e\u0441</span></p></body></html>", None))
    # retranslateUi

