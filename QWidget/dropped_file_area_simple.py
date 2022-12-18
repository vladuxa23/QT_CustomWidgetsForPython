from PySide6 import QtWidgets, QtGui


class DroppedFileArea(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    # inits ------------------------------------------------------------------------------------------------------------
    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.setGeometry(500, 100, 500, 400)
        self.setAcceptDrops(True)

        # создаём Ui
        self.list_files = QtWidgets.QListWidget()
        self.label_total_files = QtWidgets.QLabel()

        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addWidget(QtWidgets.QLabel('Перетащите файл:'))
        main_layout.addWidget(self.list_files)
        main_layout.addWidget(self.label_total_files)

        self.setLayout(main_layout)

    def dragEnterEvent(self, event: QtGui.QDragEnterEvent) -> None:
        """
        Обработка события, когда мышь над виджетом, но кнопка ещё не отпущена

        :param event: QDragEnterEvent
        :return: None
        """

        # Тут выполняются проверки и дается (или нет) разрешение на Drop
        mime = event.mimeData()

        # Если перемещаются ссылки
        if mime.hasUrls():
            # Разрешаем действие перетаскивания
            event.acceptProposedAction()

    def dropEvent(self, event: QtGui.QDropEvent) -> None:
        """
        Обработка события drop
        :param event: QDropEvent
        :return: None
        """

        print(event.mimeData().urls())
        for url in event.mimeData().urls():
            file_name = url.toLocalFile()
            self.list_files.addItem(file_name)

        self.label_total_files.setText('Files: {}'.format(self.list_files.count()))


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    w = DroppedFileArea()
    w.show()

    app.exec()
