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
from PySide6.QtWidgets import (QApplication, QDialog, QGraphicsView, QGridLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

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
        self.generate_button.setGeometry(QRect(760, 580, 81, 23))
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
        self.widget = QWidget(MainWindow)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(580, 0, 264, 115))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(100, 100))
        self.label_3.setPixmap(QPixmap(u"icons/ms-icon-70x70.png"))
        self.label_3.setScaledContents(True)

        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QSize(80, 80))
        self.label_2.setPixmap(QPixmap(u"icons/mc.webp"))
        self.label_2.setScaledContents(True)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(80, 80))
        self.label.setPixmap(QPixmap(u"icons/amulet.webp"))
        self.label.setScaledContents(True)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


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
        self.label_3.setText("")
        self.label_2.setText("")
        self.label.setText("")
    # retranslateUi

