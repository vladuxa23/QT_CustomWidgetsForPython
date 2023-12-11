from PySide6 import QtWidgets, QtCore

from QLineEdit.only_numbers import QLineEditOnlyNumbers
from QSS.button import QPushButtonDel, QPushButtonAdd


class QLineEditSpinned(QtWidgets.QWidget):
    valueChanged = QtCore.Signal(int)

    def __init__(self, label="", value: int = None, parent=None):
        super().__init__(parent)

        self.initUi(label, value)

        self.min_value = 0

    def initUi(self, label, value):

        label = QtWidgets.QLabel(f"<b>{label}:</b>")
        label.setMinimumWidth(180)
        lineEdit = QLineEditOnlyNumbers("0" if value is None else str(value))
        lineEdit.textChanged.connect(self.ifValueChanged)
        lineEdit.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)

        pbAdd = QPushButtonAdd()
        pbAdd.setMaximumWidth(22)
        pbAdd.clicked.connect(self.onPBAddClicked)
        pbDel = QPushButtonDel()
        pbDel.setMaximumWidth(22)
        pbDel.clicked.connect(self.onPBDelClicked)

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(lineEdit)
        layout.addWidget(pbAdd)
        layout.addWidget(pbDel)

        layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout)

    @property
    def value(self):
        le = self.layout().itemAt(1).widget()
        le_text = le.text()
        if not le_text:
            return 0
        return int(le_text)

    @value.setter
    def value(self, data):
        le = self.layout().itemAt(1).widget()
        le.setText(str(data))
        self.valueChanged.emit(int(data))

    @property
    def min_value(self):
        return self.__min_value

    @min_value.setter
    def min_value(self, data):
        if not isinstance(data, int):
            raise ValueError

        self.__min_value = data

    def onPBAddClicked(self):
        le = self.layout().itemAt(1).widget()
        le_text = le.text()
        if not le_text:
            le.setText('0')
            le_text = 0
        le.setText(str(int(le_text) + 1))

    def onPBDelClicked(self):
        le = self.layout().itemAt(1).widget()
        le_text = le.text()

        if not le_text:
            le.setText('0')
            le_text = 0
        result = int(le_text) - 1
        if result >= self.min_value:
            le.setText(str(result))

    def ifValueChanged(self, data):
        try:
            self.valueChanged.emit(int(data) if data else 0)
        except ValueError:
            pass


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = QLineEditSpinned("Папка")
    win.valueChanged.connect(lambda data: print(data))
    win.show()

    app.exec()
