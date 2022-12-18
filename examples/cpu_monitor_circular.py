import psutil
from PySide6 import QtWidgets

from QLayout.flex import QFlexLayout
from QThread.system_monitor import SystemMonitor
from QWidget.circular_widget import QCircularWidget


class CPUMonitor(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initThreads()

    def initThreads(self) -> None:
        """
        Инициализация потоков

        :return: None
        """
        self.systemInfo = SystemMonitor()
        self.systemInfo.start()
        self.systemInfo.system_info.connect(self.updatePB)

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.resize(600, 430)

        self.layout = QFlexLayout()
        for cpu in range(psutil.cpu_count()):
            self.layout.addWidget(QCircularWidget())

        self.setLayout(self.layout)

        self.setStyleSheet("background-color: #282a36")

    def updatePB(self, cpu_percent_list: list) -> None:
        """
        Обновление всех виджетов новыми параметрами

        :param cpu_percent_list: список со значениями загруженности CPU
        :return: None
        """

        for cpu_count in range(self.layout.count()):
            cpu_widget = self.layout.itemAt(cpu_count).widget()
            cpu_widget.setProgressBarValue(cpu_percent_list[cpu_count])
            cpu_widget.setText(f"CPU #{cpu_count}\n{cpu_percent_list[cpu_count]} %")


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = CPUMonitor()
    window.show()

    app.exec()
