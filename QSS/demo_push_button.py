from PySide6 import QtCore, QtWidgets, QtGui

from utils import load_style


class DemoPushButton(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.count = 0

        self.initUi()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        button_ok = QtWidgets.QPushButton("Ok")
        button_ok.setStyleSheet(load_style("QPushButtonNormal.qss"))

        button_unsaved = QtWidgets.QPushButton("Unsaved")
        button_unsaved.setStyleSheet(load_style("QPushButtonUnsaved.qss"))

        button_cancel = QtWidgets.QPushButton("Cancel")
        button_cancel.setStyleSheet(load_style("QPushButtonCancel.qss"))

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(button_ok)
        layout.addWidget(button_unsaved)
        layout.addWidget(button_cancel)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = DemoPushButton()
    myapp.show()

    app.exec()
