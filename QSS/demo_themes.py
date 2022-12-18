from PySide6.examples.widgets.widgetsgallery.widgetgallery import WidgetGallery
from PySide6 import QtCore, QtWidgets

from utils import load_style

if __name__ == '__main__':


    app = QtWidgets.QApplication()

    win = WidgetGallery()
    win.setStyleSheet(load_style("DarkStyle2Theme.qss"))
    # win.setStyleSheet(load_style("DarkStyleTheme.qss"))
    # win.setStyleSheet(load_style("MumbleDarkOSXTheme.qss"))
    # win.setStyleSheet(load_style("MumbleDarkTheme.qss"))
    # win.setStyleSheet(load_style("MumbleLiteOSXTheme.qss"))
    # win.setStyleSheet(load_style("MumbleLiteTheme.qss"))
    win.show()

    app.exec()