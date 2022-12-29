"""PySide6 port of the Pie Chart Example from Qt v5.x"""
import random
import sys
from PySide6 import QtWidgets, QtCore, QtGui, QtCharts


class Window(QtWidgets.QWidget):

    def __init__(self, data, parent=None):
        super().__init__(parent)

        self.data = data
        self.current_slice: tuple = None

        self.initChart()
        self.initUi()
        self.initSignals()

    def initUi(self) -> None:
        """
        Инициализация графа

        :return: None
        """

        self.resize(400, 300)

        self.chart_view = QtCharts.QChartView(self.chart)
        self.chart_view.setRenderHint(QtGui.QPainter.Antialiasing)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.chart_view)

        self.setLayout(layout)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """
        self.series.clicked.connect(self.onSliceClicked)

    def initChart(self) -> None:
        """
        Инициализация графа

        :return: None
        """

        self.series = QtCharts.QPieSeries()

        for elem, value in self.data:
            slice = QtCharts.QPieSlice(elem, value)
            self.series.append(slice)

        self.chart = QtCharts.QChart()
        self.chart.addSeries(self.series)
        self.chart.setTitle('Распределение товара')

    def onSliceClicked(self, slice: QtCharts.QPieSlice) -> None:
        """
        Активация выбранного элемента

        :param slice: элемент piechart на который нажали
        :return: None
        """

        if self.current_slice:
            self.current_slice[0].setExploded(False)
            self.current_slice[0].setLabelVisible(False)
            self.current_slice[0].setPen(self.current_slice[1])
            self.current_slice[0].setBrush(self.current_slice[2])

        self.current_slice = slice, slice.pen(), slice.brush()

        slice.setExploded(True)
        slice.setLabelVisible(True)
        slice.setPen(QtGui.QPen(QtCore.Qt.darkGreen, 2))
        slice.setBrush(QtCore.Qt.green)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    labels = ["Апельсины", "Мандарины", "Шоколад", "Мармелад"]
    data = [(labels[i], random.randint(100, 400)) for i in range(len(labels))]

    window = Window(data)
    window.show()

    app.exec()
