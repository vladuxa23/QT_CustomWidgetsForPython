import ast

from PySide6 import QtWidgets, QtCore, QtGui


class ListWidgetRules(QtWidgets.QWidget):
    closeSignal = QtCore.Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.rules = None

        self.initUi()
        self.initSignals()

    # init -------------------------------------------------------------------------------------------------------------
    def initUi(self) -> None:
        """
        Доинициализация Ui

        :return: None
        """

        self.listWidget = QtWidgets.QListWidget()

        self.pushButtonAddRule = QtWidgets.QPushButton()
        self.pushButtonAddRule.setText("Добавить")

        self.pushButtonDelRule = QtWidgets.QPushButton()
        self.pushButtonDelRule.setText("Удалить")

        self.pushButtonOk = QtWidgets.QPushButton()
        self.pushButtonOk.setText("Ok")

        button_layout = QtWidgets.QVBoxLayout()
        button_layout.addWidget(self.pushButtonAddRule)
        button_layout.addWidget(self.pushButtonDelRule)
        button_layout.addSpacerItem(
            QtWidgets.QSpacerItem(1, 1, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        )
        button_layout.addWidget(self.pushButtonOk)

        main_layout = QtWidgets.QHBoxLayout()
        main_layout.addWidget(self.listWidget)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.pushButtonAddRule.clicked.connect(self.onPushButtonAddRuleClicked)
        self.pushButtonDelRule.clicked.connect(self.onPushButtonDelRuleClicked)
        self.pushButtonOk.clicked.connect(lambda: self.close())

    # events -----------------------------------------------------------------------------------------------------------
    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        """
        Обработка закрытия приложения

        :param event: QCloseEvent
        :return: bool
        """

        rules_list = []
        for i in range(self.listWidget.count()):
            rules_list.append(self.listWidget.item(i).text())

        self.closeSignal.emit(str(rules_list))

    def showEvent(self, event: QtGui.QShowEvent) -> None:
        """
        Обработка показа приложения

        :param event: QShowEvent
        :return: bool
        """

        if self.rules is not None:
            self.listWidget.clear()
            self.rules = ast.literal_eval(self.rules)

            sorted_rules = sorted(self.rules, key=lambda val: val.replace(val.rsplit('.', 2)[0], ''))

            for elem in sorted_rules:
                self.listWidget.addItem(elem)

    # slots ------------------------------------------------------------------------------------------------------------
    def onPushButtonAddRuleClicked(self) -> None:
        """
        Добавление нового правила

        :return: None
        """

        text, ok = QtWidgets.QInputDialog.getText(
            self, "", "Добавить новое правило", echo=QtWidgets.QLineEdit.EchoMode.Normal
        )

        if ok:
            if set(text) == {" "}:
                return

            if text in [self.listWidget.item(x).text() for x in range(self.listWidget.count())]:
                QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Данная запись уже есть', button0='ok')
                return
            self.listWidget.addItem(text)
            self.listWidget.sortItems(QtCore.Qt.SortOrder.AscendingOrder)

    def onPushButtonDelRuleClicked(self) -> None:
        """
        Удаление правила из списка

        :return: None
        """

        self.listWidget.takeItem(self.listWidget.currentRow())

if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = ListWidgetRules()
    win.closeSignal.connect(lambda data: print(data))
    win.show()

    app.exec()