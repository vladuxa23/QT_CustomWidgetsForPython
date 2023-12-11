import ipaddress

from PySide6 import QtWidgets, QtCore, QtGui


class QLineEditField(QtWidgets.QWidget):
    textChanged = QtCore.Signal(str)

    def __init__(self, label, value: str = "", parent=None):
        super().__init__(parent)

        self.initUi(label, value)

    def initUi(self, label, value):
        labelField = QtWidgets.QLabel(f"<b>{label}:</b>")
        labelField.setMinimumWidth(180)

        lineEditField = QtWidgets.QLineEdit(value)
        lineEditField.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        lineEditField.textChanged.connect(self.textChanged.emit)

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(labelField)
        layout.addWidget(lineEditField)
        layout.setContentsMargins(1, 1, 1, 1)

        self.setLayout(layout)

    @property
    def value(self):
        return self.layout().itemAt(1).widget().text()

    @value.setter
    def value(self, value):
        self.layout().itemAt(1).widget().setText(value)

    def setReadOnly(self, status: bool) -> None:
        self.layout().itemAt(1).widget().setReadOnly(status)

    def setHiddenInput(self, status: bool) -> None:
        self.layout().itemAt(1).widget().setEchoMode(
            QtWidgets.QLineEdit.EchoMode.Password if status else QtWidgets.QLineEdit.EchoMode.Normal
        )


class QLineEditIpField(QLineEditField):
    def __init__(self, label, parent=None):
        super().__init__(label, parent)

        lineEdit = self.layout().itemAt(1).widget()
        lineEdit.setValidator(
            QtGui.QRegularExpressionValidator(QtCore.QRegularExpression(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"),
                                              self))
        lineEdit.textChanged.connect(self.validateIP)

    def validateIP(self, ip):

        lineEdit = self.layout().itemAt(1).widget()
        try:
            ipaddress.ip_address(ip)
            lineEdit.setStyleSheet("background-color: green")
        except ValueError:
            lineEdit.setStyleSheet("background-color: red")


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = QLineEditIpField("ip")
    win.textChanged.connect(lambda data: print(data))
    win.show()

    app.exec()