from PySide6 import QtWidgets, QtCore


class DelegateDoubleSpinBox(QtWidgets.QStyledItemDelegate):

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

        editor = QtWidgets.QDoubleSpinBox(parent, decimals=2)
        editor.setFrame(False)
        editor.setMinimum(-1.7976931348623157e308)
        editor.setMaximum(1.7976931348623157e308)
        editor.setButtonSymbols(2)
        editor.setSizePolicy(QtWidgets.QSizePolicy.Ignored, editor.sizePolicy().verticalPolicy())

        return editor
