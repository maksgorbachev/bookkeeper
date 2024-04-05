from bookkeeper.models.expense import Expense
from bookkeeper.models.category import Category
from bookkeeper.repository.sqlite_repository import SQLiteRepository
from bookkeeper.repository.abstract_repository import AbstractRepository
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QWidget, QTreeWidgetItem

from bookkeeper.view.budget_mainwindow import BudgetMainWindow


class Presenter:
    def __init__(self, db_file: str):
        self.expense_repo = SQLiteRepository[Expense](db_file, Expense)
        self.category_repo = SQLiteRepository[Category](db_file, Category)
        self.main_window = BudgetMainWindow(self.expense_repo, self.category_repo)
        #self.category_inspector = CategoryInspector(self.category_repo)

        #self.main_window.ui.pushButton.clicked.connect(self.open_category_inspector)

        self.main_window.show()

    #def open_category_inspector(self):
        #self.category_inspector.show()
