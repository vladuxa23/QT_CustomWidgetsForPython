import requests
from PySide6 import QtCore


class ThreadApi(QtCore.QThread):
    recieved = QtCore.Signal(object)

    def __init__(self, parent=None):
        super(ThreadApi, self).__init__(parent)
        self.url = None

    def run(self):

        if self.url:
            responce = requests.get(self.url)
            if responce.status_code == 200:
                return responce.json()
        return None
