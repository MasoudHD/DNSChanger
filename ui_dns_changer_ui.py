# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dns_changer_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(383, 212)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnApply = QPushButton(self.centralwidget)
        self.btnApply.setObjectName(u"btnApply")
        self.btnApply.setGeometry(QRect(260, 130, 93, 28))
        font = QFont()
        font.setPointSize(10)
        self.btnApply.setFont(font)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 50, 330, 63))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(100, 0))
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.etDNS11 = QLineEdit(self.widget)
        self.etDNS11.setObjectName(u"etDNS11")
        sizePolicy.setHeightForWidth(self.etDNS11.sizePolicy().hasHeightForWidth())
        self.etDNS11.setSizePolicy(sizePolicy)
        self.etDNS11.setMinimumSize(QSize(50, 0))
        self.etDNS11.setMaximumSize(QSize(50, 16777215))
        self.etDNS11.setFont(font)
        self.etDNS11.setMaxLength(3)

        self.gridLayout.addWidget(self.etDNS11, 0, 1, 1, 1)

        self.etDNS12 = QLineEdit(self.widget)
        self.etDNS12.setObjectName(u"etDNS12")
        sizePolicy.setHeightForWidth(self.etDNS12.sizePolicy().hasHeightForWidth())
        self.etDNS12.setSizePolicy(sizePolicy)
        self.etDNS12.setMinimumSize(QSize(50, 0))
        self.etDNS12.setMaximumSize(QSize(50, 16777215))
        self.etDNS12.setFont(font)
        self.etDNS12.setMaxLength(3)

        self.gridLayout.addWidget(self.etDNS12, 0, 2, 1, 1)

        self.etDNS13 = QLineEdit(self.widget)
        self.etDNS13.setObjectName(u"etDNS13")
        sizePolicy.setHeightForWidth(self.etDNS13.sizePolicy().hasHeightForWidth())
        self.etDNS13.setSizePolicy(sizePolicy)
        self.etDNS13.setMinimumSize(QSize(50, 0))
        self.etDNS13.setMaximumSize(QSize(50, 16777215))
        self.etDNS13.setFont(font)
        self.etDNS13.setMaxLength(3)

        self.gridLayout.addWidget(self.etDNS13, 0, 3, 1, 1)

        self.etDNS14 = QLineEdit(self.widget)
        self.etDNS14.setObjectName(u"etDNS14")
        sizePolicy.setHeightForWidth(self.etDNS14.sizePolicy().hasHeightForWidth())
        self.etDNS14.setSizePolicy(sizePolicy)
        self.etDNS14.setMinimumSize(QSize(50, 0))
        self.etDNS14.setMaximumSize(QSize(50, 16777215))
        self.etDNS14.setFont(font)
        self.etDNS14.setMaxLength(3)

        self.gridLayout.addWidget(self.etDNS14, 0, 4, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(100, 0))
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.etDNS21 = QLineEdit(self.widget)
        self.etDNS21.setObjectName(u"etDNS21")
        sizePolicy.setHeightForWidth(self.etDNS21.sizePolicy().hasHeightForWidth())
        self.etDNS21.setSizePolicy(sizePolicy)
        self.etDNS21.setMinimumSize(QSize(50, 0))
        self.etDNS21.setMaximumSize(QSize(50, 16777215))
        self.etDNS21.setFont(font)
        self.etDNS21.setMaxLength(3)

        self.gridLayout.addWidget(self.etDNS21, 1, 1, 1, 1)

        self.etDNS22 = QLineEdit(self.widget)
        self.etDNS22.setObjectName(u"etDNS22")
        sizePolicy.setHeightForWidth(self.etDNS22.sizePolicy().hasHeightForWidth())
        self.etDNS22.setSizePolicy(sizePolicy)
        self.etDNS22.setMinimumSize(QSize(50, 0))
        self.etDNS22.setMaximumSize(QSize(50, 16777215))
        self.etDNS22.setFont(font)
        self.etDNS22.setMaxLength(3)

        self.gridLayout.addWidget(self.etDNS22, 1, 2, 1, 1)

        self.etDNS23 = QLineEdit(self.widget)
        self.etDNS23.setObjectName(u"etDNS23")
        sizePolicy.setHeightForWidth(self.etDNS23.sizePolicy().hasHeightForWidth())
        self.etDNS23.setSizePolicy(sizePolicy)
        self.etDNS23.setMinimumSize(QSize(50, 0))
        self.etDNS23.setMaximumSize(QSize(50, 16777215))
        self.etDNS23.setFont(font)
        self.etDNS23.setMaxLength(3)

        self.gridLayout.addWidget(self.etDNS23, 1, 3, 1, 1)

        self.etDNS24 = QLineEdit(self.widget)
        self.etDNS24.setObjectName(u"etDNS24")
        sizePolicy.setHeightForWidth(self.etDNS24.sizePolicy().hasHeightForWidth())
        self.etDNS24.setSizePolicy(sizePolicy)
        self.etDNS24.setMinimumSize(QSize(50, 0))
        self.etDNS24.setMaximumSize(QSize(50, 16777215))
        self.etDNS24.setFont(font)
        self.etDNS24.setMaxLength(3)

        self.gridLayout.addWidget(self.etDNS24, 1, 4, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 383, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnApply.setText(QCoreApplication.translate("MainWindow", u"Disabled", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Primary DNS", None))
        self.etDNS11.setText("")
        self.etDNS12.setText("")
        self.etDNS13.setText("")
        self.etDNS14.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Secondary DNS", None))
        self.etDNS21.setText("")
        self.etDNS22.setText("")
        self.etDNS23.setText("")
        self.etDNS24.setText("")
    # retranslateUi

