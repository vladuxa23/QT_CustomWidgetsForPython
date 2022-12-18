from PySide6 import QtWidgets, QtGui


class CustomMovieSplashScreen(QtWidgets.QSplashScreen):
    def __init__(self, pathToGif):

        self.movie = QtGui.QMovie(pathToGif)
        self.movie.jumpToFrame(0)
        pixmap = QtGui.QPixmap(self.movie.frameRect().size())
        super(CustomMovieSplashScreen, self).__init__(pixmap)
        self.movie.frameChanged.connect(self.repaint)

    def showEvent(self, event):
        self.movie.start()

    def hideEvent(self, event: QtGui.QHideEvent) -> None:
        self.movie.stop()

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        painter = QtGui.QPainter(self)
        pixmap = self.movie.currentPixmap()
        self.setMask(pixmap.mask())
        painter.drawPixmap(0, 0, pixmap)
