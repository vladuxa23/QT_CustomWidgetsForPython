import datetime

from PySide6 import QtWidgets, QtCore

from QWidget.patient_complaint import Complaints, ComplaintForm


class ComplaintsList(QtWidgets.QListWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

    def addComplaint(self, complaint: ComplaintForm) -> None:
        """
        Добавление формы жалобы в виде виджета на listWidget

        :param complaint: жалоба пациента (объект типа ComplaintForm)
        :return:
        """

        item = QtWidgets.QListWidgetItem()
        widget_size = complaint.sizeHint()
        item.setSizeHint(QtCore.QSize(widget_size.width(), widget_size.height() - 120))
        self.addItem(item)
        self.setItemWidget(item, complaint)


if __name__ == '__main__':
    def demo():
        app = QtWidgets.QApplication()

        window = ComplaintsList()
        window.addComplaint(ComplaintForm(Complaints(datetime.datetime.now(), ['Кашель', 'Чихание', 'Метеоризм', ])))
        window.addComplaint(ComplaintForm(Complaints(datetime.datetime.now(), ['Кашель', 'Чихание', 'Метеоризм', ])))
        window.addComplaint(ComplaintForm(Complaints(datetime.datetime.now(), ['Кашель', 'Чихание', 'Метеоризм', ])))
        window.addComplaint(ComplaintForm(Complaints(datetime.datetime.now(), ['Кашель', 'Чихание', 'Метеоризм', ])))
        window.addComplaint(ComplaintForm(Complaints(datetime.datetime.now(), ['Кашель', 'Чихание', 'Метеоризм', ])))
        window.addComplaint(ComplaintForm(Complaints(datetime.datetime.now(), ['Кашель', 'Чихание', 'Метеоризм', ])))
        window.show()

        app.exec()


    demo()
