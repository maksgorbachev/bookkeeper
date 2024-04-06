from typing import Callable

from PySide6.QtWidgets import QWidget, QTreeWidgetItem

from bookkeeper.view.ui.ui_category_widget import Ui_category_widget
from bookkeeper.models.category import Category
from bookkeeper.repository.abstract_repository import AbstractRepository


class CategoryInspector(QWidget):
    def __init__(
            self,
            repo: AbstractRepository[Category],
            handler: Callable,
    ):
        super().__init__()
        self._repo_category = repo
        self._cache_category_id: dict[str, int] = {}
        self._handler = handler
        self.ui = Ui_category_widget()
        self.ui.setupUi(self)

        self.ui.pb_add_category.clicked.connect(self._handle_button_add)

        self._update_cache_categories()

    def _build_tree_category(self):
        self.ui.tree_category.clear()
        tree_widgets: list[QTreeWidgetItem] = []
        for _ in self._repo_category.get_all():
            tree_widgets.append(QTreeWidgetItem())
        for i, row in enumerate(self._repo_category.get_all()):
            tree_widgets[i].addChildren(
                [tree_widgets[cat.pk-1] for cat in row.get_subcategories(self._repo_category)])
            tree_widgets[i].setText(0, row.name)

        self.ui.tree_category.setColumnCount(1)
        self.ui.tree_category.addTopLevelItems(tree_widgets)

    def _update_cache_categories(self):
        categories: list[Category] = self._repo_category.get_all()
        self._cache_category_id = {
            category.name: category.pk for category in categories
        }
        self.ui.cmb_category.clear()
        self.ui.led_name.clear()
        self.ui.cmb_category.addItems(self._cache_category_id.keys())

    def show_widget(self):
        self._build_tree_category()

        self.ui.cmb_category.clear()
        self.ui.cmb_category.addItems(self._cache_category_id.keys())

        self.show()

    def _handle_button_add(self):
        name = self.ui.led_name.text()
        parent = self.ui.cmb_category.currentText()
        parent_id = self._cache_category_id.get(parent)

        category = Category(name=name, parent=parent_id)
        self._repo_category.add(category)

        self._update_cache_categories()
        self._build_tree_category()

    def closeEvent(self, unused_event):
        self._handler()
        self.close()
