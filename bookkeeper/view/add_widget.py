from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QWidget, QTreeWidgetItem
from PySide6.QtUiTools import QUiLoader

from bookkeeper.models.expense import Expense
from bookkeeper.models.category import Category
from bookkeeper.repository.abstract_repository import AbstractRepository

from bookkeeper.view.ui.ui_add_widget import Ui_add_widget


class AddWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.ui = Ui_add_widget()
        self.ui.setupUi(self)
        self.setParent(parent)
