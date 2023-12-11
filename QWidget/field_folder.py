import os
from typing import Optional

from PySide6 import QtWidgets, QtCore


class QLineEditFolder(QtWidgets.QWidget):
    textChanged = QtCore.Signal(str)

    def __init__(self, label: Optional[str] = None, folder: Optional[str] = None, parent=None):
        super().__init__(parent)

        self.initUi(label)
        if folder is None:
            folder = os.getcwd()
        self.folder = folder

    def initUi(self, label: str) -> None:
        self.label = QtWidgets.QLabel("<b>Выбранная папка:</b>" if not label else f"<b>{label}:</b>")
        self.label.setMinimumWidth(120)
        self.lineEditFolder = QtWidgets.QLineEdit()
        self.lineEditFolder.setSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                          QtWidgets.QSizePolicy.Fixed)
        self.lineEditFolder.setReadOnly(True)

        self.pushButtonChooseFolder = QtWidgets.QPushButton()
        self.pushButtonChooseFolder.setText("...")
        self.pushButtonChooseFolder.setMaximumWidth(22)
        self.pushButtonChooseFolder.clicked.connect(self.onPushButtonChooseFolderClicked)

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.lineEditFolder)
        layout.addWidget(self.pushButtonChooseFolder)
        layout.setContentsMargins(1, 1, 1, 1)

        self.setLayout(layout)

    def onPushButtonChooseFolderClicked(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(self, "Выбор папки", dir='.')

        if path:
            self.lineEditFolder.setText(os.path.abspath(path))
            self.textChanged.emit(os.path.abspath(path))

    @property
    def folder(self):
        return self.lineEditFolder.text()

    @folder.setter
    def folder(self, value):
        self.lineEditFolder.setText(os.path.abspath(value))


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = QLineEditFolder("Папка")
    win.textChanged.connect(lambda data: print(data))
    win.show()

    app.exec()
