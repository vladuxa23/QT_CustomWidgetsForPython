from PySide6 import QtWidgets, QtCore


class QCheckBoxField(QtWidgets.QWidget):
    stateChanged = QtCore.Signal(bool)

    def __init__(self, label="", value: bool = False, parent=None):
        super().__init__(parent)

        self.initUi(label, value)

    def initUi(self, label, value):
        label = QtWidgets.QLabel(f"<b>{label}</b>")

        checkBox = QtWidgets.QCheckBox("")
        checkBox.setChecked(value)
        checkBox.stateChanged.connect(self.ifStateChanged)

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(checkBox)

        layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout)

    def ifStateChanged(self, data):
        self.stateChanged.emit(True if data else False)

    @property
    def value(self):
        le: QtWidgets.QCheckBox = self.layout().itemAt(1).widget()
        return le.isChecked()

    @value.setter
    def value(self, data: bool):
        le: QtWidgets.QCheckBox = self.layout().itemAt(1).widget()
        le.setChecked(data)
        self.stateChanged.emit(data)


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = QCheckBoxField("Test")
    win.stateChanged.connect(lambda data: print(data))
    win.value = True
    print(win.value)
    win.show()

    app.exec_()
