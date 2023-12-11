from PySide6 import QtWidgets, QtCore

from QSS.button import QPushButtonAdd, QPushButtonDel


class QComboBoxEditable(QtWidgets.QWidget):
    textChanged = QtCore.Signal(str)
    dataChanged = QtCore.Signal(list)

    def __init__(self, label: str, items: list, parent=None):
        super(QComboBoxEditable, self).__init__(parent)

        self.initUi(label, items)

    def initUi(self, label, items):
        label = QtWidgets.QLabel(f"<b>{label}:</b>")
        comboBox = QtWidgets.QComboBox()
        comboBox.addItems(items if items else [])
        comboBox.currentTextChanged.connect(lambda x: self.textChanged.emit(x))
        pbAdd = QPushButtonAdd()
        pbAdd.setMaximumWidth(22)
        pbAdd.clicked.connect(self.onPBAddClicked)
        pbDel = QPushButtonDel()
        pbDel.setMaximumWidth(22)
        pbDel.clicked.connect(self.onPBDelClicked)

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(comboBox)
        layout.addWidget(pbAdd)
        layout.addWidget(pbDel)
        layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout)

    @property
    def value(self):
        return self.layout().itemAt(1).widget().currentText()

    @value.setter
    def value(self, data):
        w: QtWidgets.QComboBox = self.layout().itemAt(1).widget()
        w.setCurrentText(data)
        self.textChanged.emit(data)

    def onPBAddClicked(self):
        label = self.layout().itemAt(0).widget().text().strip("</b>:")
        comboBox = self.layout().itemAt(1).widget()

        text, ok = QtWidgets.QInputDialog.getText(
            self, f"Добавление параметра '{label}'", "Введите новое значение"
        )

        if not ok:
            return

        lst = [comboBox.itemText(i) for i in range(comboBox.count())]
        lst.append(text)
        lst.sort()

        comboBox.clear()
        comboBox.addItems(lst)
        self.dataChanged.emit(lst)

    def onPBDelClicked(self):
        label = self.layout().itemAt(0).widget().text().strip("</b>:")
        comboBox: QtWidgets.QComboBox = self.layout().itemAt(1).widget()

        answer = QtWidgets.QMessageBox.question(
            self, f"Удаление параметра '{label}'", "Вы действительно хотите удалить параметр?"
        )

        if answer != QtWidgets.QMessageBox.StandardButton.Yes:
            return

        comboBox.removeItem(comboBox.currentIndex())
        lst = [comboBox.itemText(i) for i in range(comboBox.count())]
        lst.sort()

        comboBox.clear()
        comboBox.addItems(lst)
        self.dataChanged.emit(lst)




if __name__ == '__main__':
    app = QtWidgets.QApplication()

    w = QComboBoxEditable("Test", ["s1", "s2", "s3"])
    w.dataChanged.connect(lambda x: print(x))
    w.textChanged.connect(lambda x: print(x))
    print(w.value)
    w.value = "s3"
    w.show()

    app.exec()