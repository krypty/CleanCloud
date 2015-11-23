# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.le_access_key_id = QtWidgets.QLineEdit(Dialog)
        self.le_access_key_id.setAutoFillBackground(True)
        self.le_access_key_id.setObjectName("le_access_key_id")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.le_access_key_id)
        self.le_secret_key_id = QtWidgets.QLineEdit(Dialog)
        self.le_secret_key_id.setAutoFillBackground(True)
        self.le_secret_key_id.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le_secret_key_id.setObjectName("le_secret_key_id")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.le_secret_key_id)
        self.cbx_region = QtWidgets.QComboBox(Dialog)
        self.cbx_region.setObjectName("cbx_region")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cbx_region)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btn_login = QtWidgets.QPushButton(Dialog)
        self.btn_login.setObjectName("btn_login")
        self.horizontalLayout.addWidget(self.btn_login)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "CleanCloud"))
        self.label.setText(_translate("Dialog", "Secret access key: "))
        self.label_2.setText(_translate("Dialog", "Access key id: "))
        self.label_3.setText(_translate("Dialog", "Region"))
        self.btn_login.setText(_translate("Dialog", "Login"))

