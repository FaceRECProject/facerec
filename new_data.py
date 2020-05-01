# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_data.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class new_data(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(120, 250, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_name = QtWidgets.QLabel(Dialog)
        self.label_name.setGeometry(QtCore.QRect(80, 40, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_name.setFont(font)
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.label_sex = QtWidgets.QLabel(Dialog)
        self.label_sex.setGeometry(QtCore.QRect(80, 80, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_sex.setFont(font)
        self.label_sex.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sex.setObjectName("label_sex")
        self.label_num = QtWidgets.QLabel(Dialog)
        self.label_num.setGeometry(QtCore.QRect(80, 120, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_num.setFont(font)
        self.label_num.setAlignment(QtCore.Qt.AlignCenter)
        self.label_num.setObjectName("label_num")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(80, 160, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(130, 80, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox.setFont(font)
        self.comboBox.setEditable(False)
        self.comboBox.setCurrentText("")
        self.comboBox.setModelColumn(0)
        self.comboBox.setObjectName("comboBox")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(130, 40, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 120, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 160, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "新建信息"))
        self.label_name.setText(_translate("Dialog", "姓名："))
        self.label_sex.setText(_translate("Dialog", "性别："))
        self.label_num.setText(_translate("Dialog", "工号："))
        self.label_4.setText(_translate("Dialog", "部门："))
