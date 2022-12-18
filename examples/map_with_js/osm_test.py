# На PySide6 пока не работает, в процессе отладки

import os
import re
import requests
from PySide6 import QtCore, QtWidgets, QtWebEngineWidgets, QtWebChannel

# https://www.youtube.com/watch?v=6c6KX0GjUI8&ab_channel=TKST1102 интересный пример использования карт
# https://leafletjs.com/index.html - сервис для работы со слоями карты (маркеры и прочее)
# https://www.mapbox.com/ - поставщик карт
# http://ip-api.com/ - инфо по IP - адресам


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initMap()

    def initUi(self):

        widgetLeftPanel = QtWidgets.QWidget()
        widgetRightPanel = QtWidgets.QWidget()
        splitterMain = QtWidgets.QSplitter(QtCore.Qt.Horizontal)

        layoutMain = QtWidgets.QHBoxLayout()
        layoutLeftPanel = QtWidgets.QVBoxLayout()
        layoutRightPanel = QtWidgets.QVBoxLayout()

        # widgetLeftPanel
        self.labelCoords = QtWidgets.QLabel()

        self.view = QtWebEngineWidgets.QWebEngineView()

        # widgetRightPanel
        labelCheckIP = QtWidgets.QLabel("Проверить IP")

        self.lineEditCheckIP = QtWidgets.QLineEdit()
        self.lineEditCheckIP.setPlaceholderText("Введите IP для проверки")

        self.pushButtonCheckIP = QtWidgets.QPushButton("Проверить")
        self.pushButtonCheckIP.clicked.connect(self.getIPInfo)

        layoutLeftPanel.addWidget(self.labelCoords)
        layoutLeftPanel.addWidget(self.view)

        layoutRightPanel.addWidget(labelCheckIP)
        layoutRightPanel.addWidget(self.lineEditCheckIP)
        layoutRightPanel.addWidget(self.pushButtonCheckIP)
        layoutRightPanel.addStretch(1)

        widgetLeftPanel.setLayout(layoutLeftPanel)
        widgetRightPanel.setLayout(layoutRightPanel)

        splitterMain.addWidget(widgetLeftPanel)
        splitterMain.addWidget(widgetRightPanel)

        layoutMain.addWidget(splitterMain)

        self.setLayout(layoutMain)

    def initMap(self):
        file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "map.html", )

        self.channel = QtWebChannel.QWebChannel()
        self.channel.registerObject("Window", self)

        self.view.page().setWebChannel(self.channel)
        self.view.setUrl(QtCore.QUrl.fromLocalFile(file))
        self.view.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

    @QtCore.Slot(float, float)
    def onMapMove(self, lat, lng):
        self.labelCoords.setText("Текущие координаты:\nДолгота: {:.5f}, Широта: {:.5f}".format(lng, lat))

    def getIPInfo(self):
        def getIPValidation(ip_):
            if len(ip) != 0:
                reg = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
                if re.match(reg, ip_) is None:
                    return False
                return True

        ip = self.lineEditCheckIP.text()

        if getIPValidation(ip) is False:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Введенные данные не являются IP - адресом")
            return

        response = requests.get(f"http://ip-api.com/json/{ip}")
        response = response.json()
        print(response)

        if response.get('status') != 'success':
            QtWidgets.QMessageBox.about(self, "Уведомление", "Информация по IP - адресу не найдена")
            return

        page = self.view.page()

        page.runJavaScript(f"map.setView([{response.get('lat')}, {response.get('lon')}], 16);")
        page.runJavaScript(f"L.marker([{response.get('lat')}, {response.get('lon')}]).addTo(map)"
                           f".bindPopup('<b>Провайдер:</b>{response.get('isp')}<br><b>Организация:</b> {response.get('org')}')"
                           f".openPopup();")
        circleOpt = "{color: 'blue', fillColor: '#B8E1E9', fillOpacity: 0.4, radius: 500}"
        page.runJavaScript("L.circle([{0}, {1}], {2}).addTo(map);"
                           .format(response.get('lat'), response.get('lon'), circleOpt))


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    w = Window()
    w.show()
    app.exec()
