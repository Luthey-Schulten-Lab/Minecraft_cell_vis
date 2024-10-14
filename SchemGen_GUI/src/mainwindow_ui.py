# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QGraphicsView, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(872, 653)
        self.graphicsView = QGraphicsView(MainWindow)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(10, 30, 551, 581))
        self.add_button = QPushButton(MainWindow)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setGeometry(QRect(570, 550, 81, 23))
        self.generate_button = QPushButton(MainWindow)
        self.generate_button.setObjectName(u"generate_button")
        self.generate_button.setGeometry(QRect(750, 580, 81, 23))
        self.delete_all_button = QPushButton(MainWindow)
        self.delete_all_button.setObjectName(u"delete_all_button")
        self.delete_all_button.setGeometry(QRect(754, 550, 81, 23))
        self.delete_select_button = QPushButton(MainWindow)
        self.delete_select_button.setObjectName(u"delete_select_button")
        self.delete_select_button.setGeometry(QRect(660, 550, 91, 23))
        self.tableWidget = QTableWidget(MainWindow)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(580, 110, 256, 421))
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.preview_button = QPushButton(MainWindow)
        self.preview_button.setObjectName(u"preview_button")
        self.preview_button.setGeometry(QRect(570, 580, 81, 23))
        self.label = QLabel(MainWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(740, 30, 81, 71))
        self.label.setPixmap(QPixmap(u"icons/STC_logo.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(MainWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(660, 30, 81, 71))
        self.label_2.setPixmap(QPixmap(u"icons/display_yeast.gif"))
        self.label_2.setScaledContents(True)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Scheme Generator", None))
        self.add_button.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.generate_button.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.delete_all_button.setText(QCoreApplication.translate("MainWindow", u"Delete All", None))
        self.delete_select_button.setText(QCoreApplication.translate("MainWindow", u"Delete Select", None))
        self.preview_button.setText(QCoreApplication.translate("MainWindow", u"Preview", None))
        self.label.setText("")
        self.label_2.setText("")
    # retranslateUi

