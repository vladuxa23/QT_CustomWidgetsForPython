from PySide6 import QtWidgets, QtCore


class RegistrationDialog(QtWidgets.QDialog):
    registered = QtCore.Signal(dict)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initSignals()

    def initUi(self):
        """

        :return:
        """

        self.setWindowTitle("Регистрация")
        self.setFixedSize(300, 140)

        self.__labelLogin = QtWidgets.QLabel("Логин")
        self.__labelLogin.setMinimumWidth(85)
        self.__lineEditLogin = QtWidgets.QLineEdit()

        self.__labelPassword = QtWidgets.QLabel("Пароль")
        self.__labelPassword.setMinimumWidth(85)
        self.__lineEditPassword = QtWidgets.QLineEdit()
        self.__lineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        self.__labelPasswordRepeat = QtWidgets.QLabel("Пароль еще раз")
        self.__labelPasswordRepeat.setMinimumWidth(85)
        self.__lineEditPasswordRepeat = QtWidgets.QLineEdit()
        self.__lineEditPasswordRepeat.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        layoutLogin = QtWidgets.QHBoxLayout()
        layoutLogin.addWidget(self.__labelLogin)
        layoutLogin.addWidget(self.__lineEditLogin)

        layoutPassword = QtWidgets.QHBoxLayout()
        layoutPassword.addWidget(self.__labelPassword)
        layoutPassword.addWidget(self.__lineEditPassword)

        layoutPasswordRepeat = QtWidgets.QHBoxLayout()
        layoutPasswordRepeat.addWidget(self.__labelPasswordRepeat)
        layoutPasswordRepeat.addWidget(self.__lineEditPasswordRepeat)

        self.__pushButtonRegistration = QtWidgets.QPushButton("Регистрация")
        self.__pushButtonRegistration.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed,
            QtWidgets.QSizePolicy.Policy.Fixed
        )

        layoutMain = QtWidgets.QVBoxLayout()
        layoutMain.addLayout(layoutLogin)
        layoutMain.addLayout(layoutPassword)
        layoutMain.addLayout(layoutPasswordRepeat)
        layoutMain.addWidget(self.__pushButtonRegistration, alignment=QtCore.Qt.AlignmentFlag.AlignRight)

        self.setLayout(layoutMain)

    def initSignals(self):
        """

        :return:
        """

        self.__pushButtonRegistration.clicked.connect(self.onPushButtonRegistrationClicked)

    @property
    def data(self):
        return {
            "login": self.__lineEditLogin.text(),
            "password": self.__lineEditPassword.text(),
        }

    def onPushButtonRegistrationClicked(self):
        """

        :return:
        """

        if not self.check_password_repeat():
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Введенные пароли не совпадают")
            return

        if not self.data["login"]:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Логин не указан")
            return

        if not self.data["password"]:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Пароль не указан")
            return

        self.registered.emit(self.data)

    def check_password_repeat(self):
        """

        :return:
        """

        return self.__lineEditPassword.text() == self.__lineEditPasswordRepeat.text()

    def clear(self) -> None:
        """

        :return:
        """

        self.__lineEditLogin.clear()
        self.__lineEditPassword.clear()
        self.__lineEditPasswordRepeat.clear()


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = RegistrationDialog()
    win.registered.connect(lambda x: print("registered is good, with data", x))

    win.show()

    app.exec_()
