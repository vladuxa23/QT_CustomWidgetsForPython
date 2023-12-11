from PySide6 import QtWidgets, QtCore


class LoginDialog(QtWidgets.QDialog):
    entered = QtCore.Signal(dict)
    registered = QtCore.Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initSignals()

    def initUi(self):
        """

        :return:
        """

        self.setWindowTitle("Вход")
        self.setFixedSize(250, 150)

        self.labelLogin = QtWidgets.QLabel("Логин")
        self.labelLogin.setMinimumWidth(40)
        self.lineEditLogin = QtWidgets.QLineEdit()

        self.labelPassword = QtWidgets.QLabel("Пароль")
        self.labelPassword.setMinimumWidth(40)
        self.lineEditPassword = QtWidgets.QLineEdit()
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        layoutLogin = QtWidgets.QHBoxLayout()
        layoutLogin.addWidget(self.labelLogin)
        layoutLogin.addWidget(self.lineEditLogin)

        layoutPassword = QtWidgets.QHBoxLayout()
        layoutPassword.addWidget(self.labelPassword)
        layoutPassword.addWidget(self.lineEditPassword)

        self.pushButtonRegistration = QtWidgets.QPushButton("Регистрация")
        self.pushButtonRegistration.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed,
            QtWidgets.QSizePolicy.Policy.Fixed
        )

        self.pushButtonEnter = QtWidgets.QPushButton("Вход")

        self.checkBox = QtWidgets.QCheckBox("Сохранять настройки")

        layoutMain = QtWidgets.QVBoxLayout()
        layoutMain.addWidget(self.pushButtonRegistration, alignment=QtCore.Qt.AlignmentFlag.AlignRight)
        layoutMain.addLayout(layoutLogin)
        layoutMain.addLayout(layoutPassword)
        layoutMain.addWidget(self.pushButtonEnter)
        layoutMain.addWidget(self.checkBox)

        self.setLayout(layoutMain)

    def initSignals(self):
        self.pushButtonEnter.clicked.connect(self.onPushButtonEnteredClicked)
        self.pushButtonRegistration.clicked.connect(lambda: self.registered.emit())

    @property
    def data(self):
        return {
            "login": self.lineEditLogin.text(),
            "password": self.lineEditPassword.text(),
            "saved_status": self.checkBox.isChecked()
        }

    @data.setter
    def data(self, value: dict):
        self.lineEditLogin.setText(value["login"])
        self.lineEditPassword.setText(value["password"])
        self.checkBox.setChecked(value["saved_status"])

    def onPushButtonEnteredClicked(self):
        if not self.data["login"]:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Логин не указан")
            return

        if not self.data["password"]:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Пароль не указан")
            return

        self.entered.emit(self.data)


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = LoginDialog()
    win.registered.connect(lambda: print("registered is good, without data"))
    win.entered.connect(lambda x: print("entered is good, data:", x))

    win.show()

    app.exec_()
