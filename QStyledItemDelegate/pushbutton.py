from PySide6 import QtCore, QtWidgets, QtGui


class DelegatePushButtonOpenViewer(QtWidgets.QStyledItemDelegate):
    clicked = QtCore.Signal(QtCore.QModelIndex)

    def paint(self, painter: QtGui.QPainter, option: QtWidgets.QStyleOptionViewItem, index: QtCore.QModelIndex) -> None:
        """
        Отрисовка делегата

        :param painter: объект для рисования
        :param option: параметры отрисовки
        :param index: индекс элемента, для которого будет включаться делегат
        :return: None
        """

        if (isinstance(self.parent(), QtWidgets.QAbstractItemView)
                and self.parent().model() is index.model()):
            self.parent().openPersistentEditor(index)

    def createEditor(
            self,
            parent: QtWidgets.QWidget,
            option: QtWidgets.QStyleOptionViewItem,
            index: QtCore.QModelIndex
    ) -> QtWidgets.QWidget:
        """
        Создание редактора данных для делегата

        :param parent: родитель
        :param option: параметры отображения
        :param index: индекс элемента, для которого будет включаться делегат
        :return: виджет
        """

        button = QtWidgets.QPushButton(parent)
        button.clicked.connect(lambda *args, ix=index: self.clicked.emit(ix))

        return button

    def setEditorData(self, editor: QtWidgets.QWidget, index: QtCore.QModelIndex) -> None:
        """
        Установка исходных данных в кнопку

        :param editor: делегат
        :param index: индекс элемента, для которого будет включаться делегат
        :return: None
        """

        editor.setText("...")

    def setModelData(self, editor:QtWidgets.QWidget, model:QtCore.QAbstractItemModel, index:QtCore.QModelIndex) -> None:
        """
        Установка данных напрямую в модель

        :param editor: делегат
        :param model: модель с данными
        :param index: индекс элемента, для которого будет включаться делегат
        :return: None
        """

        pass
