from calendar import monthrange
from datetime import datetime, timedelta

from PySide6.QtWidgets import QTableWidgetItem, QWidget

from bookkeeper.models.expense import Expense
from bookkeeper.models.category import Category
from bookkeeper.repository.abstract_repository import AbstractRepository
from bookkeeper.models.expense import Expense

from bookkeeper.view.ui.ui_budget_widget import Ui_budget_widget


class BudgetWidget(QWidget):
    def __init__(
            self,
            limit: int,
            expenses: AbstractRepository[Expense],
    ):
        super().__init__()
        self._limit = limit
        self.expenses = expenses
        self.ui = Ui_budget_widget()
        self.ui.setupUi(self)

        self.ui.table_widget.setColumnWidth(0, 270)
        self.ui.table_widget.setColumnWidth(1, 270)

    def update_widget(self):
        current_date = datetime.now()
        count_day_of_month = monthrange(current_date.year, current_date.month)[1]
        all_expenses: list[Expense] = self.expenses.get_all()

        first = datetime(current_date.year, current_date.month, current_date.day, 0, 0, 0)
        last = first + timedelta(days=1)
        summa = sum([
            expense.amount for expense in all_expenses if first <= datetime.fromisoformat(expense.expense_date) <= last
        ])
        self.ui.table_widget.setItem(0, 0, QTableWidgetItem(str(summa)))
        self.ui.table_widget.setItem(0, 1, QTableWidgetItem(str(self._limit)))

        first = first - timedelta(first.weekday())
        last = first + timedelta(days=7)
        summa = sum([
            expense.amount for expense in all_expenses if first <= datetime.fromisoformat(expense.expense_date) <= last
        ])
        self.ui.table_widget.setItem(1, 0, QTableWidgetItem(str(summa)))
        self.ui.table_widget.setItem(1, 1, QTableWidgetItem(str(self._limit * 7)))

        first = datetime(current_date.year, current_date.month, 1, 0, 0, 0)
        last = first + timedelta(days=count_day_of_month)
        summa = sum([
            expense.amount for expense in all_expenses if first <= datetime.fromisoformat(expense.expense_date) <= last
        ])
        self.ui.table_widget.setItem(2, 0, QTableWidgetItem(str(summa)))
        self.ui.table_widget.setItem(2, 1, QTableWidgetItem(str(self._limit * count_day_of_month)))
