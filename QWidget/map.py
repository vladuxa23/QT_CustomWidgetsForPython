from PySide6 import QtWidgets, QtWebEngineWidgets, QtCore


class QMapWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)

        map_url = QtCore.QUrl(f"https://www.openstreetmap.org/#map=10/60.00/30.00")
        if map_url:
            self.map_view = QtWebEngineWidgets.QWebEngineView()
            self.map_view.setUrl(map_url)
        else:
            self.map_view = QtWidgets.QLabel()
            self.map_view.setText("Карта не подключена")
            self.map_view.setEnabled(False)
            self.map_view.setAlignment(QtCore.Qt.AlignCenter)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.map_view)

        self.setLayout(layout)


if __name__ == '__main__':
    def demo():

        app = QtWidgets.QApplication()

        window = QMapWidget()
        window.show()

        app.exec()

    demo()
