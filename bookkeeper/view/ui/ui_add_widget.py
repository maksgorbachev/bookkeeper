# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QGroupBox,
    QLabel, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_add_widget(object):
    def setupUi(self, add_widget):
        if not add_widget.objectName():
            add_widget.setObjectName(u"add_widget")
        add_widget.resize(670, 140)
        add_widget.setMinimumSize(QSize(670, 140))
        add_widget.setMaximumSize(QSize(670, 140))
        self.group = QGroupBox(add_widget)
        self.group.setObjectName(u"group")
        self.group.setGeometry(QRect(0, 0, 670, 140))
        self.lbl_comment = QLabel(self.group)
        self.lbl_comment.setObjectName(u"lbl_comment")
        self.lbl_comment.setGeometry(QRect(260, 30, 100, 20))
        self.lbl_summa = QLabel(self.group)
        self.lbl_summa.setObjectName(u"lbl_summa")
        self.lbl_summa.setGeometry(QRect(10, 30, 80, 20))
        self.spb_summa = QDoubleSpinBox(self.group)
        self.spb_summa.setObjectName(u"spb_summa")
        self.spb_summa.setGeometry(QRect(90, 30, 80, 20))
        self.lbl_category = QLabel(self.group)
        self.lbl_category.setObjectName(u"lbl_category")
        self.lbl_category.setGeometry(QRect(10, 60, 80, 20))
        self.pb_add_item = QPushButton(self.group)
        self.pb_add_item.setObjectName(u"pb_add_item")
        self.pb_add_item.setGeometry(QRect(210, 100, 171, 31))
        self.txt_comment = QTextEdit(self.group)
        self.txt_comment.setObjectName(u"txt_comment")
        self.txt_comment.setGeometry(QRect(380, 30, 280, 50))
        self.cmb_category = QComboBox(self.group)
        self.cmb_category.setObjectName(u"cmb_category")
        self.cmb_category.setGeometry(QRect(90, 60, 80, 20))
        self.pb_add_category = QPushButton(self.group)
        self.pb_add_category.setObjectName(u"pb_add_category")
        self.pb_add_category.setGeometry(QRect(175, 60, 21, 21))

        self.retranslateUi(add_widget)

        QMetaObject.connectSlotsByName(add_widget)
    # setupUi

    def retranslateUi(self, add_widget):
        add_widget.setWindowTitle(QCoreApplication.translate("add_widget", u"Form", None))
        self.group.setTitle(QCoreApplication.translate("add_widget", u"\u0417\u0430\u043f\u0438\u0441\u044c", None))
        self.lbl_comment.setText(QCoreApplication.translate("add_widget", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439", None))
        self.lbl_summa.setText(QCoreApplication.translate("add_widget", u"\u0421\u0443\u043c\u043c\u0430: ", None))
        self.lbl_category.setText(QCoreApplication.translate("add_widget", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:", None))
        self.pb_add_item.setText(QCoreApplication.translate("add_widget", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.pb_add_category.setText("")
    # retranslateUi
