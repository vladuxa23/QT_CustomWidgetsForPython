from PySide6 import QtCore, QtWidgets, QtGui

from utils import get_random_person_name


class QCheckableComboBox(QtWidgets.QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self) -> None:
        """
        Доинициализация Ui

        :return: None
        """

        self.setMaxVisibleItems(25)

    # events -----------------------------------------------------------------------------------------------------------
    def event(self, event: QtCore.QEvent) -> bool:
        """
        Обработка различных типов ивентов

        :param event: QEvent
        :return: bool
        """

        if event.type() == QtCore.QEvent.ToolTipChange:
            self.update()

        return super().event(event)

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        """
        Перерисовка комбобокса в соответствии с его содержимым

        :param event: QPaintEvent
        :return: None
        """

        painter = QtWidgets.QStylePainter(self)
        painter.setPen(self.palette().color(QtGui.QPalette.Text))

        options = QtWidgets.QStyleOptionComboBox()
        self.initStyleOption(options)
        options.currentText = ", ".join(self.checkedItems())

        painter.drawComplexControl(QtWidgets.QStyle.CC_ComboBox, options)
        painter.drawControl(QtWidgets.QStyle.CE_ComboBoxLabel, options)

        self.setToolTip("\n".join(self.checkedItems()))

    # overrides backend ------------------------------------------------------------------------------------------------
    def addItem(self, item: str, checked: bool = False, **kwargs) -> None:
        """
        Добавление в комбобокс элемента с чекбоксом

        :param item: название нового элемента
        :param checked: статус элемента
        :param kwargs: отсальные параметры
        :return: None
        """

        super(QCheckableComboBox, self).addItem(item)

        item = self.model().item(self.count() - 1, 0)
        item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        if checked:
            item.setCheckState(QtCore.Qt.Checked)
        else:
            item.setCheckState(QtCore.Qt.Unchecked)

    def addItems(self, items: list) -> None:
        """
        Добавление в комбобокс списка элементов

        :param items: список элементов
        :return: None
        """

        for elem in items:
            self.addItem(elem)

    # backend ----------------------------------------------------------------------------------------------------------
    def addItemsWithClear(self, items: list) -> None:
        """
        Обновление данных в комбобоксе с очисткой

        :param items: список строк
        :return: None
        """

        self.clear()
        self.addItems(items)

    def items(self) -> list:
        """
        Получение всех элементов комбобокса

        :return: список всех элементов
        """

        result = []
        for i in range(self.count()):
            result.append(self.itemText(i))
        return result

    def checkedItem(self, index: int) -> bool:
        """
        Возвращает статус чекбокса по номеру элемента

        :param index: номер элемента в комбобоксе
        :return: статус элемента
        """

        item = self.model().item(index, 0)
        return item.checkState() == QtCore.Qt.Checked

    def checkedItems(self) -> list:
        """
        Возвращает список элементов, у которых чексбокс активирован

        :return: список элементов
        """

        checkedItems = []
        for i in range(self.count()):
            if self.checkedItem(i):
                checkedItems.append(self.model().item(i, 0).text())

        return checkedItems


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = QCheckableComboBox()
    myapp.addItems(get_random_person_name())
    myapp.show()

    app.exec()
