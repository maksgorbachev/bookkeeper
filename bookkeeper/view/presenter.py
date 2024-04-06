from bookkeeper.models.expense import Expense
from bookkeeper.models.category import Category
from bookkeeper.repository.sqlite_repository import SQLiteRepository
from bookkeeper.repository.abstract_repository import AbstractRepository
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QWidget, QTreeWidgetItem

from bookkeeper.view.add_widget import AddWidget
from bookkeeper.view.budget_mainwindow import BudgetMainWindow
from bookkeeper.view.table_widget import TableWidget
from bookkeeper.view.category_widget import CategoryInspector


class Presenter:
    def __init__(self, db_file: str):
        self.expense_repo = SQLiteRepository[Expense](db_file, Expense)
        self.category_repo = SQLiteRepository[Category](db_file, Category)

        self.table_widget = TableWidget(self.category_repo, self.expense_repo)
        self.table_widget.update_table()

        self.add_widget = AddWidget(
            self.category_repo,
            self.expense_repo,
            self.open_category_inspector,
            self.add_new_expense,
        )
        self.category_inspector_closed()

        self.main_window = BudgetMainWindow(self.table_widget, self.add_widget)

        self.category_inspector = CategoryInspector(
            self.category_repo,
            self.category_inspector_closed,
        )

        self.main_window.show()

    def open_category_inspector(self):
        self.category_inspector.show_widget()

    def category_inspector_closed(self):
        self.add_widget.update_widget()

    def add_new_expense(self, expense: Expense):
        self.table_widget.update_table()
