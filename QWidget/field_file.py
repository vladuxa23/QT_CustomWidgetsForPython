import os

from PySide6 import QtWidgets, QtCore


class QLineEditFile(QtWidgets.QWidget):
    textChanged = QtCore.Signal(str)

    def __init__(self, label, file=None, parent=None):
        super().__init__(parent)

        self.initUi(label, file)

    def initUi(self, label, file):
        self.label = QtWidgets.QLabel(f"<b>{label}:</b>")
        self.label.setMinimumWidth(120)

        self.lineEditFile = QtWidgets.QLineEdit(file)
        self.lineEditFile.setSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                        QtWidgets.QSizePolicy.Fixed)
        self.lineEditFile.setReadOnly(True)

        self.pushButtonChooseFile = QtWidgets.QPushButton()
        self.pushButtonChooseFile.setText("...")
        self.pushButtonChooseFile.setMaximumWidth(22)
        self.pushButtonChooseFile.clicked.connect(self.onPushButtonChooseFileClicked)

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.lineEditFile)
        layout.addWidget(self.pushButtonChooseFile)
        layout.setContentsMargins(1, 1, 1, 1)

        self.setLayout(layout)

    def onPushButtonChooseFileClicked(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, "Выбор файла", dir=".")[0]

        if path:
            self.lineEditFile.setText(os.path.abspath(path))
            self.textChanged.emit(os.path.abspath(path))

    @property
    def file(self):
        return self.lineEditFile.text()

    @file.setter
    def file(self, value):
        self.lineEditFile.setText(os.path.abspath(value))


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = QLineEditFile("Файл")
    win.textChanged.connect(lambda data: print(data))
    win.show()

    app.exec()
