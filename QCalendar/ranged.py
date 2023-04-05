from PySide6 import QtWidgets, QtCore, QtGui


class RangedCalendar(QtWidgets.QCalendarWidget):
    def __init__(self):
        super().__init__()
        self.fromDate = None
        self.toDate = None

        self.initUi()
        self.initSignals()

        super().dateTextFormat()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.highlighterFormat = QtGui.QTextCharFormat()
        # кстанавливаем стандартную подсветку дат
        self.highlighterFormat.setBackground(self.palette().brush(QtGui.QPalette.Highlight))
        self.highlighterFormat.setForeground(self.palette().color(QtGui.QPalette.HighlightedText))

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.clicked.connect(self.selectRange)

    def highlightRange(self, f: QtGui.QTextCharFormat) -> None:
        """
        Подсветка выбранного диапазона

        :param f: формат подсветки
        :return: None
        """

        if self.fromDate and self.toDate:
            d1 = min(self.fromDate, self.toDate)
            d2 = max(self.fromDate, self.toDate)
            while d1 <= d2:
                self.setDateTextFormat(d1, f)
                d1 = d1.addDays(1)

    def selectRange(self, dateValue: QtCore.QDate) -> None:
        """
        Выбор диапазона дат

        :param dateValue: выбранная дата
        :return: None
        """

        self.highlightRange(QtGui.QTextCharFormat())

        if QtWidgets.QApplication.instance().keyboardModifiers() & QtCore.Qt.ShiftModifier and self.fromDate:
            self.toDate = dateValue
            self.highlightRange(self.highlighterFormat)
        else:
            self.fromDate = dateValue
            self.toDate = None


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    myApp = RangedCalendar()
    myApp.show()

    app.exec()
