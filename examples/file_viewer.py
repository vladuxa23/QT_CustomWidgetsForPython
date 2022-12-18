from PySide6 import QtCore, QtWidgets

from QWidget.dropped_file_area_simple import DroppedFileArea
from QWidget.filename_choose import QFolderChooseWidget


class FileHandler(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initModels()
        self.initUi()
        self.initSignals()

    # inits ------------------------------------------------------------------------------------------------------------
    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.setGeometry(500, 100, 500, 400)
        self.setAcceptDrops(True)

        # создаём Ui
        self.folder_widget = QFolderChooseWidget()
        self.list_files = DroppedFileArea()

        self.tree = QtWidgets.QTreeView()
        self.tree.setSelectionMode(QtWidgets.QTreeView.SingleSelection)
        self.tree.setDragDropMode(QtWidgets.QTreeView.InternalMove)
        self.tree.setModel(self.file_model)
        self.tree.setRootIndex(self.file_model.index(QtCore.QDir.currentPath()))

        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addWidget(self.folder_widget)
        main_layout.addWidget(self.tree)
        main_layout.addWidget(self.list_files)

        self.setLayout(main_layout)

    def initModels(self) -> None:
        """
        Инициализация моделей

        :return: None
        """

        self.file_model = QtWidgets.QFileSystemModel()
        self.file_model.setRootPath(QtCore.QDir.currentPath())

    def initSignals(self) -> None:
        """

        :return:
        """

        self.folder_widget.choosedFolder.connect(lambda path: self.tree.setRootIndex(self.file_model.index(path)))


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = FileHandler()
    win.show()

    app.exec()
