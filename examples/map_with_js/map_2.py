import os
import sys
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget
from pyqtlet2 import L

from examples.map_with_js.map_widget import MapWidget



class MapWindow(QWidget):
    def __init__(self):
        # Setting up the widgets and layout
        super().__init__()

        self.mapWidget = MapWidget()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.mapWidget)
        self.setLayout(self.layout)

        # Working with the maps with pyqtlet
        self.map = L.map(self.mapWidget)
        self.map.setView([12.97, 77.59], 10)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MapWindow()
    sys.exit(app.exec_())