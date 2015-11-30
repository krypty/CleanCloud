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
        MainWindow.resize(1240, 713)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gl_blocks = QtWidgets.QGridLayout()
        self.gl_blocks.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gl_blocks.setObjectName("gl_blocks")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gl_blocks.addLayout(self.verticalLayout_7, 1, 1, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gl_blocks.addLayout(self.verticalLayout_4, 0, 1, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gl_blocks.addLayout(self.verticalLayout_6, 1, 0, 1, 1)
        self.gl_blocks.setColumnStretch(0, 1)
        self.gl_blocks.setColumnStretch(1, 1)
        self.gl_blocks.setRowStretch(0, 1)
        self.gl_blocks.setRowStretch(1, 1)
        self.verticalLayout_2.addLayout(self.gl_blocks)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_refresh_all = QtWidgets.QPushButton(self.centralwidget)
        icon = QtGui.QIcon.fromTheme("view-refresh")
        self.btn_refresh_all.setIcon(icon)
        self.btn_refresh_all.setObjectName("btn_refresh_all")
        self.horizontalLayout.addWidget(self.btn_refresh_all)
        self.btn_delete_all = QtWidgets.QPushButton(self.centralwidget)
        icon = QtGui.QIcon.fromTheme("list-remove")
        self.btn_delete_all.setIcon(icon)
        self.btn_delete_all.setObjectName("btn_delete_all")
        self.horizontalLayout.addWidget(self.btn_delete_all)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_2.setStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1240, 26))
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
        self.btn_refresh_all.setText(_translate("MainWindow", "Refresh all"))
        self.btn_delete_all.setText(_translate("MainWindow", "Delete all"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.action_menu_quit.setText(_translate("MainWindow", "Quit"))
        self.action_menu_logout.setText(_translate("MainWindow", "Logout"))

