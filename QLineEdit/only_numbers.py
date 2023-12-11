from PySide6 import QtWidgets, QtCore, QtGui


class QLineEditOnlyNumbers(QtWidgets.QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

    # init -------------------------------------------------------------------------------------------------------------
    def initUi(self) -> None:
        """
        Доинициализация Ui

        :return: None
        """

        self.setAlignment(QtCore.Qt.AlignLeft)
        self.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Fixed,
        )

        self.setValidator(QtGui.QRegularExpressionValidator(QtCore.QRegularExpression("^([1-9][0-9]*|0)")))

if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = QLineEditOnlyNumbers()
    win.show()

    app.exec()
