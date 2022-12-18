import psutil
from PySide6 import QtWidgets

from QThread.system_monitor import SystemMonitor
from QWidget.system_info import SystemWidget


class CPUMonitor(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()
        self.initThreads()

    def initUI(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        layout = QtWidgets.QHBoxLayout()

        for _ in range(psutil.cpu_count()):
            layout.addWidget(SystemWidget(self))

        self.setLayout(layout)

    def initThreads(self) -> None:
        """
        Инициализация потоков

        :return: None
        """

        self.systemMonitor = SystemMonitor()
        self.systemMonitor.start()
        self.systemMonitor.system_info.connect(self.updateSystemWidget)

    def updateSystemWidget(self, cpu_percent_list: list) -> None:
        """
        Обновление параметров системных виджетов

        :param cpu_percent_list: список со значениями загрузки CPU
        :return: None
        """

        layout = self.layout()

        for cpu_count in range(layout.count()):
            widget_link = layout.itemAt(cpu_count).widget()

            widget_link.setValue(cpu_percent_list[cpu_count])
            widget_link.setText(f"CPU №{cpu_count + 1} - {cpu_percent_list[cpu_count]}")


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = CPUMonitor()
    win.show()

    app.exec()
