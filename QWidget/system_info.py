from PySide6 import QtWidgets, QtCore


class SystemWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.system_value = QtWidgets.QProgressBar()
        self.system_value.setRange(0, 100)
        self.system_value.setOrientation(QtCore.Qt.Vertical)
        self.system_value.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )

        self.system_label = QtWidgets.QLabel()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.system_value)
        layout.addWidget(self.system_label)

        self.setLayout(layout)

    def setValue(self, value: int) -> None:
        """
        Установка значения system_value в CPUWidget

        :param value: новое значение
        :return: None
        """

        self.system_value.setValue(value)

    def setText(self, text: str) -> None:
        """
        Установка значения system_label в CPUWidget

        :param text: новый текст в виджете
        :return: None
        """

        self.system_label.setText(text)


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = SystemWidget()
    win.setValue(23)
    win.setText("Текст")
    win. show()

    app.exec()