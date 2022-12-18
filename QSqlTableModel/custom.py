from typing import Union

from PySide6 import QtCore, QtSql, QtGui


class EditableSQLModel(QtSql.QSqlTableModel):

    def __init__(self, parent=None):
        super().__init__(parent)

    def data(self, item, role):
        if role == QtCore.Qt.DisplayRole:
            if item.column() == 1:
                name = QtSql.QSqlTableModel.data(self, item, QtCore.Qt.DisplayRole)
                return name

        if role == QtCore.Qt.BackgroundRole:
            if item.row() % 2:
                return QtGui.QColor(QtCore.Qt.lightGray)

        return QtSql.QSqlTableModel.data(self, item, role)

    def flags(self, index: Union[QtCore.QModelIndex, QtCore.QPersistentModelIndex]) -> QtCore.Qt.ItemFlag:
        """
        Установка флагов для обработки данных

        :param index: индекс модели
        :return: QtCore.Qt.ItemFlag
        """

        if index.column() == 2:
            return QtCore.Qt.ItemIsEnabled
        else:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable
