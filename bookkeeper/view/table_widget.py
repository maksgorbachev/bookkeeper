from PySide6.QtWidgets import QWidget

from bookkeeper.view.ui.ui_table_widget import Ui_WidgetTable


class TableWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.ui = Ui_WidgetTable()
        self.ui.setupUi(self)
        self.setParent(parent)

        self.ui.table_widget.setColumnWidth(0, 150)
        self.ui.table_widget.setColumnWidth(1, 80)
        self.ui.table_widget.setColumnWidth(2, 120)
        self.ui.table_widget.setColumnWidth(3, 318)
