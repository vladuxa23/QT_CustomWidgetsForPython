from PySide6 import QtWidgets, QtCore

from QThread.folder import FolderGetSize
from QWidget.field_ip import QLineEditField


class CheckFolderSizeWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(CheckFolderSizeWidget, self).__init__(parent)

        self.__initUi()

        self.__thread_check_folder_size = FolderGetSize()  # Подсчёт материала
        self.__thread_check_folder_size.getSized.connect(self.__threadCheckSendFolderSizeSlot)

        timer = QtCore.QTimer(self)
        timer.setInterval(3000)
        timer.timeout.connect(self.__timerCheckSendFolderSize)
        timer.start()

    def __initUi(self):
        self.__fieldSendingFolderSize = QLineEditField("Объем папки")
        self.__fieldSendingFolderSize.setReadOnly(True)
        self.__fieldSendingFolderCount = QLineEditField("Количество файлов")
        self.__fieldSendingFolderCount.setReadOnly(True)

        l = QtWidgets.QVBoxLayout()
        l.addWidget(self.__fieldSendingFolderSize)
        l.addWidget(self.__fieldSendingFolderCount)

        l.setContentsMargins(0, 0, 0, 0)

        self.setLayout(l)

    def __threadCheckSendFolderSizeSlot(self, result: dict) -> None:
        """
        Установка значений параметров полученных из потока

        :param result: Свойства папки (размер, кол-во файлов)
        :return: None
        """

        size, count = result.get('size'), result.get('count')
        self.__fieldSendingFolderSize.value = f"{str(round(size / 1024, 2))} Кб"
        self.__fieldSendingFolderCount.value = f"{str(count)} шт."

    def __timerCheckSendFolderSize(self) -> None:
        """
        Запуск потока проверки свойств папки

        :return: None
        """

        if not self.__thread_check_folder_size.isRunning():
            self.__thread_check_folder_size.start()

    def setPath(self, path):
        self.__fieldSendingFolderSize.value = "Идёт подсчёт..."
        self.__fieldSendingFolderCount.value = "Идёт подсчёт..."
        self.__thread_check_folder_size.folder = path

    def __initThread(self) -> None:
        """
        Инициализация потоков

        :return: None
        """


if __name__ == '__main__':

    app = QtWidgets.QApplication()

    win = CheckFolderSizeWidget()
    win.setPath(".")
    win.show()

    app.exec_()