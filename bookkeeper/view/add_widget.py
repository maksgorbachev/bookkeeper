from datetime import datetime
from typing import Callable

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QWidget, QTreeWidgetItem
from PySide6.QtUiTools import QUiLoader

from bookkeeper.models.expense import Expense
from bookkeeper.models.category import Category
from bookkeeper.repository.abstract_repository import AbstractRepository

from bookkeeper.view.ui.ui_add_widget import Ui_add_widget


class AddWidget(QWidget):
    def __init__(
            self,
            handler: Callable,
            handler_add_expense: Callable,
    ):
        super().__init__()
        self._cache_categories: dict[str, int] = {}
        self.ui = Ui_add_widget()
        self.ui.setupUi(self)
        self.ui.pb_add_category.clicked.connect(self._handler_button_category)
        self.ui.pb_add_item.clicked.connect(self._handler_button_add)

        self._open_button_category = handler
        self._handler_add_expense = handler_add_expense

    def _handler_button_category(self):
        self._open_button_category()

    def fill_combobox_categories(self, categories: dict[str, int]):
        self._cache_categories = categories
        self.ui.cmb_category.clear()
        self.ui.cmb_category.addItems(self._cache_categories.keys())

    def _handler_button_add(self):
        price: int = self.ui.spb_amount.value()

        expense = self.ui.dateTimeEdit.dateTime()
        category_name = self.ui.cmb_category.currentText()
        commentary = self.ui.txt_comment.toPlainText()

        expense = Expense(
            amount=price,
            category=self._cache_categories[category_name],
            expense_date=expense.toPython(),
            comment=commentary
        )

        self._handler_add_expense(expense)
