from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import (
    QComboBox,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QListWidget,
    QFrame,
    QProgressBar,
    QLineEdit,
    QDialog,
    QToolBar,
    QStatusBar,
)
from PySide6.QtGui import QPixmap, QAction, QIcon

from app.cooker_backend import cooker_backend
import os

print(os.path.exists("resources/create_png.png"))
print("Current Working Directory:", os.getcwd())


class cooker_ui(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Personal Cooking Book")
        self.resize(1000, 1000)
        self.backend = cooker_backend(self)
        self.toolbar_creator()
        self.setStatusBar(QStatusBar(self))

    def toolbar_creator(self):
        toolbar = QToolBar("Cooker Toolbar")
        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        toolbar.setIconSize(QSize(46, 46))
        self.addToolBar(toolbar)

        create_button = QAction(
            QIcon("resources/create_png.png"), "Create new receipt", self
        )
        create_button.setStatusTip("This lets you create a new receipt!")
        create_button.triggered.connect(self.backend.create_new_receipt)

        toolbar.addAction(create_button)
