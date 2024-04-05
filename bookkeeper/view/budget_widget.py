from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QWidget, QTreeWidgetItem
from PySide6.QtUiTools import QUiLoader

from bookkeeper.models.expense import Expense
from bookkeeper.models.category import Category
from bookkeeper.repository.abstract_repository import AbstractRepository

from bookkeeper.view.ui.ui_budget_widget import Ui_budget_widget


class BudgetWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.ui = Ui_budget_widget()
        self.ui.setupUi(self)
        self.setParent(parent)

        self.ui.table_widget.setColumnWidth(0, 300)
        self.ui.table_widget.setColumnWidth(1, 300)
