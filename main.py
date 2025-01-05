import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QStyleFactory
from PySide6.QtCore import Qt

# from app.style import stylesheet

from app.cooker_ui import cooker_ui


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Heic Converter")
        self.ui = cooker_ui()
        self.ui.setWindowFlags(
            Qt.Window | Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint
        )
        # self.ui.setStyleSheet(stylesheet)
        self.ui.show()


if __name__ == "__main__":
    app = QApplication()
    app.setStyle(QStyleFactory.create("Fusion"))
    widget = MainWindow()
    sys.exit(app.exec())
