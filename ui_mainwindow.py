# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(209, 362)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_20 = QLabel(self.groupBox)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout.addWidget(self.label_20, 0, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 0, 1, 1, 2)

        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 1, 0, 1, 2)

        self.spinBox_13 = QSpinBox(self.groupBox)
        self.spinBox_13.setObjectName(u"spinBox_13")
        self.spinBox_13.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_13, 1, 2, 1, 1)

        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 2, 0, 1, 2)

        self.spinBox_16 = QSpinBox(self.groupBox)
        self.spinBox_16.setObjectName(u"spinBox_16")
        self.spinBox_16.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_16, 2, 2, 1, 1)

        self.label_18 = QLabel(self.groupBox)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout.addWidget(self.label_18, 3, 0, 1, 2)

        self.spinBox_15 = QSpinBox(self.groupBox)
        self.spinBox_15.setObjectName(u"spinBox_15")
        self.spinBox_15.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_15, 3, 2, 1, 1)

        self.label_16 = QLabel(self.groupBox)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 4, 0, 1, 2)

        self.spinBox_11 = QSpinBox(self.groupBox)
        self.spinBox_11.setObjectName(u"spinBox_11")
        self.spinBox_11.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_11, 4, 2, 1, 1)

        self.label_15 = QLabel(self.groupBox)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 5, 0, 1, 2)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 5, 2, 1, 1)

        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 6, 0, 1, 2)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 7, 1, 1, 1)

        self.label_17 = QLabel(self.groupBox)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 8, 1, 1, 1)

        self.spinBox_10 = QSpinBox(self.groupBox)
        self.spinBox_10.setObjectName(u"spinBox_10")
        self.spinBox_10.setMaximum(255)

        self.gridLayout.addWidget(self.spinBox_10, 8, 2, 1, 1)

        self.label_19 = QLabel(self.groupBox)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout.addWidget(self.label_19, 9, 1, 1, 1)

        self.spinBox_14 = QSpinBox(self.groupBox)
        self.spinBox_14.setObjectName(u"spinBox_14")
        self.spinBox_14.setMaximum(255)

        self.gridLayout.addWidget(self.spinBox_14, 9, 2, 1, 1)

        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 10, 1, 1, 2)

        self.spinBox_9 = QSpinBox(self.groupBox)
        self.spinBox_9.setObjectName(u"spinBox_9")
        self.spinBox_9.setMaximum(255)

        self.gridLayout.addWidget(self.spinBox_9, 7, 2, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 209, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Capturador de part\u00edculas", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Part\u00edculas", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Origen en x:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Origen en y:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Destino en x:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Destino en y:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Color (rgb):", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
    # retranslateUi

