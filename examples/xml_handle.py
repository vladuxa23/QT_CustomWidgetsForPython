import xml.etree.ElementTree as ET

import requests
from PySide6 import QtWidgets, QtCore, QtGui


# https://cbr.ru/development/SXML/  # подробнее об API

class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()
        self.initSignals()

        self.loadData("http://www.cbr.ru/scripts/XML_daily.asp?")

    def initUI(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.setWindowTitle("Курс валют")
        self.setFixedSize(250, 400)

        labelChooseCurrency = QtWidgets.QLabel("Выберите валюту")

        self.comboBoxCurrency = QtWidgets.QComboBox()

        labelChooseDate = QtWidgets.QLabel("Выберите дату")

        self.dateEdit = QtWidgets.QDateEdit()
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QtCore.QDate.currentDate())

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)

        self.labelResult = QtWidgets.QLabel()
        self.labelResult.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.labelResult.setAlignment(QtCore.Qt.AlignCenter)
        self.labelResult.setFont(font)
        self.labelResult.setStyleSheet("color: green")

        layoutV = QtWidgets.QVBoxLayout()
        layoutV.addWidget(labelChooseCurrency)
        layoutV.addWidget(self.comboBoxCurrency)
        layoutV.addWidget(labelChooseDate)
        layoutV.addWidget(self.dateEdit)
        layoutV.addWidget(self.labelResult)

        self.setLayout(layoutV)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.dateEdit.dateChanged.connect(self.refreshData)

        self.comboBoxCurrency.currentTextChanged.connect(
            lambda: self.labelResult.setText(self.currencyDict[self.comboBoxCurrency.currentText()])
        )

    def loadData(self, url: str) -> None:
        """
        Загрузка данных из сети

        :param url: адрес для запроса
        :return: None
        """

        getXml = requests.get(url)

        if getXml.status_code == 200:
            try:
                tree = ET.fromstring(getXml.content)
                currencyName = tree.findall("Valute/Name")
                currencyValue = tree.findall("Valute/Value")
                currencyName = [x.text for x in currencyName]
                currencyValue = [x.text for x in currencyValue]

                self.currencyDict = dict(zip(currencyName, currencyValue))

                self.comboBoxCurrency.blockSignals(True)
                index = self.comboBoxCurrency.currentIndex()
                self.comboBoxCurrency.clear()
                self.comboBoxCurrency.addItems(list(self.currencyDict.keys()))
                self.comboBoxCurrency.setCurrentIndex(index)
                self.labelResult.setText(self.currencyDict[self.comboBoxCurrency.currentText()])
                self.comboBoxCurrency.blockSignals(False)

            except Exception as err:
                print(err)

    def refreshData(self) -> None:
        """
        Обновление данных

        :return: None
        """

        day = str(self.dateEdit.date().day())
        if len(day) == 1:
            day = "0" + day

        month = str(self.dateEdit.date().month())
        if len(month) == 1:
            month = "0" + month

        year = str(self.dateEdit.date().year())

        query = f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={day}/{month}/{year}'
        self.loadData(query)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
