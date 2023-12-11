from PySide6 import QtWidgets, QtCore, QtGui


class DBSettingsDialog(QtWidgets.QDialog):
    saved = QtCore.Signal(dict)
    closed = QtCore.Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initSignals()

    def closeEvent(self, arg__1:QtGui.QCloseEvent) -> None:
        """

        :param arg__1:
        :return:
        """

        self.closed.emit()



    def initUi(self):
        """

        :return:
        """

        self.setWindowTitle("Парамаетры БД")
        self.setFixedSize(400, 175)

        self.labelHost = QtWidgets.QLabel("Хост")
        self.labelHost.setMinimumWidth(80)
        self.lineEditHost = QtWidgets.QLineEdit()

        self.labelPort = QtWidgets.QLabel("Порт")
        self.labelPort.setMinimumWidth(80)
        self.lineEditPort = QtWidgets.QLineEdit("3306")

        self.labelDB = QtWidgets.QLabel("База данных")
        self.labelDB.setMinimumWidth(80)
        self.lineEditDB = QtWidgets.QLineEdit()

        self.labelUser = QtWidgets.QLabel("Пользователь")
        self.labelUser.setMinimumWidth(80)
        self.lineEditUser = QtWidgets.QLineEdit()

        self.labelPassword = QtWidgets.QLabel("Пароль")
        self.labelPassword.setMinimumWidth(80)
        self.lineEditPassword = QtWidgets.QLineEdit()
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        layoutHost = QtWidgets.QHBoxLayout()
        layoutHost.addWidget(self.labelHost)
        layoutHost.addWidget(self.lineEditHost)

        layoutPort = QtWidgets.QHBoxLayout()
        layoutPort.addWidget(self.labelPort)
        layoutPort.addWidget(self.lineEditPort)

        layoutDB = QtWidgets.QHBoxLayout()
        layoutDB.addWidget(self.labelDB)
        layoutDB.addWidget(self.lineEditDB)

        layoutUser = QtWidgets.QHBoxLayout()
        layoutUser.addWidget(self.labelUser)
        layoutUser.addWidget(self.lineEditUser)

        layoutPassword = QtWidgets.QHBoxLayout()
        layoutPassword.addWidget(self.labelPassword)
        layoutPassword.addWidget(self.lineEditPassword)

        self.pushButtonSave = QtWidgets.QPushButton("Сохранить")

        layoutMain = QtWidgets.QVBoxLayout()
        layoutMain.addLayout(layoutHost)
        layoutMain.addLayout(layoutPort)
        layoutMain.addLayout(layoutDB)
        layoutMain.addLayout(layoutUser)
        layoutMain.addLayout(layoutPassword)
        layoutMain.addWidget(self.pushButtonSave)

        self.setLayout(layoutMain)

    def initSignals(self):
        self.pushButtonSave.clicked.connect(self.onPushButtonSaveClicked)

    @property
    def data(self):
        return {
            "host": self.lineEditHost.text(),
            "port": self.lineEditPort.text(),
            "database": self.lineEditDB.text(),
            "user": self.lineEditUser.text(),
            "password": self.lineEditPassword.text(),
        }

    def onPushButtonSaveClicked(self):
        """

        :return:
        """

        for i in range(self.layout().count() - 1):
            label = self.layout().itemAt(i).itemAt(0).widget().text()
            line = self.layout().itemAt(i).itemAt(1).widget().text().replace(" ", "")

            if not line:
                QtWidgets.QMessageBox.warning(self, "Ошибка", f"Поле {label!r} не заполнено")
                return

        self.saved.emit(self.data)


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = DBSettingsDialog()
    win.saved.connect(lambda x: print("saved is good, data:", x))
    win.show()

    app.exec_()
