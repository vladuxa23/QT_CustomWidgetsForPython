from PySide6 import QtCore, QtWidgets, QtGui

from QWidget.ui.circular_widget import Ui_Form


class QCircularWidget(QtWidgets.QWidget):
    clicked = QtCore.Signal()

    def __init__(self, text: str = "", parent=None):
        super(QCircularWidget, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.labelTitle.setText(text)

        self.initUi()

    def initUi(self) -> None:
        """
        Доинициализация Ui

        :return: None
        """

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # Удаление titleBar
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # Установка прозрачного фона

        # добавление эффекта тени
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(10)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 120))
        self.ui.circularBg.setGraphicsEffect(self.shadow)

    def setText(self, text: str) -> None:
        """
        Установка текста на кнопку

        :param text: текст
        :return: None
        """

        self.ui.labelTitle.setText(text)

    def setProgressBarValue(self, value: int) -> None:
        """
        Установка значения прогресс бара

        :param value: значение
        :return: None
        """

        try:
            styleSheet = """
            QFrame{
                border-radius: 60px;
                background-color: qconicalgradient(
                                      cx:0.5, 
                                      cy:0.5, 
                                      angle:-{ANGLE}, 
                                      stop:1 rgba(255, 0, 127, 0), 
                                      stop:0 rgba(85, 170, 255, 255)
                                      );
            }
            """

            new_stylesheet = styleSheet.replace("{ANGLE}", str(270 + value))

            self.ui.circularProgress.setStyleSheet(new_stylesheet)
        except Exception as err:
            self.logger.exception(err)

    def event(self, event: QtCore.QEvent) -> bool:
        if event.type() == QtCore.QEvent.Type.MouseButtonPress:
            self.clicked.emit()

        return super(QCircularWidget, self).event(event)


if __name__ == '__main__':
    class DemoWindow(QtWidgets.QWidget):
        def __init__(self, parent=None):
            super().__init__(parent)

            self.pb_value = 0

            timer = QtCore.QTimer(self)
            timer.setInterval(10)
            timer.timeout.connect(self.setPBValue)

            self.button = QCircularWidget()
            self.button.ui.labelTitle.setText("Выполнить")
            self.button.clicked.connect(timer.start)

            layout = QtWidgets.QVBoxLayout()
            layout.addWidget(self.button)
            self.setLayout(layout)

        def setPBValue(self):
            self.pb_value += 1
            self.button.setProgressBarValue(self.pb_value)


    app = QtWidgets.QApplication()

    win = DemoWindow()
    win.show()

    app.exec()
