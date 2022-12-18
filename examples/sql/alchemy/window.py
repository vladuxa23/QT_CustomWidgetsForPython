from PySide6 import QtWidgets, QtCore

from model import addUser, getNames, getUser


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

        self.initSignals()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.pushButtonAdd = QtWidgets.QPushButton("Добавить пользователя")
        self.listViewPerson = QtWidgets.QListView()
        self.plainTextEditLog = QtWidgets.QPlainTextEdit()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.pushButtonAdd)
        layout.addWidget(self.listViewPerson)
        layout.addWidget(self.plainTextEditLog)

        self.setLayout(layout)

        self.loadUsers()

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.pushButtonAdd.clicked.connect(self.addNewUser)
        self.listViewPerson.clicked.connect(self.getUserInfo)

    def loadUsers(self) -> None:
        """
        Загрузка ФИО пользователей

        :return: None
        """

        sim = QtCore.QStringListModel(getNames())
        self.listViewPerson.setModel(sim)

    def addNewUser(self) -> None:
        """
        Добавление нового пользователя в БД

        :return: None
        """

        user = addUser()

        model = self.listViewPerson.model()

        new_row = model.rowCount()
        model.insertRow(new_row)
        model.setData(model.index(new_row, 0), f"{user.get('name')} {user.get('surname')}")

    def getUserInfo(self) -> None:
        """
        Получение информации о пользователе из БД

        :return: None
        """

        model = self.listViewPerson.model()
        insert_row_index = self.listViewPerson.selectionModel().selectedRows()[0]
        name, surname = tuple(model.data(insert_row_index).split(" "))

        user = getUser(name, surname)
        self.plainTextEditLog.setPlainText(
            f"Пользователь: {user.get('name')} {user.get('surname')}\n"
            f"Логин:              {user.get('login')}\n"
            f"Пароль:            {user.get('password')}\n"
            f"E-Mail:               {user.get('email')}\n"
            f"Телефон:         {user.get('phone')}\n"
            f"Дата рег.:       {user.get('register_time').isoformat()}\n"
        )


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    win = Window()
    win.show()

    app.exec()
