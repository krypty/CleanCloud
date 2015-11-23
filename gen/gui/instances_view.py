# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'instances_view.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(394, 331)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btn_refresh = QtWidgets.QPushButton(Form)
        self.btn_refresh.setObjectName("btn_refresh")
        self.horizontalLayout_2.addWidget(self.btn_refresh)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.lbl_title = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lbl_title.setFont(font)
        self.lbl_title.setObjectName("lbl_title")
        self.verticalLayout.addWidget(self.lbl_title)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.gbx_list = QtWidgets.QGroupBox(Form)
        self.gbx_list.setObjectName("gbx_list")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.gbx_list)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listWidget = QtWidgets.QListWidget(self.gbx_list)
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.gridLayout.addWidget(self.gbx_list, 0, 0, 1, 1)
        self.gbx_details = QtWidgets.QGroupBox(Form)
        self.gbx_details.setObjectName("gbx_details")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.gbx_details)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbl_details_data = QtWidgets.QLabel(self.gbx_details)
        self.lbl_details_data.setText("")
        self.lbl_details_data.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_details_data.setObjectName("lbl_details_data")
        self.verticalLayout_3.addWidget(self.lbl_details_data)
        self.gridLayout.addWidget(self.gbx_details, 0, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_select_all = QtWidgets.QPushButton(Form)
        self.btn_select_all.setObjectName("btn_select_all")
        self.horizontalLayout_3.addWidget(self.btn_select_all)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.btn_stop = QtWidgets.QPushButton(Form)
        self.btn_stop.setObjectName("btn_stop")
        self.horizontalLayout_3.addWidget(self.btn_stop)
        self.btn_delete = QtWidgets.QPushButton(Form)
        self.btn_delete.setObjectName("btn_delete")
        self.horizontalLayout_3.addWidget(self.btn_delete)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_refresh.setText(_translate("Form", "Refresh"))
        self.lbl_title.setText(_translate("Form", "Instances"))
        self.gbx_list.setTitle(_translate("Form", "Instances list"))
        self.gbx_details.setTitle(_translate("Form", "Details"))
        self.btn_select_all.setText(_translate("Form", "Select All"))
        self.btn_stop.setText(_translate("Form", "Stop"))
        self.btn_delete.setText(_translate("Form", "Delete"))

