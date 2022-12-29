"""
Виджет для работы с файлами с помощью drag & drop и контекстного меню
"""

import os
from uuid import uuid4

from PySide6 import QtWidgets, QtCore, QtGui


class QDroppedFileArea(QtWidgets.QWidget):
    adding = QtCore.Signal(str)
    clicked = QtCore.Signal(str)
    deleting = QtCore.Signal(str)
    renaming = QtCore.Signal(tuple)
    downloading = QtCore.Signal(tuple)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initContextMenu()
        self.initSignals()

    # inits ------------------------------------------------------------------------------------------------------------
    def initUi(self) -> None:
        """
        Доинициализация Ui

        :return: None
        """

        self.setAcceptDrops(True)

        self.listWidgetFiles = QtWidgets.QListWidget()
        self.listWidgetFiles.setAcceptDrops(True)
        self.listWidgetFiles.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)

        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addWidget(self.listWidgetFiles)
        main_layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(main_layout)

    def initContextMenu(self) -> None:
        """
        Инициализация контекстного меню

        :return:
        """

        action_rename = QtGui.QAction("Переименовать файл", self)
        action_rename.triggered.connect(self.actionRenameTriggered)

        action_download = QtGui.QAction("Скачать файл", self)
        action_download.triggered.connect(self.actionDownloadTriggered)

        action_delete = QtGui.QAction("Удалить файл", self)
        action_delete.triggered.connect(self.actionDeleteTriggered)

        self.context_menu = QtWidgets.QMenu(self)
        self.context_menu.addAction(action_rename)
        self.context_menu.addAction(action_download)
        self.context_menu.addSeparator()
        self.context_menu.addAction(action_delete)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.listWidgetFiles.customContextMenuRequested.connect(self.showContextMenu)
        self.listWidgetFiles.clicked.connect(lambda: self.clicked.emit(self.listWidgetFiles.currentItem().data(0)))

    def showContextMenu(self, point: QtCore.QPoint) -> None:
        """
        Отображение контекстного меню

        :param point: QtCore.QPoint
        :return: None
        """

        self.context_menu.exec(self.mapToGlobal(point))

    # events -----------------------------------------------------------------------------------------------------------
    def dragEnterEvent(self, event: QtGui.QDragEnterEvent) -> None:
        """
        Обработка перетаскивания

        :param event: QtGui.QDragEnterEvent
        :return: None
        """

        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QtGui.QDropEvent) -> None:
        """
        Обработка завершения перетаскивания

        :param event: QtGui.QDropEvent
        :return: None
        """

        for url in event.mimeData().urls():
            path = url.toLocalFile()
            path = os.path.normpath(path)
            if os.path.isfile(path):
                if self.listWidgetFiles.findItems(os.path.basename(path), QtCore.Qt.MatchFlag.MatchFixedString):
                    QtWidgets.QMessageBox.warning(
                        self, "Ошибка!",
                        "Файл с таким названием уже присвоен к организации \n"
                        "Переименнуйте загружаемый файл, либо уже загруженный."
                    )
                    return None
                self.addItem(path)
                self.adding.emit(path)

            if os.path.isdir(path):
                QtWidgets.QMessageBox.about(
                    self, "Ошибка", "Невозможно загрузить папку.\nВы можете загрузить сразу несколько файлов из папки"
                )

    # slots ------------------------------------------------------------------------------------------------------------
    def addItem(self, file_path: str) -> None:
        """
        Добавление файла в виджет

        :param file_path: путь к файлу
        :return: None
        """

        file_name = os.path.basename(file_path)
        self.listWidgetFiles.addItem(file_name)

    def addItems(self, file_pathes: list) -> None:
        """
        Добавление списка файлов в виджет

        :param file_pathes: список путей к файлам
        :return: None
        """

        for file_path in file_pathes:
            self.addItem(file_path)

    def actionRenameTriggered(self) -> None:
        """
        Функция переименования файла в listWidget

        :return: None
        """

        if not self.check_selected():
            return

        selected_file = self.listWidgetFiles.currentItem().data(0)

        new_file_name, ok = QtWidgets.QInputDialog.getText(
            self, "Переименнование",
            f"Для переименования {selected_file}\nвведите новое имя файла")

        if not ok:
            return

        self.listWidgetFiles.currentItem().setText(new_file_name)
        self.renaming.emit((selected_file, new_file_name))

    def actionDownloadTriggered(self) -> None:
        """
        Получение имени скачиваемого файла

        :return: None
        """

        if not self.check_selected():
            return

        selected_file = self.listWidgetFiles.currentItem().data(0)

        folder = os.path.normpath(QtWidgets.QFileDialog.getExistingDirectory(self, "Выбор папки"))

        orig_path = os.path.join(folder, selected_file)
        new_path = None  # для корректного скачивания

        if os.path.exists(orig_path):
            # На случай если такой файл в папке есть
            new_path = os.path.join(folder, f"{str(uuid4())}_{selected_file}")

        self.downloading.emit((orig_path, new_path))

    def actionDeleteTriggered(self) -> None:
        """
        Удаление файла из виджета

        :return: None
        """

        if not self.check_selected():
            return

        selected_file = self.listWidgetFiles.currentItem().data(0)

        answer = QtWidgets.QMessageBox.question(
            self, "Удаление",
            f"Вы действительно хотите удалить:\n{selected_file}")

        if answer == QtWidgets.QMessageBox.No:
            return

        self.listWidgetFiles.takeItem(self.listWidgetFiles.row(self.listWidgetFiles.currentItem()))
        self.deleting.emit(selected_file)

    # backend ----------------------------------------------------------------------------------------------------------
    def check_selected(self) -> bool:
        """
        Проверка выделен ли хоть один элемент

        :return: название элемента | None
        """

        selected_file = self.listWidgetFiles.currentItem()

        if selected_file is None:
            QtWidgets.QMessageBox.warning(self, "Ошибка", " Ни один файл не выбран")
            return False
        return True


if __name__ == '__main__':
    def demo() -> None:
        """
        Запуск демо использования виджета

        :return: None
        """

        import time

        app = QtWidgets.QApplication()

        win = QDroppedFileArea()
        # win.addItem("1234")
        # win.addItems(['123', '321'])
        win.adding.connect(lambda x: print(time.ctime(), x))
        win.renaming.connect(lambda x: print(time.ctime(), x))
        win.downloading.connect(lambda x: print(time.ctime(), x))
        win.clicked.connect(lambda x: print(time.ctime(), x))
        win.deleting.connect(lambda x: print(time.ctime(), x))
        win.show()

        app.exec()


    demo()
