import random
import time
from typing import Any, Union

from PySide6 import QtCore, QtWidgets, QtGui

from utils import get_random_address, get_random_person_name


class CustomModel(QtGui.QStandardItemModel):
    """
    Кастомная модель для работы с данными. Реализует возможность различного
    отображения данных в столбцах.
    """

    def __init__(self, parent=None):
        super(CustomModel, self).__init__(parent)

    def data(self, index: Union[QtCore.QModelIndex, QtCore.QPersistentModelIndex], role: int = ...) -> Any:
        """
        Функция переопределения выдачи данных для отображения

        :param index: элемент модели
        :param role: роль элемента в модели
        :return: Any
        """

        # отбор отображаемых элементов
        if role == QtCore.Qt.DisplayRole:
            pass
            # по колонке определяем то как отображать данные
            if index.column() == 0:
                try:
                    number = QtGui.QStandardItemModel.data(self, index, QtCore.Qt.DisplayRole)
                    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(number)))
                except ValueError:
                    pass

        # отбор фона строк
        if role == QtCore.Qt.BackgroundRole:
            if index.row() % 2:
                # возврат нового цвета фона
                return QtGui.QColor(QtCore.Qt.lightGray)

        return QtGui.QStandardItemModel.data(self, index, role)

    def getColumnNumberByName(self, column_name: str) -> int:
        """
        Метод возвращает номер столбца по его имени

        :param column_name: название столбца
        :return: номер столбца
        """

        for i in range(1, self.columnCount()):  # отсчёт с 1, т.к. 0 столбец это id и он не показывается
            if column_name == self.headerData(i, QtCore.Qt.Horizontal):
                return i



class DemoWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.loadTable()

    def initUi(self):

        self.resize(1200, 500)

        self.tableView = QtWidgets.QTableView()
        self.tableView.resizeColumnsToContents()

        self.pushButtonGetData = QtWidgets.QPushButton("Показать данные")
        self.pushButtonGetData.clicked.connect(self.getDataFromRow)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.tableView)
        layout.addWidget(self.pushButtonGetData)

        self.setLayout(layout)

    def getDataFromRow(self):
        selected_indexes = self.tableView.selectedIndexes()
        if selected_indexes:
            selected_index = selected_indexes[0]
            row = selected_index.row()
            column = selected_index.column()

        print(row, column)

    def loadTable(self):

        model = CustomModel()
        model.setHorizontalHeaderLabels(["Время", "Имя", "Адрес"])

        count = 20
        names = get_random_person_name(count)
        addresses = get_random_address(count)
        times = [int(time.time() + random.randint(0, 400)) for _ in range(count)]

        for name, address, elem_time in list(zip(names, addresses, times)):
            item_1 = QtGui.QStandardItem(str(elem_time))
            item_2 = QtGui.QStandardItem(str(name))
            item_3 = QtGui.QStandardItem(str(address))
            model.appendRow([item_1, item_2, item_3])

        self.tableView.setModel(model)
        self.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableView.resizeColumnsToContents()


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = DemoWindow()
    win.show()

    app.exec()
