import os

from PySide6 import QtGui, QtWidgets

from conf import ROOT_PATH

ICON_ADD = os.path.join(ROOT_PATH, 'QSS', 'icons', 'add.png')
ICON_DEL = os.path.join(ROOT_PATH, 'QSS', 'icons', 'minus.png')
ICON_NEXT = os.path.join(ROOT_PATH, 'QSS', 'icons', 'right-arrow.png')
ICON_PREV = os.path.join(ROOT_PATH, 'QSS', 'icons', 'back-arrow.png')
ICON_CLEAR = os.path.join(ROOT_PATH, 'QSS', 'icons', 'clear.png')


class QPushButtonAdd(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setIcon(QtGui.QIcon(ICON_ADD))
        self.setFixedSize(24, 24)


class QPushButtonDel(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setIcon(QtGui.QIcon(ICON_DEL))
        self.setFixedSize(24, 24)


class QPushButtonClear(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setIcon(QtGui.QIcon(ICON_CLEAR))
        self.setFixedSize(24, 24)


class QPushButtonNext(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setIcon(QtGui.QIcon(ICON_NEXT))
        self.setFixedSize(24, 24)


class QPushButtonPrev(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setIcon(QtGui.QIcon(ICON_PREV))
        self.setFixedSize(24, 24)


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    w = QPushButtonAdd()
    w.show()
    app.exec()
