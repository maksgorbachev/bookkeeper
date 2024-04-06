# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'category_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGroupBox,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_category_widget(object):
    def setupUi(self, category_widget):
        if not category_widget.objectName():
            category_widget.setObjectName(u"category_widget")
        category_widget.resize(420, 550)
        category_widget.setMinimumSize(QSize(420, 550))
        self.verticalLayout_2 = QVBoxLayout(category_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(category_widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.tree_category = QTreeWidget(self.frame)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.tree_category.setHeaderItem(__qtreewidgetitem)
        self.tree_category.setObjectName(u"tree_category")
        self.tree_category.setGeometry(QRect(0, 0, 401, 401))
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 400, 401, 131))
        self.lbl_name = QLabel(self.groupBox)
        self.lbl_name.setObjectName(u"lbl_name")
        self.lbl_name.setGeometry(QRect(10, 30, 180, 20))
        self.lbl_name.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbl_parent = QLabel(self.groupBox)
        self.lbl_parent.setObjectName(u"lbl_parent")
        self.lbl_parent.setGeometry(QRect(10, 60, 180, 20))
        self.lbl_parent.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.led_name = QLineEdit(self.groupBox)
        self.led_name.setObjectName(u"led_name")
        self.led_name.setGeometry(QRect(200, 30, 180, 20))
        self.cmb_category = QComboBox(self.groupBox)
        self.cmb_category.setObjectName(u"cmb_category")
        self.cmb_category.setGeometry(QRect(200, 60, 180, 20))
        self.pb_add_category = QPushButton(self.groupBox)
        self.pb_add_category.setObjectName(u"pb_add_category")
        self.pb_add_category.setGeometry(QRect(110, 90, 150, 40))

        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(category_widget)

        QMetaObject.connectSlotsByName(category_widget)
    # setupUi

    def retranslateUi(self, category_widget):
        category_widget.setWindowTitle(QCoreApplication.translate("category_widget", u"Category", None))
        self.groupBox.setTitle(QCoreApplication.translate("category_widget", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043d\u043e\u0432\u0443\u044e \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e", None))
        self.lbl_name.setText(QCoreApplication.translate("category_widget", u"\u0418\u043c\u044f \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438", None))
        self.lbl_parent.setText(QCoreApplication.translate("category_widget", u"\u0420\u043e\u0434\u0438\u0442\u0435\u043b\u044c\u0441\u043a\u0430\u044f \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.pb_add_category.setText(QCoreApplication.translate("category_widget", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e", None))
    # retranslateUi

