# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(1024, 600)
        widget.setMinimumSize(QtCore.QSize(1024, 500))
        widget.setMaximumSize(QtCore.QSize(1024, 768))
        self.label_camera = QtWidgets.QLabel(widget)
        self.label_camera.setEnabled(True)
        self.label_camera.setGeometry(QtCore.QRect(340, 60, 640, 480))
        self.label_camera.setMinimumSize(QtCore.QSize(640, 480))
        self.label_camera.setMaximumSize(QtCore.QSize(640, 480))
        self.label_camera.setText("")
        self.label_camera.setObjectName("label_camera")
        self.graphicsView = QtWidgets.QGraphicsView(widget)
        self.graphicsView.setGeometry(QtCore.QRect(340, 60, 640, 480))
        self.graphicsView.setMinimumSize(QtCore.QSize(640, 480))
        self.graphicsView.setMaximumSize(QtCore.QSize(640, 480))
        self.graphicsView.setObjectName("graphicsView")
        self.label_2 = QtWidgets.QLabel(widget)
        self.label_2.setGeometry(QtCore.QRect(640, 20, 91, 16))
        self.label_2.setObjectName("label_2")
        self.btn_new_face = QtWidgets.QPushButton(widget)
        self.btn_new_face.setGeometry(QtCore.QRect(130, 80, 80, 31))
        self.btn_new_face.setMaximumSize(QtCore.QSize(100, 100))
        self.btn_new_face.setObjectName("btn_new_face")
        self.label_info = QtWidgets.QLabel(widget)
        self.label_info.setGeometry(QtCore.QRect(30, 170, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_info.setFont(font)
        self.label_info.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_info.setObjectName("label_info")
        self.columnView = QtWidgets.QColumnView(widget)
        self.columnView.setGeometry(QtCore.QRect(20, 150, 301, 381))
        self.columnView.setObjectName("columnView")
        self.label_photo = QtWidgets.QLabel(widget)
        self.label_photo.setGeometry(QtCore.QRect(190, 210, 111, 131))
        self.label_photo.setText("")
        self.label_photo.setObjectName("label_photo")
        self.textEdit = QtWidgets.QTextEdit(widget)
        self.textEdit.setGeometry(QtCore.QRect(20, 210, 301, 321))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.reflash = QtWidgets.QPushButton(widget)
        self.reflash.setGeometry(QtCore.QRect(270, 120, 51, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.reflash.setFont(font)
        self.reflash.setObjectName("reflash")
        self.label_camera.raise_()
        self.graphicsView.raise_()
        self.label_2.raise_()
        self.btn_new_face.raise_()
        self.columnView.raise_()
        self.label_info.raise_()
        self.textEdit.raise_()
        self.label_photo.raise_()
        self.reflash.raise_()

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "FaceRecognition"))
        self.label_2.setText(_translate("widget", "摄像头采集信息"))
        self.btn_new_face.setText(_translate("widget", "新建人脸数据"))
        self.label_info.setText(_translate("widget", "员工信息"))
        self.reflash.setText(_translate("widget", "刷新"))
