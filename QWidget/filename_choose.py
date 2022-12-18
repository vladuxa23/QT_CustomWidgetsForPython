import os.path

from PySide6 import QtWidgets, QtCore


class QFolderChooseWidget(QtWidgets.QWidget):
    choosedFolder = QtCore.Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initSignals()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.lineEdit = QtWidgets.QLineEdit()
        self.lineEdit.setReadOnly(True)

        self.pushButton = QtWidgets.QPushButton("Обзор")

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.pushButton)

        self.setLayout(layout)

    def initSignals(self) -> None:
        """
        Инициализация сигналов
        :return:
        """

        self.pushButton.clicked.connect(self.onPushButtonClicked)

    def onPushButtonClicked(self) -> None:
        """
        Выбор пути к файлу

        :return: None
        """

        folder_name = QtWidgets.QFileDialog.getExistingDirectory(self, "Выбор папки")
        if folder_name:
            folder_name = os.path.abspath(folder_name)
            self.lineEdit.setText(folder_name)
            self.choosedFolder.emit(folder_name)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = QFolderChooseWidget()
    window.show()

    app.exec()
