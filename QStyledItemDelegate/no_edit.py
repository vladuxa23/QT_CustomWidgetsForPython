from PySide6 import QtWidgets, QtCore


class NoEditDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self):
        super(NoEditDelegate, self).__init__()

    def createEditor(
            self,
            parent: QtWidgets.QWidget,
            option: QtWidgets.QStyleOptionViewItem,
            index: QtCore.QModelIndex
    ) -> QtWidgets.QWidget:
        return 0
