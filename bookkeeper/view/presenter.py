from bookkeeper.models.expense import Expense
from bookkeeper.models.category import Category
from bookkeeper.repository.sqlite_repository import SQLiteRepository

from bookkeeper.view import AddWidget, BudgetWidget, BudgetMainWindow, CategoryInspector, TableWidget


class Presenter:
    def __init__(self, db_file: str):
        self.expense_repo = SQLiteRepository[Expense](db_file, Expense)
        self.category_repo = SQLiteRepository[Category](db_file, Category)

        self.table_widget = TableWidget(self.category_repo, self.expense_repo)
        self.table_widget.update_table()

        self.budget = BudgetWidget(limit=1000, expenses=self.expense_repo)
        self.budget.update_widget()

        self.add_widget = AddWidget(
            self.category_repo,
            self.expense_repo,
            self.open_category_inspector,
            self.add_new_expense,
        )
        self.category_inspector_closed()

        self.main_window = BudgetMainWindow(self.table_widget, self.budget, self.add_widget)

        self.category_inspector = CategoryInspector(
            self.category_repo,
            self.category_inspector_closed,
        )

        self.main_window.show()

    def open_category_inspector(self):
        self.category_inspector.show_widget()

    def category_inspector_closed(self):
        self.add_widget.update_widget()

    def add_new_expense(self):
        self.table_widget.update_table()
        self.budget.update_widget()
