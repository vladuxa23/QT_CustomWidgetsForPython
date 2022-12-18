import pyodbc
from PySide6 import QtWidgets, QtGui, QtCore
from conf import *


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initDB()
        self.initUi()
        self.initTableViewModel()
        self.initListViewModel()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.resize(1000, 600)

        self.tableView = QtWidgets.QTableView()
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.listView = QtWidgets.QListView()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.tableView)
        layout.addWidget(self.listView)

        self.setLayout(layout)

    def initTableViewModel(self) -> None:
        """
        Инициализация модели для таблицы

        :return: None
        """

        model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderLabels(["№ п/п", "Имя", "Группа", "Изменен"])

        self.cursor.execute("SELECT * FROM HumanResources.Department")
        data = self.cursor.fetchall()

        for elem in data:
            item1 = QtGui.QStandardItem(str(elem[0]))
            item2 = QtGui.QStandardItem(str(elem[1]))
            item3 = QtGui.QStandardItem(str(elem[2]))
            item4 = QtGui.QStandardItem(str(elem[3]))
            model.appendRow([item1, item2, item3, item4])

        self.tableView.setModel(model)

    def initListViewModel(self) -> None:
        """
        Инициализация модели для списка

        :return: None
        """

        self.cursor.execute("SELECT name FROM HumanResources.Department")
        data = [x[0] for x in self.cursor.fetchall()]

        self.listView.setModel(QtCore.QStringListModel(data))

    def initDB(self) -> None:
        """
        Инициализация подключения к БД

        :return: None
        """

        self.conn = pyodbc.connect(
            'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

        self.cursor = self.conn.cursor()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
