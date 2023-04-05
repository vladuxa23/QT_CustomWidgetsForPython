from PySide6 import QtCore, QtGui, QtWidgets


class AvailableDate:
    def __init__(self, date: QtCore.QDate, status: bool):
        self.date = date
        self.status = status

    def __eq__(self, other):
        if self.date == other.date and self.status == other.status:
            return True
        else:
            return False

    def __str__(self):
        return f"Дата {self.date}, статус {self.status}"

    def __repr__(self):
        return f"{self.__class__.__name__}(date={self.date!r}, status={self.status!r})"

    @property
    def date(self) -> QtCore.QDate:
        """
        Получение даты

        :return:
        """

        return self.__date

    @date.setter
    def date(self, value: QtCore.QDate) -> None:
        """
        Установка даты

        :param value: объект QDate
        :return: None
        """

        if not isinstance(value, QtCore.QDate):
            raise TypeError(f"Ожидается QtCore.QDate, получено {type(value)}")
        self.__date = value

    @property
    def status(self) -> bool:
        """
        Получение статуса

        :return:
        """

        return self.__status

    @status.setter
    def status(self, value: bool) -> None:
        """
        Установка статуса

        :param value: статус
        :return: None
        """

        if not isinstance(value, bool):
            raise TypeError(f"Ожидается bool, получено {type(value)}")
        self.__status = value


class ManagementCalendar(QtWidgets.QCalendarWidget):
    dateStatusChanged = QtCore.Signal(AvailableDate)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.availableDates = []

        self.initUi()
        self.initContextMenu()
        self.initSignals()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.setSelectedDate(QtCore.QDate.currentDate())
        self.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.clicked.connect(self.onCalendarClicked)
        self.customContextMenuRequested.connect(self.showContextMenu)

    def initContextMenu(self) -> None:
        """
        Генерация контекстного меню

        :return: None
        """

        set_day_available = QtGui.QAction("Сделать доступным", self)
        set_day_available.triggered.connect(lambda: self.appendAvailableDate(self.selectedDate()))

        set_day_unavailable = QtGui.QAction("Сделать недоступным", self)
        set_day_unavailable.triggered.connect(lambda: self.removeAvailableDate(self.selectedDate()))

        self.list_context_menu = QtWidgets.QMenu(self)
        self.list_context_menu.addActions([set_day_available, set_day_unavailable])

    def paintCell(self, painter: QtGui.QPainter, rect: QtCore.QRect, date: QtCore.QDate) -> None:
        """
        Перерисовка ячейки

        :param painter: объект Painter
        :param rect: объект Rect
        :param date: объект Date
        :return: None
        """

        QtWidgets.QCalendarWidget.paintCell(self, painter, rect, date)

        if AvailableDate(date, True) not in self.availableDates:
            painter.setBrush(QtGui.QColor(255, 0, 0, 50))
        else:
            painter.setBrush(QtGui.QColor(0, 255, 0, 50))

        painter.setPen(QtGui.QColor(0, 0, 0, 0))
        painter.drawRect(rect)

    def showContextMenu(self, point: QtCore.QPoint) -> None:
        """
        Показ контекстного меню

        :param point: координаты курсора
        :return: None
        """

        # TODO Не решена проблема клика ПКМ на дату другого месяца
        #  Возможное решение
        #  https://stackoverflow.com/questions/58313818/adding-items-to-a-qtableview-within-qcalendarwidget

        table_view: QtWidgets.QTableView = self.findChild(QtWidgets.QTableView)
        point = QtCore.QPoint(point.x(), point.y() - 20)

        try:
            year = self.yearShown()
            month = self.monthShown()
            day = int(table_view.indexAt(point).data(0))

            self.setSelectedDate(QtCore.QDate(year, month, day))
            self.setFocus()

            self.list_context_menu.exec(self.mapToGlobal(point))
        except (TypeError, ValueError):
            pass

    @property
    def availableDates(self) -> list:
        """
        Разрешенные даты

        :return: список с датами
        """

        return self.__availableDates

    @availableDates.setter
    def availableDates(self, value):
        self.__availableDates = value

    def onCalendarClicked(self) -> None:
        """
        Отправка выбранной даты и её статуса через сигнал

        :return: None
        """

        current_date = self.selectedDate()
        status = True if AvailableDate(current_date, True) in self.availableDates else False

        self.dateStatusChanged.emit(AvailableDate(current_date, status))

    def appendAvailableDate(self, date: QtCore.QDate) -> None:
        """
        Добавление разрешенной даты в список разрешенных дат

        :param date: выбранная дата
        :return: None
        """

        # if date < QtCore.QDate.currentDate():  # Если необходимо изменить статус предыдущей даты
        #     QtWidgets.QMessageBox.warning(self, "Внимание", "Дата не может быть меньше сегодняшней")
        #     self.onCalendarClicked()
        #     return
        self.__availableDates.append(AvailableDate(date, True))
        print(self.availableDates)
        self.onCalendarClicked()

    def removeAvailableDate(self, date: QtCore.QDate) -> None:
        try:
            # if date < QtCore.QDate.currentDate():  # Если необходимо изменить статус предыдущей даты
            #     QtWidgets.QMessageBox.warning(self, "Внимание", "Нельзя изменить прошедшую дату")
            #     self.onCalendarClicked()
            #     return
            self.__availableDates.remove(AvailableDate(date, True))
            self.onCalendarClicked()
            print(self.__availableDates)
        except ValueError:
            pass


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = ManagementCalendar()
    win.dateStatusChanged.connect(lambda x: print(x))
    win.show()

    app.exec()
