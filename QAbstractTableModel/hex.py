from typing import Any

from PySide6 import QtCore, QtGui


class HexModel(QtCore.QAbstractTableModel):
    def __init__(self):
        super().__init__()

        self.byte_data = None

    # override backend -------------------------------------------------------------------------------------------------
    def columnCount(self, parent: QtCore.QModelIndex = None) -> int:
        """
        Метод возвращает количество столбцов модели

        :param parent: QtCore.QModelIndex
        :return: количество столбцов
        """

        try:
            return 8
        except Exception as err:
            self.logger.exception(err)

    def rowCount(self, parent: QtCore.QModelIndex = None) -> int:
        """
        Метод возвращает количество строк таблицы

        :param parent: QtCore.QModelIndex
        :return: количество строк
        """

        try:
            return len(self.byte_data) // 16 + 1
        except Exception as err:
            self.logger.exception(err)

    def data(self, index: QtCore.QModelIndex, role: int) -> Any:
        """
        Метод управления данными в модели

        :param index: QtCore.QModelIndex
        :param role: тип отображения данных
        :return: Any
        """

        try:
            if self.byte_data is None:
                return

            if role == QtCore.Qt.DisplayRole:
                try:
                    char = self.byte_data[index.row() * 16 + index.column()]
                    return '{:02X}'.format(char)
                except IndexError:
                    return None

            elif role == QtCore.Qt.EditRole:
                try:
                    return self.byte_data[index.row() * 16 + index.column()]
                except IndexError:
                    return None

            elif role == QtCore.Qt.TextAlignmentRole:
                return QtCore.Qt.AlignCenter

            elif role == QtCore.Qt.BackgroundRole:
                if index.column() % 2:
                    return QtGui.QColor(QtCore.Qt.lightGray)

        except Exception as err:
            self.logger.exception(err)
