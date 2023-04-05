from PySide6 import QtWidgets, QtCore, QtGui


class LoadScreen(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(LoadScreen, self).__init__(parent)

        self.setFixedSize(200, 200)
        self.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint | QtCore.Qt.WindowType.CustomizeWindowHint)

        self.labelAnimation = QtWidgets.QLabel(self)

        self.movie = QtGui.QMovie("ui/loading_5.gif")

        self.labelAnimation.setMovie(self.movie)

        # timer = QtCore.QTimer(self)
        # self.startAnimation()
        # timer.singleShot(3000, self.stopAnimation)

    def startAnimation(self):
        self.movie.start()

    def stopAnimation(self):
        self.movie.stop()
        self.close()


class Demo(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.load_screen = LoadScreen(self)

        self.load_screen.startAnimation()



if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = Demo()
    win.show()

    app.exec()