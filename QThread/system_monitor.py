from PySide6 import QtCore
import psutil
import time


class SystemMonitor(QtCore.QThread):
    system_info = QtCore.Signal(list)

    def run(self):
        while True:
            time.sleep(0.5)
            self.system_info.emit(psutil.cpu_percent(percpu=True))
