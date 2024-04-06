from functools import cache

from PySide6.QtWidgets import QWidget, QTableWidgetItem

from bookkeeper.view.ui.ui_table_widget import Ui_WidgetTable
from bookkeeper.repository.abstract_repository import AbstractRepository
from bookkeeper.models.expense import Expense
from bookkeeper.models.category import Category


class TableWidget(QWidget):
    def __init__(
            self,
            categories: AbstractRepository[Category],
            expenses: AbstractRepository[Expense],
    ):
        super().__init__()
        self.ui = Ui_WidgetTable()
        self.ui.setupUi(self)
        self.categories = categories
        self.expenses = expenses

        self.ui.table_widget.setColumnWidth(0, 150)
        self.ui.table_widget.setColumnWidth(1, 80)
        self.ui.table_widget.setColumnWidth(2, 120)
        self.ui.table_widget.setColumnWidth(3, 315)

    def update_table(self):
        expenses = self.expenses.get_all()
        while self.ui.table_widget.rowCount() > 0:
            self.ui.table_widget.removeRow(0)
        for expense in expenses:
            self._add_expense(expense)

    @cache
    def _get_name_category_for_id(self, cat_id: int) -> str:
        category = self.categories.get(cat_id)
        return category.name

    def _add_expense(self, expense: Expense):
        count_row = self.ui.table_widget.rowCount()
        self.ui.table_widget.insertRow(count_row)
        self.ui.table_widget.setItem(count_row, 0, QTableWidgetItem(str(expense.expense_date)))
        self.ui.table_widget.setItem(count_row, 1, QTableWidgetItem(str(expense.amount)))
        self.ui.table_widget.setItem(count_row, 2, QTableWidgetItem(self._get_name_category_for_id(expense.category)))
        self.ui.table_widget.setItem(count_row, 3, QTableWidgetItem(expense.comment))
