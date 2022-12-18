"""
Демонстрация использования QDroppedArea
"""
import time

from PySide6 import QtWidgets, QtCore, QtGui


class QDroppedArea(QtWidgets.QWidget):
    dropped = QtCore.Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.setFixedSize(300, 300)
        self.setAcceptDrops(True)  # устанавливаем возможность делать Drop на виджет

    def dragEnterEvent(self, event: QtGui.QDragEnterEvent) -> None:
        """
        Обработка перетаскивания

        :param event: QtGui.QDragEnterEvent
        :return: None
        """

        if event.mimeData().hasUrls():
            event.acceptProposedAction()  # разрешаем перетаскивание, если url

    def dropEvent(self, event: QtGui.QDropEvent) -> None:
        """
        Обработка завершения перетаскивания

        :param event: QtGui.QDropEvent
        :return: None
        """

        # Здесь можно настроить перетаскивание для обработки любых объектов

        for url in event.mimeData().urls():
            file_name = url.toLocalFile()
            self.dropped.emit("Dropped file: " + file_name)


if __name__ == "__main__":
    def demo() -> None:
        app = QtWidgets.QApplication()

        window = QDroppedArea()
        window.dropped.connect(lambda data: print(time.ctime(), data))
        window.show()

        app.exec()

    demo()