from PySide6 import QtCore, QtWidgets


class ImageViewer(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self) -> None:
        """

        :return:
        """

        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        label = QtWidgets.QLabel("Имя файла:")
        self.lineEdit = QtWidgets.QLineEdit()
        self.lineEdit.setReadOnly(True)

        layoutName = QtWidgets.QHBoxLayout()
        layoutName.addWidget(label)
        layoutName.addWidget(self.lineEdit)

        self.labelImage = QtWidgets.QLabel("Изображение не установлено")
        self.labelImage.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        self.labelImage.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelImage.setStyleSheet("border: 1px solid black;")
        self.pushButtonNext = QtWidgets.QPushButton(">")
        self.pushButtonNext.setMaximumWidth(15)
        self.pushButtonNext.setEnabled(False)
        self.pushButtonPrev = QtWidgets.QPushButton("<")
        self.pushButtonPrev.setMaximumWidth(15)
        self.pushButtonPrev.setEnabled(False)

        layoutButtons = QtWidgets.QHBoxLayout()
        layoutButtons.addWidget(self.pushButtonPrev)
        layoutButtons.addWidget(self.pushButtonNext)
        layoutButtons.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        layoutMain = QtWidgets.QVBoxLayout()
        layoutMain.addLayout(layoutName)
        layoutMain.addWidget(self.labelImage)
        layoutMain.addLayout(layoutButtons)

        self.setLayout(layoutMain)

    @property
    def image(self):
        return self.lineEdit.text(), self.labelImage.pixmap()

    @image.setter
    def image(self, image_name):
        self.setImage(image_name)

    def setImage(self, image: str) -> None:
        """

        :param image:
        :return:
        """

        self.lineEdit.setText(image)

        # вызов метода для получения байт из БД для картинки

    def clear(self) -> None:
        """

        :return:
        """

        self.labelImage.setText("Изображение не установлено")
        self.lineEdit.clear()


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = ImageViewer()
    #
    win.image = 'ui/loading_1.gif'
    print(win.image)


    win.show()

    app.exec_()
