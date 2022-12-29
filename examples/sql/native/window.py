import sys

from PySide6 import QtWidgets, QtCore, QtSql

from QSqlTableModel.custom import EditableSQLModel
from QStyledItemDelegate.no_edit import NoEditDelegate
from form import Ui_Form


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.initSQLModel()
        self.initUi()
        self.initSignals()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.setWindowTitle("БД")

        self.ui.tableView.setModel(self.model)
        self.ui.tableView.setColumnHidden(0, True)
        self.ui.tableView.horizontalHeader().setSectionsMovable(True)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tableView.setItemDelegateForColumn(4, NoEditDelegate())

        self.ui.lcdNumber.display(self.model.rowCount())

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.ui.pushButtonAdd.clicked.connect(self.onPushButtonAddClicked)
        self.ui.pushButtonDel.clicked.connect(self.onPushButtonDelClicked)

    def initSQLModel(self) -> None:
        """
        Создание подключения (модели) для работы с БД

        :return: None
        """

        # Загружаем драйвер и устанавливаем БД
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('fieldlist.db')

        # Создаём модель (можно использовать кастомную)
        self.model = EditableSQLModel()
        # self.model = QtSql.QSqlTableModel()
        self.model.setTable('field')

        self.model.select()
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "id")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Name")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Surname")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Birthday")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Phone")

    def onPushButtonAddClicked(self) -> None:
        """
        Обработка нажатия на кнопку добавить

        :return: None
        """

        index = self.model.rowCount()
        self.model.insertRows(index, 1)
        self.model.setData(self.model.index(index, 1), self.ui.lineEditName.text())
        self.model.setData(self.model.index(index, 2), self.ui.lineEditSurname.text())
        self.model.setData(self.model.index(index, 4), self.ui.lineEditPhone.text())
        self.model.setData(self.model.index(index, 3), self.ui.dateEditBirth.text())
        self.model.submitAll()

        self.ui.lcdNumber.display(self.model.rowCount())

    def onPushButtonDelClicked(self) -> None:
        """
        Обработка нажатия на кнопку удалить

        :return: None
        """

        if self.ui.tableView.currentIndex().row() > -1:
            self.model.removeRow(self.ui.tableView.currentIndex().row())
            self.model.select()
            self.ui.lcdNumber.display(self.model.rowCount())
        else:
            QtWidgets.QMessageBox.question(self, 'Уведомление', 'Пожалуйста, выберите строку для удаления',
                                           QtWidgets.QMessageBox.Ok)


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    win = Window()
    win.show()
    app.exec()
