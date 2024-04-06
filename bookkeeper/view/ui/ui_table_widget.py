# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'table_widget.ui'
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


class Ui_WidgetTable(object):
    def setupUi(self, WidgetTable):
        if not WidgetTable.objectName():
            WidgetTable.setObjectName(u"WidgetTable")
        WidgetTable.resize(670, 390)
        WidgetTable.setMinimumSize(QSize(670, 390))
        WidgetTable.setMaximumSize(QSize(670, 390))
        self.table_widget = QTableWidget(WidgetTable)
        if self.table_widget.columnCount() < 4:
            self.table_widget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.table_widget.setObjectName(u"table_widget")
        self.table_widget.setGeometry(QRect(0, 20, 670, 370))
        self.table_widget.setMinimumSize(QSize(670, 370))
        self.table_widget.setMaximumSize(QSize(1280, 620))
        self.lbl = QLabel(WidgetTable)
        self.lbl.setObjectName(u"lbl")
        self.lbl.setGeometry(QRect(0, 0, 201, 16))

        self.retranslateUi(WidgetTable)

        QMetaObject.connectSlotsByName(WidgetTable)
    # setupUi

    def retranslateUi(self, WidgetTable):
        WidgetTable.setWindowTitle(QCoreApplication.translate("WidgetTable", u"Form", None))
        ___qtablewidgetitem = self.table_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("WidgetTable", u"\u0414\u0430\u0442\u0430", None));
        ___qtablewidgetitem1 = self.table_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("WidgetTable", u"\u0421\u0443\u043c\u043c\u0430", None));
        ___qtablewidgetitem2 = self.table_widget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("WidgetTable", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None));
        ___qtablewidgetitem3 = self.table_widget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("WidgetTable", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439", None));
        self.lbl.setText(QCoreApplication.translate("WidgetTable", u"\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0435 \u0440\u0430\u0441\u0445\u043e\u0434\u044b", None))
    # retranslateUi

