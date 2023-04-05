from PySide6 import QtWidgets, QtMultimedia, QtMultimediaWidgets, QtGui


class Camera(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self._capture_session = None
        self._camera = None
        self._camera_info = None
        self._image_capture = None

        self.initCamera()
        self.initUi()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self._camera_viewfinder = QtMultimediaWidgets.QVideoWidget()

        if self._camera and self._camera.error() == QtMultimedia.QCamera.NoError:
            name = self._camera_info.description()
            self.setWindowTitle(f"PySide6 Camera Example ({name})")

            self._capture_session.setVideoOutput(self._camera_viewfinder)
            self._camera.start()
        else:
            self.setWindowTitle("PySide6 Camera Example")
            self._take_picture_action.setEnabled(False)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self._camera_viewfinder)

        self.setLayout(layout)

    def initCamera(self) -> None:
        """
        Инициализация камеры

        :return: None
        """

        available_cameras = QtMultimedia.QMediaDevices.videoInputs()

        if available_cameras:
            self._camera_info = available_cameras[0]
            self._camera = QtMultimedia.QCamera(self._camera_info)
            self._image_capture = QtMultimedia.QImageCapture(self._camera)
            self._capture_session = QtMultimedia.QMediaCaptureSession()
            self._capture_session.setCamera(self._camera)
            self._capture_session.setImageCapture(self._image_capture)

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        if self._camera and self._camera.isActive():
            self._camera.stop()
        event.accept()


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    win = Camera()

    available_geometry = win.screen().availableGeometry()
    win.resize(available_geometry.width() / 3, available_geometry.height() / 2)

    win.show()
    app.exec()
