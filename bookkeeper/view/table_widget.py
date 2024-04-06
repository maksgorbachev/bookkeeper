from PySide6.QtWidgets import QWidget, QTableWidgetItem

from bookkeeper.view.ui.ui_table_widget import Ui_WidgetTable
from bookkeeper.models.expense import Expense


class TableWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_WidgetTable()
        self.ui.setupUi(self)

        self.ui.table_widget.setColumnWidth(0, 150)
        self.ui.table_widget.setColumnWidth(1, 80)
        self.ui.table_widget.setColumnWidth(2, 120)
        self.ui.table_widget.setColumnWidth(3, 318)

    def fill_table(self, expenses: list[Expense]):
        while self.ui.table_widget.rowCount() > 0:
            self.ui.table_widget.removeRow(0)
        for expense in expenses:
            self.add_expense(expense)

    def add_expense(self, expense: Expense):
        count_row = self.ui.table_widget.rowCount()
        self.ui.table_widget.insertRow(count_row)
        self.ui.table_widget.setItem(count_row, 0, QTableWidgetItem(str(expense.expense_date)))
        self.ui.table_widget.setItem(count_row, 1, QTableWidgetItem(str(expense.amount)))
        self.ui.table_widget.setItem(count_row, 2, QTableWidgetItem(str(expense.category)))
        self.ui.table_widget.setItem(count_row, 3, QTableWidgetItem(expense.comment))
