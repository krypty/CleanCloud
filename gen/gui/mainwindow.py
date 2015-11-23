# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridLayout.addLayout(self.verticalLayout_7, 1, 1, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 1, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout.addLayout(self.verticalLayout_6, 1, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_refresh = QtWidgets.QPushButton(self.centralwidget)
        self.btn_refresh.setObjectName("btn_refresh")
        self.horizontalLayout.addWidget(self.btn_refresh)
        self.btn_delete_all = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete_all.setObjectName("btn_delete_all")
        self.horizontalLayout.addWidget(self.btn_delete_all)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_menu_quit = QtWidgets.QAction(MainWindow)
        self.action_menu_quit.setObjectName("action_menu_quit")
        self.action_menu_logout = QtWidgets.QAction(MainWindow)
        self.action_menu_logout.setObjectName("action_menu_logout")
        self.menuFile.addAction(self.action_menu_logout)
        self.menuFile.addAction(self.action_menu_quit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CleanCloud"))
        self.btn_refresh.setText(_translate("MainWindow", "Refresh all"))
        self.btn_delete_all.setText(_translate("MainWindow", "Delete all"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.action_menu_quit.setText(_translate("MainWindow", "Quit"))
        self.action_menu_logout.setText(_translate("MainWindow", "Logout"))

