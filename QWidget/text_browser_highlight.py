import re
import sys

from PySide6 import QtWidgets, QtCore, QtGui

from QSS.button import QPushButtonNext, QPushButtonPrev, QPushButtonClear


class Highlighter(QtGui.QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.__colors = self.__initColors()
        self.__mapping = {}

    @staticmethod
    def __initColors():
        colors = []
        for elem in QtCore.Qt.GlobalColor.__dict__:
            if not elem.startswith("__") and not elem.startswith("_"):
                if elem not in [
                    "name", "values", "color0", "color1", "transparent",
                    "white", "black", "gray", "lightGray", "darkGray"
                ]:
                    colors.append(getattr(QtCore.Qt.GlobalColor, elem))
        return colors

    def add_mapping(self, pattern):
        self.__mapping = {}
        patterns = pattern.split(";")

        if not patterns[0]:
            self.__mapping = {}
            return

        for index, elem in enumerate(patterns):
            try:
                color = self.__colors[index]
            except IndexError:
                i = len(patterns) // len(self.__colors)
                j = len(patterns) // i - len(self.__colors)
                color = self.__colors[j]

            fmt = QtGui.QTextCharFormat()
            fmt.setBackground(color)
            self.__mapping[elem.lower()] = fmt

    def highlightBlock(self, text_block):
        # print(self.__mapping)
        for pattern, fmt in self.__mapping.items():
            for match in re.finditer(pattern, text_block.lower()):
                start, end = match.span()
                self.setFormat(start, end - start, fmt)


class HighlightTextBrowser(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.__initUi()
        self.__initSignals()

    def __initUi(self):
        self.setWindowTitle("Поиск в браузере")

        self.__plainTextEdit = QtWidgets.QPlainTextEdit()
        self.__plainTextEdit.setStyleSheet("selection-background-color: cyan; selection-color: black; font-size: 15px")

        self.__highlighter = Highlighter(self.__plainTextEdit.document())

        self.__lineEditSearch = QtWidgets.QLineEdit()
        self.__lineEditSearch.setPlaceholderText("Шаблон для поиска (несколько значений можно ввести через ;)")

        self.__pushButtonNext = QPushButtonNext()
        self.__pushButtonPrev = QPushButtonPrev()
        self.__pushButtonClear = QPushButtonClear()

        lineWidget = QtWidgets.QWidget()
        lineWidget.setStyleSheet("background-color:black")
        lineWidget.setMinimumWidth(2)
        lineWidget.setMaximumWidth(2)

        l_menu = QtWidgets.QHBoxLayout()
        l_menu.addWidget(self.__lineEditSearch)
        l_menu.addWidget(self.__pushButtonPrev)
        l_menu.addWidget(self.__pushButtonNext)
        l_menu.addWidget(lineWidget)
        l_menu.addWidget(self.__pushButtonClear)

        l_main = QtWidgets.QVBoxLayout()
        l_main.addLayout(l_menu)

        l_main.addWidget(self.__plainTextEdit)

        l_main.setContentsMargins(0, 0, 0, 0)

        self.setLayout(l_main)

    def __initSignals(self):
        self.__pushButtonNext.clicked.connect(self.__find_next)
        self.__pushButtonPrev.clicked.connect(self.__find_prev)
        self.__pushButtonClear.clicked.connect(self.clear)

        self.__lineEditSearch.textChanged.connect(self.__search)

    def __search(self):
        text = self.__lineEditSearch.text()
        self.__highlighter.add_mapping(text)
        self.__highlighter.setDocument(self.__plainTextEdit.document())

    def __find_next(self):
        self.__plainTextEdit.find(self.__lineEditSearch.text())

    def __find_prev(self):
        self.__plainTextEdit.find(self.__lineEditSearch.text(), QtGui.QTextDocument.FindBackward)

    @property
    def text(self):
        return self.getText()

    @text.setter
    def text(self, value):
        self.setText(value)

    def appendText(self, text):
        self.__plainTextEdit.appendPlainText(text)
        self.__search()

    def setText(self, text):
        self.__plainTextEdit.setPlainText(text)
        self.__search()

    def getText(self):
        return self.__plainTextEdit.toPlainText()

    def clear(self):
        self.__plainTextEdit.clear()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = HighlightTextBrowser()
    window.text = '1, 2, 3, 4, 5, 6, 7 8 9 10 11 12 13 14 15'
    window.show()

    app.exec()
