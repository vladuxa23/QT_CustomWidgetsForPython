import os

from PySide6 import QtCore

import filesystem


class FolderGetSize(QtCore.QThread):
    getSized = QtCore.Signal(dict)

    def __init__(self, ):
        super().__init__()

        self.__folder = None

    @property
    def folder(self):
        return self.__folder

    @folder.setter
    def folder(self, value: str):
        self.__folder = value

    def run(self):

        if self.folder and os.path.exists(self.folder):
            self.getSized.emit(filesystem.Folder.size(self.folder))
        else:
            pass