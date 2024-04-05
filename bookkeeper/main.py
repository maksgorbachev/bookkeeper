import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QWidget

from bookkeeper.view.presenter import Presenter
from bookkeeper.view.table_widget import TableWidget
from bookkeeper.view.budget_widget import BudgetWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)

    presenter = Presenter('data/budget.db')
   
    sys.exit(app.exec())
