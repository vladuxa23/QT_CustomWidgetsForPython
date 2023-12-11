import os
from typing import Sequence, Union

from PySide6 import QtWidgets, QtCore, QtGui

from conf import ROOT_PATH


class EditableListView(QtWidgets.QWidget):
    added = QtCore.Signal(str)
    deleted = QtCore.Signal(str)
    selectionChanged = QtCore.Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initSignals()

    # inits ------------------------------------------------------------------------------------------------------------
    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        icon_add = QtGui.QIcon(os.path.join(ROOT_PATH, 'QSS', 'icons', 'add.png'))
        icon_del = QtGui.QIcon(os.path.join(ROOT_PATH, 'QSS', 'icons', 'minus.png'))

        self.__lineEditFilter = QtWidgets.QLineEdit()
        self.__lineEditFilter.setPlaceholderText("Найти...")

        self.__model = QtGui.QStandardItemModel(self)
        self.__proxyModel = QtCore.QSortFilterProxyModel(self)
        self.__proxyModel.setSourceModel(self.__model)

        self.__listView = QtWidgets.QListView()
        self.__listView.setModel(self.__proxyModel)

        self.__pbAdd = QtWidgets.QPushButton(icon=icon_add)
        self.__pbDel = QtWidgets.QPushButton(icon=icon_del)

        layout_pb = QtWidgets.QHBoxLayout()
        layout_pb.addSpacerItem(
            QtWidgets.QSpacerItem(10, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        )
        layout_pb.addWidget(self.__pbAdd)
        layout_pb.addWidget(self.__pbDel)
        layout_pb.setContentsMargins(0, 0, 0, 0)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.__lineEditFilter)
        layout.addWidget(self.__listView)
        layout.addLayout(layout_pb)
        layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout)

    def initSignals(self) -> None:
        """
        Инициализация сигналов
        :return: None
        """

        self.__pbAdd.clicked.connect(self.onPBAddClicked)
        self.__pbDel.clicked.connect(self.onPBDelClicked)

        self.__lineEditFilter.textChanged.connect(self.__filter)

        self.__listView.clicked.connect(lambda data: self.selectionChanged.emit(self.__listView.model().data(data)))

    # properties -------------------------------------------------------------------------------------------------------
    @property
    def items(self) -> None:
        """

        :return:
        """

        model = self.__listView.model()

        items = []
        for i in range(model.rowCount()):  # проверка на повторение
            items.append(model.data(model.index(i, 0)))

        return items

    @items.setter
    def items(self, new_items: Sequence[str]) -> None:
        """

        :param new_items:
        :return:
        """

        self.clear()

        for item in new_items:
            self.append(item, check_unique=True)

    @property
    def item(self):
        indexes = self.__listView.selectedIndexes()
        if len(indexes) > 0:
            return self.__listView.model().data(indexes[0])

    # slots ------------------------------------------------------------------------------------------------------------
    def onPBAddClicked(self) -> None:
        """

        :return:
        """

        answer, ok = QtWidgets.QInputDialog.getText(self, "Новый элемент", "Введите название нового элемента")

        if not ok or not answer.replace(" ", ""):
            return

        self.added.emit(answer)

    def onPBDelClicked(self) -> None:
        """

        :return:
        """

        indexes = self.__listView.selectedIndexes()
        if len(indexes) > 0:
            self.deleted.emit(self.__listView.model().data(indexes[0]))
        else:
            QtWidgets.QMessageBox.warning(self, 'Внимание', 'Ничего не выбрано')

    # backend ----------------------------------------------------------------------------------------------------------
    def append(self, item: str, check_unique: bool = False) -> None:
        """

        :param check_unique:
        :param item:
        :return:
        """

        if not isinstance(item, str):
            raise ValueError(f"{item} is not string")

        if check_unique:
            if not self.__is_unique_item(item):
                return False

        item = QtGui.QStandardItem(item)
        self.__model.appendRow(item)

        return True

    def remove(self, index: Union[str, QtCore.QModelIndex]):
        """

        :param index:
        :return:
        """

        if isinstance(index, str):
            model: QtCore.QAbstractProxyModel = self.__listView.model()

            for i in range(model.rowCount()):  # проверка на повторение
                row_text = model.data(model.index(i, 0))
                if row_text == index:
                    index = model.index(i, 0)
                    break
            else:
                return False

        self.__model.removeRow(index.row())
        return True

    def clear(self) -> None:
        """

        :return:
        """

        self.__model = QtGui.QStandardItemModel(self)
        self.__proxyModel = QtCore.QSortFilterProxyModel(self)
        self.__proxyModel.setSourceModel(self.__model)

        self.__listView.setModel(self.__proxyModel)
        self.__lineEditFilter.clear()

    def __is_unique_item(self, item):
        """

        :param item:
        :return:
        """

        model: QtCore.QAbstractProxyModel = self.__listView.model()

        for i in range(model.rowCount()):  # проверка на повторение
            row_text = model.data(model.index(i, 0))
            if row_text == item:
                return False

        return True

    def __filter(self):
        """

        :return:
        """

        model: QtCore.QSortFilterProxyModel = self.__listView.model()
        model.setFilterRegularExpression(QtCore.QRegularExpression(self.__lineEditFilter.text()))


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = EditableListView()
    win.items = ['1', '2', '3', '4', '5', '55', '45', '35', '25']
    win.added.connect(lambda data: print(data))
    win.deleted.connect(lambda data: print(data))
    win.selectionChanged.connect(lambda data: print(data))
    win.show()

    app.exec()