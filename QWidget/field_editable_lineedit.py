from PySide6 import QtWidgets, QtCore


class EditableField(QtWidgets.QWidget):
    edited = QtCore.Signal(str)

    def __init__(self, label: str, minimum_label_width: int, parent=None):
        super().__init__(parent)

        self.initUi(label, minimum_label_width)

        self.initSignals()

    def initUi(self, label, minimum_label_width) -> None:
        """
        Доинициализация Ui

        :return: None
        """

        layout = QtWidgets.QHBoxLayout()

        self.label = QtWidgets.QLabel(label)
        self.label.setMinimumWidth(minimum_label_width)

        self.lineEdit = QtWidgets.QLineEdit()
        self.lineEdit.setReadOnly(True)

        self.pushButtonEdit = QtWidgets.QPushButton()
        self.pushButtonEdit.setFixedSize(22, 22)

        layout.addWidget(self.label)
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.pushButtonEdit)

        layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout)

    def initSignals(self) -> None:
        """

        :return:
        """

        self.pushButtonEdit.clicked.connect(self.onPushButtonClicked)

    def onPushButtonClicked(self) -> None:
        """

        :return:
        """

        text, ok = QtWidgets.QInputDialog.getText(self, "Изменить", "Введите новое значение")

        if ok:
            self.lineEdit.setText(text)
            self.edited.emit(text)

    def clear(self):
        self.text = ''

    @property
    def text(self):
        return self.lineEdit.text()

    @text.setter
    def text(self, new_text):
        self.lineEdit.setText(new_text)

    @property
    def label_text(self):
        return self.label.text()

    @property
    def editable(self):
        return self.pushButtonEdit.isEnabled()

    @editable.setter
    def editable(self, status):
        self.pushButtonEdit.setEnabled(status)


def get_field_by_label(layout: QtWidgets.QLayout, label_text: str) -> EditableField:
    for i in range(layout.count()):
        field: EditableField = layout.itemAt(i).widget()
        if field.label_text == label_text:
            return field


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = EditableField('Name', 80)
    win.show()

    app.exec()
