from random import randint

from PySide6 import QtWidgets, QtCore, QtGui

from QLayout.flex import QFlexLayout


class QTagBar(QtWidgets.QScrollArea):
    adding = QtCore.Signal(str)
    deleting = QtCore.Signal(str)
    clicked = QtCore.Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.tags = []
        self.initUi()

    # inits ------------------------------------------------------------------------------------------------------------
    def initUi(self) -> None:
        """
        Доинициализация Ui

        :return: None
        """

        self.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.setContentsMargins(2, 2, 2, 2)

        self.comboBoxItems = QtWidgets.QComboBox()
        self.comboBoxItems.setObjectName("input_combobox")
        self.comboBoxItems.setEditable(True)
        self.comboBoxItems.installEventFilter(self)

        self.layoutTags = QFlexLayout()
        self.layoutTags.setSpacing(4)
        self.layoutTags.setContentsMargins(2, 2, 2, 2)

        layout_main = QtWidgets.QVBoxLayout()
        layout_main.addWidget(self.comboBoxItems)
        layout_main.addLayout(self.layoutTags)
        layout_main.addSpacerItem(
            QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        )

        c_w = QtWidgets.QWidget()
        c_w.setLayout(layout_main)

        self.setWidget(c_w)
        self.setWidgetResizable(True)

    # events -----------------------------------------------------------------------------------------------------------
    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:
        """
        Обработка доп. событий для конкретного виджета

        :param watched: QtCore.QObject
        :param event: QtCore.QEvent
        :return: True | False
        """

        if watched.objectName() == 'input_combobox' and event.type() == QtCore.QEvent.Type.KeyPress:
            if event.key() == 16777220:  # Нажатие на Enter
                self.__addNewItem()

        return super().eventFilter(watched, event)

    # private slots ----------------------------------------------------------------------------------------------------
    def __addNewItem(self) -> None:
        """
        Добавление тега в TagBar

        :param: название тега
        :return: None
        """

        new_tag = self.comboBoxItems.currentText()

        if new_tag not in self.tags and new_tag:
            tag = Tag(new_tag)
            tag.deleting.connect(self.deleteItem)
            tag.clicked.connect(lambda x: self.clicked.emit(x))

            self.layoutTags.addWidget(tag)
            self.tags.append(new_tag)

            self.adding.emit(self.comboBoxItems.currentText())
            self.comboBoxItems.setCurrentText("")

    # public slots -----------------------------------------------------------------------------------------------------
    def onTagClicked(self, tag_label: str) -> None:
        """
        Действие при нажатии на тэг

        :param tag_label: название тэга
        :return: None
        """

        self.clicked.emit(tag_label)

    def addItem(self, item_label) -> None:
        """
        Добавление тега не через lineEdit

        :param item_label: название тега
        :return: None
        """

        tag = Tag(item_label)
        tag.deleting.connect(self.deleteItem)
        tag.clicked.connect(self.onTagClicked)

        self.layoutTags.addWidget(tag)
        self.tags.append(item_label)

    def addItems(self, items: list) -> None:
        """
        Добавление списка тегов в TagBar

        :param items: список тегов
        :return: None
        """

        for item_label in items:
            self.addItem(item_label)

    def addPlaceholder(self, placeholder: str) -> None:
        """
        Добавляет элемент для быстрого выбора в comboBox

        :return: None
        """

        self.comboBoxItems.addItem(placeholder)

        if self.comboBoxItems.itemText(0) != "":
            self.comboBoxItems.insertItem(0, "")
            self.comboBoxItems.setCurrentIndex(0)

    def addPlaceholders(self, placeholders: list) -> None:
        """
        Добавляет элементы для быстрого выбора в comboBox

        :return: None
        """

        for placeholder in placeholders:
            self.addPlaceholder(placeholder)

        # скорее костыль чем нет
        if self.comboBoxItems.itemText(0) != "":
            self.comboBoxItems.insertItem(0, "")
            self.comboBoxItems.setCurrentIndex(0)

    def deleteItem(self, tag_label: str) -> None:
        """
        Удаление тега из TagBar

        :param tag_label: название тега
        :return: None
        """

        self.tags.remove(tag_label)
        self.deleting.emit(tag_label)

    def clear(self) -> None:
        """
        Очистка TagBar

        :return: None
        """

        for i in reversed(range(self.layoutTags.count())):
            self.layoutTags.itemAt(i).widget().setParent(None)

        self.tags.clear()
        self.comboBoxItems.clear()


class Tag(QtWidgets.QFrame):
    deleting = QtCore.Signal(str)
    clicked = QtCore.Signal(str)

    def __init__(self, tag_label, parent=None):
        super().__init__(parent)

        self.tag_label = tag_label

        self.initUi()
        self.initColor()

    def initUi(self) -> None:
        """
        Доинициализация Ui

        :return: None
        """

        self.setObjectName(self.tag_label)

        self.setContentsMargins(2, 2, 2, 2)
        self.setFixedHeight(28)
        self.setSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)

        self.pushButtonDelete = QtWidgets.QPushButton('x')
        self.pushButtonDelete.setFixedSize(9, 9)
        self.pushButtonDelete.setStyleSheet('border:1px; font-weight:bold')
        self.pushButtonDelete.setSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        self.pushButtonDelete.clicked.connect(self.onPushButtonDeleteClicked)

        label = QtWidgets.QLabel(self.tag_label)
        label.setStyleSheet('border:0px')
        label.setFixedHeight(16)

        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(label)
        hbox.addWidget(self.pushButtonDelete)
        hbox.setContentsMargins(4, 4, 4, 4)
        hbox.setSpacing(10)
        self.setLayout(hbox)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        """
        Переопределение метода для обработки щелчка мышью

        :param event: QtGui.QMouseEvent
        :return: None
        """

        self.clicked.emit(self.tag_label)

    def initColor(self) -> None:
        """
        Раскраска виджета в зависимости от содержимого

        :return: None
        """

        self.setStyleSheet(
            f"border: 1px solid rgb({randint(0, 255)}, {randint(0, 255)}, {randint(0, 255)}); "
            f"border-radius: 4px; "
            f"background-color: rgb({randint(0, 255)}, {randint(0, 255)}, {randint(0, 255)});")

    def onPushButtonDeleteClicked(self) -> None:
        """
        Удаление тега

        :return: None
        """

        self.deleting.emit(self.tag_label)
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = QTagBar()
    win.adding.connect(lambda x: print(x))
    win.clicked.connect(lambda x: print(x))
    win.deleting.connect(lambda x: print(x))
    win.addItems(["1234", "4321"])
    win.addItem("43210")
    win.show()

    app.exec()
