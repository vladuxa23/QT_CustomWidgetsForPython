import os
import traceback

from PySide6 import QtCore, QtWidgets, QtWebEngineWidgets


class QPreviewWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.VIEWER_PDFJS = r"file:///exec/pdfjs/web/viewer.html"

    # init -------------------------------------------------------------------------------------------------------------
    def initUi(self) -> None:
        """
        Доинициализация Ui

        :return: None
        """

        try:
            # browser
            self.browser = QtWebEngineWidgets.QWebEngineView()  # Для PDF
            self.browser.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            self.browser.setHidden(True)

            # previewTextArea
            self.previewTextArea = QtWidgets.QTextBrowser()  # Для остальных файлов
            self.previewTextArea.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            self.previewTextArea.setFont('Consolas')

            # lineEdit
            self.lineEditPath = QtWidgets.QLineEdit()
            self.lineEditPath.setReadOnly(True)


            layout = QtWidgets.QVBoxLayout()
            layout.setContentsMargins(0, 0, 0, 0)
            layout.addWidget(self.lineEditPath)

            layout.addWidget(self.browser)
            layout.addWidget(self.previewTextArea)

            self.setLayout(layout)
        except Exception as err:
            pass

    # pushButton slots -------------------------------------------------------------------------------------------------


    # backend ----------------------------------------------------------------------------------------------------------
    def showPreview(self, file_path: str) -> None:
        """
        Управление предпросмотром

        :param file_path: Путь к файлу
        :return: None
        """

        ext_image = ["bmp", "gif", "jpeg", "jpg", "jfif", "png", "pbm", "pgm", "ppm", "xbm", "xpm"]
        ext_pdf = ["pdf"]
        ext_htm = ["html", "htm", "xml"]
        ext_doc = ["doc"]
        ext_docx = ["docx"]
        ext_cert = ["cer", "crl", "der", "p7b", "p7c", "p7m", "p7s", "stl"]

        ext = file_path.split(".")[-1]

        try:
            self.lineEditPath.setText(os.path.abspath(file_path))

            if ext in ext_image:
                img = "file:///" + file_path.replace("\\", "/")
                self.browser.load(QtCore.QUrl.fromUserInput(img))
                self.browser.setHidden(False)

            elif ext in ext_pdf:

                self.browser.setHidden(False)
                pdf = "file:///" + file_path.replace("\\", "/")
                load = "%s?file=%s" % (self.VIEWER_PDFJS, pdf)
                self.browser.load(QtCore.QUrl.fromUserInput(load))

            elif ext in ext_htm:
                self.browser.setHidden(False)
                url = QtCore.QUrl.fromLocalFile(os.path.abspath(file_path))
                self.browser.load(url)

            elif ext in ext_doc:
                self.previewTextArea.setHidden(False)
                self.previewTextArea.setText(doc_txt(file_path))

            elif ext in ext_docx:
                self.previewTextArea.setHidden(False)
                self.previewTextArea.setText(get_docx_data(file_path))

            elif ext in ext_cert:
                self.previewTextArea.setHidden(False)
                self.previewTextArea.setText(certificate.get_cert_info(file_path))

            else:
                if os.path.getsize(file_path) > (4096 * 1024):  # 4 Мб
                    self.browser.setHidden(True)
                    self.previewTextArea.setHidden(False)

                    self.previewTextArea.setText("Файл слишком большой для отображения."
                                                 "Используйте Viewer")
                    return

                self.browser.setHidden(True)
                self.previewTextArea.setHidden(False)
                self.previewTextArea.setText(sh.get_file_bytes(file_path, self.spinBoxFileSize.value()))

            self.previewTextArea.verticalScrollBar().setValue(0)

        except Exception as err:
            self.logger.exception(err)
            self.previewTextArea.append("Не удалось отобразить файл")
            self.previewTextArea.append(str(traceback.format_exc()))


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = QPreviewWidget()
    win.lineEditPath.setText(os.path.abspath(r""))
    win.show()

    app.exec()
