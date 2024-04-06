# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'budget_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_budget_widget(object):
    def setupUi(self, budget_widget):
        if not budget_widget.objectName():
            budget_widget.setObjectName(u"budget_widget")
        budget_widget.resize(670, 140)
        budget_widget.setMinimumSize(QSize(670, 140))
        budget_widget.setMaximumSize(QSize(670, 140))
        self.lbl = QLabel(budget_widget)
        self.lbl.setObjectName(u"lbl")
        self.lbl.setGeometry(QRect(10, 0, 150, 20))
        self.table_widget = QTableWidget(budget_widget)
        if (self.table_widget.columnCount() < 2):
            self.table_widget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.table_widget.rowCount() < 3):
            self.table_widget.setRowCount(3)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_widget.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_widget.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_widget.setVerticalHeaderItem(2, __qtablewidgetitem4)
        self.table_widget.setObjectName(u"table_widget")
        self.table_widget.setGeometry(QRect(0, 20, 670, 115))
        self.table_widget.setMinimumSize(QSize(670, 115))
        self.table_widget.setMaximumSize(QSize(670, 115))

        self.retranslateUi(budget_widget)

        QMetaObject.connectSlotsByName(budget_widget)
    # setupUi

    def retranslateUi(self, budget_widget):
        budget_widget.setWindowTitle(QCoreApplication.translate("budget_widget", u"Form", None))
        self.lbl.setText(QCoreApplication.translate("budget_widget", u"\u0411\u044e\u0434\u0436\u0435\u0442", None))
        ___qtablewidgetitem = self.table_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("budget_widget", u"\u0421\u0443\u043c\u043c\u0430", None));
        ___qtablewidgetitem1 = self.table_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("budget_widget", u"\u0411\u044e\u0434\u0436\u0435\u0442", None));
        ___qtablewidgetitem2 = self.table_widget.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("budget_widget", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0439 \u0434\u0435\u043d\u044c", None));
        ___qtablewidgetitem3 = self.table_widget.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("budget_widget", u"\u0422\u0435\u043a\u0443\u0449\u0430\u044f \u043d\u0435\u0434\u0435\u043b\u044f", None));
        ___qtablewidgetitem4 = self.table_widget.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("budget_widget", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0439 \u043c\u0435\u0441\u044f\u0446", None));
    # retranslateUi

