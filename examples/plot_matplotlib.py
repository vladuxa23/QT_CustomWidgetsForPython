import random

import matplotlib
from PySide6 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT
from matplotlib.figure import Figure

matplotlib.use('Qt5Agg')


class MplCanvas(FigureCanvas):

    def __init__(self, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)

        self.axes = fig.add_subplot(111)
        self.axes = fig.add_subplot(111)

        # SET STYLE
        # fig.set(facecolor="#6272a4")
        # self.axes.set(facecolor="#87CEFA")

        super().__init__(fig)


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        n_data = 100
        self.x_data = list(range(n_data))
        self.y_data = [random.randint(0, 20) for i in range(n_data)]

        self.initUi()
        self.initTimer()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.canvas = MplCanvas(width=8, height=5, dpi=100)

        toolbar = NavigationToolbar2QT(self.canvas, self)
        toolbar.setObjectName('toolbar')

        label = QtWidgets.QLabel("Max")

        self.spinBoxMax = QtWidgets.QSpinBox()
        self.spinBoxMax.setRange(0, 100)

        paramLayout = QtWidgets.QHBoxLayout()
        paramLayout.addWidget(label)
        paramLayout.addWidget(self.spinBoxMax)
        paramLayout.addStretch(1)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addLayout(paramLayout)
        layout.addWidget(self.canvas)

        self.setLayout(layout)

    def initTimer(self) -> None:
        """
        Инициализация таймера

        :return: None
        """

        timer = QtCore.QTimer(self)
        timer.setInterval(100)
        timer.timeout.connect(self.update_plot)
        timer.start()

    def update_plot(self):
        num = self.spinBoxMax.value()

        if num == 0:
            num = random.randint(0, 100)
        self.y_data = self.y_data[1:] + [random.randint(0, num)]
        self.canvas.axes.cla()  # Clear the canvas.
        self.canvas.axes.plot(self.x_data, self.y_data, 'r')

        self.canvas.draw()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    win = Window()
    win.show()

    app.exec()
