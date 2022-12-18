from PySide6 import QtCore, QtGui, QtWidgets

COLORS = [
    '#000000', '#141923', '#414168', '#3a7fa7', '#35e3e3', '#8fd970', '#5ebb49',
    '#458352', '#dcd37b', '#fffee5', '#ffd035', '#cc9245', '#a15c3e', '#a42f3b',
    '#f45b7a', '#c24998', '#81588d', '#bcb0c2', '#ffffff',
]


class QPaletteButton(QtWidgets.QPushButton):

    def __init__(self, color):
        super().__init__()

        self.color = color
        self.setFixedSize(QtCore.QSize(24, 24))
        self.setStyleSheet("background-color: %s;" % color)


class Canvas(QtWidgets.QLabel):

    def __init__(self):
        super().__init__()

        self.pen_color = QtGui.QColor('#000000')

        pixmap = QtGui.QPixmap(600, 300)
        self.setPixmap(pixmap)

        self.last_x, self.last_y = None, None

    def set_pen_color(self, color):
        self.pen_color = QtGui.QColor(color)

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        if self.last_x is None:  # Первое срабатывание
            self.last_x = event.x()
            self.last_y = event.y()
            return  # Игнорируем его

        canvas = self.pixmap()
        painter = QtGui.QPainter(canvas)
        p = painter.pen()
        p.setWidth(4)
        p.setColor(self.pen_color)
        painter.setPen(p)
        painter.drawLine(self.last_x, self.last_y, event.x(), event.y())
        painter.end()
        self.setPixmap(canvas)

        # Обновляем глобальные параметры точек X и Y
        self.last_x = event.x()
        self.last_y = event.y()

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        self.last_x = None
        self.last_y = None


class MainWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.canvas = Canvas()

        palette = QtWidgets.QHBoxLayout()
        self.add_palette_buttons(palette)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addLayout(palette)

        self.setLayout(layout)

    def add_palette_buttons(self, layout):
        for c in COLORS:
            b = QPaletteButton(c)
            b.pressed.connect(lambda c=c: self.canvas.set_pen_color(c))
            layout.addWidget(b)


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = MainWindow()
    window.show()
    app.exec()
