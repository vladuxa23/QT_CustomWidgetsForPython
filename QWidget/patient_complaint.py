import datetime
from dataclasses import dataclass

from PySide6 import QtWidgets


@dataclass
class Complaints:
    date: datetime.datetime
    complaints: list


class ComplaintForm(QtWidgets.QWidget):

    def __init__(self, complaint=None, parent=None):
        super().__init__(parent)

        if complaint is None:
            complaint = Complaints(datetime.datetime.now(), [])
        self.complaint = complaint

        self.initUi()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.setMaximumHeight(200)

        self.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)

        self.date_time_edit_complaints = QtWidgets.QDateTimeEdit()
        self.date_time_edit_complaints.setDateTime(self.complaint.date)
        self.date_time_edit_complaints.setEnabled(False)

        self.list_widget_complaints = QtWidgets.QListWidget()
        for complaint in self.complaint.complaints:
            self.list_widget_complaints.addItem(QtWidgets.QListWidgetItem(complaint))

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.date_time_edit_complaints)
        layout.addWidget(self.list_widget_complaints)

        self.setLayout(layout)


if __name__ == '__main__':
    def demo():
        app = QtWidgets.QApplication()

        window = ComplaintForm(Complaints(datetime.datetime.now(), ['Кашель', 'Чихание', 'Метеоризм', ]))
        window.show()

        app.exec()


    demo()
