# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QHBoxLayout, QHeaderView,
    QLCDNumber, QLabel, QLayout, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTableView,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(679, 382)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_7.addWidget(self.label)

        self.lineEditName = QLineEdit(Form)
        self.lineEditName.setObjectName(u"lineEditName")

        self.horizontalLayout_7.addWidget(self.lineEditName)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_6.addWidget(self.label_2)

        self.lineEditSurname = QLineEdit(Form)
        self.lineEditSurname.setObjectName(u"lineEditSurname")

        self.horizontalLayout_6.addWidget(self.lineEditSurname)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_5.addWidget(self.label_3)

        self.lineEditPhone = QLineEdit(Form)
        self.lineEditPhone.setObjectName(u"lineEditPhone")

        self.horizontalLayout_5.addWidget(self.lineEditPhone)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_4.addWidget(self.label_4)

        self.dateEditBirth = QDateEdit(Form)
        self.dateEditBirth.setObjectName(u"dateEditBirth")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEditBirth.sizePolicy().hasHeightForWidth())
        self.dateEditBirth.setSizePolicy(sizePolicy)
        self.dateEditBirth.setCalendarPopup(True)

        self.horizontalLayout_4.addWidget(self.dateEditBirth)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.pushButtonAdd = QPushButton(Form)
        self.pushButtonAdd.setObjectName(u"pushButtonAdd")

        self.horizontalLayout_2.addWidget(self.pushButtonAdd)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_8.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.lcdNumber = QLCDNumber(Form)
        self.lcdNumber.setObjectName(u"lcdNumber")

        self.horizontalLayout.addWidget(self.lcdNumber)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_8.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.tableView = QTableView(Form)
        self.tableView.setObjectName(u"tableView")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.tableView)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.pushButtonDel = QPushButton(Form)
        self.pushButtonDel.setObjectName(u"pushButtonDel")

        self.horizontalLayout_3.addWidget(self.pushButtonDel)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.pushButtonAdd.setText(QCoreApplication.translate("Form", u"Add", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u0412\u0441\u0435\u0433\u043e \u0441\u0442\u0440\u043e\u043a:", None))
        self.pushButtonDel.setText(QCoreApplication.translate("Form", u"Delete", None))
    # retranslateUi

