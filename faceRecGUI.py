#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2020/4/15
# @Author    :Beobachter

import sys
import shutil
import cv2
import os
import face_feature
import time
import dlib
import math
import random
import numpy as np
from datetime import *
from PyQt5 import QtWidgets, QtCore, QtGui
from main_window import Ui_widget
from new_data import new_data
import face_rec
import db


class FaceRec(QtWidgets.QWidget, Ui_widget):
    _signal = QtCore.pyqtSignal(int)
    def __init__(self):
        super(FaceRec, self).__init__()
        self.setupUi(self)
        self.timer_camera = QtCore.QTimer(self)  # 本地摄像头定时器
        self.CAM_NUM = 0  # 获取摄像头编号
        self.time = time  # 获取时间对象
        self.detector = dlib.get_frontal_face_detector()
        self.cap = cv2.VideoCapture(0)

        self.photo_path = 'photo/'
        self.tmp_path = 'tmp/'

        self.get_camera()
        self.show_camera()
        self.new = newdata()
        self.face_recognition()
        # time.sleep(10)
        # self.tmp()
        # self.ui_reflash()
        btn = self.btn_new_face
        btn.clicked.connect(self.newface)
        # self.savebtn.clicked.connect(self.newface)
        reflash = self.reflash
        reflash.clicked.connect(self.ui_reflash)
        self.check()
        self.timer_camera.timeout.connect(self.show_camera)  # 计时结束调用show_camera()方法

    def ui_reflash(self):
        self.face_recognition()

    def localtime(self):
        self.dt = datetime.now()
        self.t = self.dt.strftime('%Y-%m-%d %H:%M:%S')
        self.day = self.dt.strftime('%Y%m%d')
        self.date = self.dt.strftime('%x')
        # self.curr_time = self.dt.time()
        self.ym = self.dt.strftime('%Y%m')
        self.mon = self.dt.strftime('%m')
        self.defult_in = timedelta(hours=8)
        self.defult_out = timedelta(hours=17)
        self.defult_overtime = timedelta(hours=18)
        self.curr_time = timedelta(hours=self.dt.hour,minutes=self.dt.minute,seconds=self.dt.second)

    def get_camera(self):

        if not self.timer_camera.isActive():
            flag = self.cap.open(self.CAM_NUM)
            if not flag:
                QtWidgets.QMessageBox.warning(self, u"Warning", u"请检测相机与电脑是否连接正确", buttons=QtWidgets.QMessageBox.Ok,
                                                defaultButton=QtWidgets.QMessageBox.Ok)
            else:
                self.timer_camera.start(30)  # 30ms刷新一次
                # self.timer_rec.start(30)
        else:
            self.timer_camera.stop()    # 定时器关闭
            # self.timer_rec.stop()
            self.cap.release()          # 摄像头释放
            self.label_camera.clear()   # 视频显示区域清屏
            self.graphicsView.show()

    def show_camera(self):
        flag, self.image = self.cap.read()
        self.faces = self.detector(self.image, 0)
        self.save_flag = 0
        if len(self.faces) == 1:
            # 矩形框 / Show the rectangle box of face
            for k, d in enumerate(self.faces):
                # 计算矩形大小
                # 计算矩形框大小 / compute the size of rectangle box
                self.dd = d
                self.height = (d.bottom() - d.top())
                self.width = (d.right() - d.left())

                hh = int(self.height / 2)
                ww = int(self.width / 2)

                # 判断人脸矩形框是否超出 480x640
                if (d.right() + ww) > 640 or (d.bottom() + hh > 480) or (d.left() - ww < 0) or (d.top() - hh < 0):
                    cv2.putText(self.image, "OUT OF RANGE", (20, 300), cv2.FONT_ITALIC, 0.8, (0, 0, 255), 1,
                                cv2.LINE_AA)
                    color_rectangle = (0, 0, 255)
                else:
                    color_rectangle = (255, 255, 255)
                    self.curr_img = self.image
                    self.save_flag = 1
                    # self.face_recognition()

                cv2.rectangle(self.image,
                              tuple([d.left() - ww, d.top() - hh]),
                              tuple([d.right() + ww, d.bottom() + hh]),
                              color_rectangle, 2)

        elif len(self.faces)==0:
            self.textEdit.setText('\n\n\n\n          Unknow')
            # shutil.rmtree(self.tmp_path)
            # os.mkdir(self.tmp_path)
        else:
            cv2.putText(self.image, '请无关人员不要出现在镜头内！',(250,20),cv2.FONT_ITALIC, 0.8, (0, 255, 255), 1, cv2.LINE_AA)

        self.pic_show = cv2.resize(self.image, (640, 480))
        self.pic_show = cv2.cvtColor(self.pic_show, cv2.COLOR_BGR2RGB)
        showimage = QtGui.QImage(self.pic_show.data, self.pic_show.shape[1], self.pic_show.shape[0],
                                 QtGui.QImage.Format_RGB888)
        self.graphicsView.close()
        self.label_camera.setPixmap(QtGui.QPixmap.fromImage(showimage))
        # start = time.time()
        # self.face_recognition()
        # end = time.time()
        # print(end-start)

    def newface(self):
        QtWidgets.QMessageBox.information(self,'提示','请对准镜头保持1~2秒')
        time.sleep(1)
        if self.save_flag == 1:
            img_blank = np.zeros((int(self.height * 2), self.width * 2, 3), np.uint8)
            for i in range(self.height * 2):
                for j in range(self.width * 2):
                    img_blank[i][j] = self.image[self.dd.top() - int(self.height / 2) + i][self.dd.left() - int(self.width / 2) + j]
            cv2.imwrite( self.tmp_path+'tmp.jpg', img_blank)
            reply = QtWidgets.QMessageBox.information(self, '提示','保存成功！',QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
            if reply == QtWidgets.QMessageBox.Yes:
                self.new.show()
        else:
            QtWidgets.QMessageBox.information(self,'提示','请重新对准！')

    def face_features(self):
        features = db.get_features()
        id = []
        feature = []
        if features != 'error'and len(features) > 0:
            for val in features:
                id.append(val[0])
                n = [float(y) for y in (val[1].split(','))]
                feature.append(n)
        else:
            id.append(0)
            feature.append(0)
        return id,feature

    def check(self):
            if self.curr_time == timedelta(hours=16):
                id = db.fetch_id()
                for i in id:
                    id_att = db.get_his(i,self.date)
                    if id_att == []:
                        no = i + '-' + self.day
                        s_no = i + '-' + self.ym
                        db.save_att(no,i,self.dt,self.date,abs='1')
                        his = db.get_statistics(self.mon,i)
                        abs_times = his[1] + str(1)
                        db.statistics(i,s_no,self.mon,his[0],abs_times)
                        break


    def punch(self,id):
        re_in = self.curr_time <= self.defult_in
        re_out = self.curr_time >= self.defult_out
        re_over = self.defult_overtime < self.curr_time
        # index = random.randint(0,999999)
        no = id + '-' + self.day
        s_no = id + '-' + self.ym
        if re_in == True:
            # no = self.day + id
            db.save_att(no,id,self.dt,self.date)
        if re_in == False and re_out == False:
            # no = self.day + id
            late = str(math.ceil((self.curr_time-self.defult_in).seconds/3600))
            db.save_att(no,id,self.dt,self.date,latetime=late)
            val = db.get_statistics(self.mon,id)
            late_times = val[0] + str(1)
            db.statistics(id,s_no,self.mon,late_times,val[1])
        if re_out == True and re_over == False:
            db.save_att(no,id,self.dt,self.date)
        if re_over == True:
            over = int((self.curr_time-self.defult_overtime).seconds/3600)
            db.save_att(no,id,self.dt,self.date,overtime=str(over))


    def face_recognition(self):
        id, feature = self.face_features()
        # print(id,feature)
        if self.save_flag == 1 and id[0] != 0 and feature[0] != 0:
            similar_person_id = face_rec.Face_REC(self.image,self.faces[0],feature)
            if similar_person_id == 'unknow':
                self.textEdit.setText('\n\n\n\n          Unknow')
                self.label_photo.setPixmap(QtGui.QPixmap(''))
            else:
                try:
                    data = db.fetch_info(id[similar_person_id])
                    # count = db.get_count(id[similar_person_id])
                    statis = db.get_statistics(self.mon,id[similar_person_id])
                    print(data)
                    self.textEdit.setPlainText('\n\n  姓名：' + data[0][1] + '\n\n  性别：' + data[0][2] +
                                               '\n\n  工号：' + data[0][0] + '\n\n  部门：' + data[0][3] +
                                               '\n\n  本月迟到：'+statis[0]+'次'+'  缺勤：'+statis[1]+'次')
                    pix = QtGui.QPixmap(self.photo_path+data[0][4])
                    self.label_photo.setPixmap(pix)
                    self.label_photo.setScaledContents(True)
                    self.punch(id[similar_person_id])
                except:
                        self.textEdit.setText('\n\n\n\n          请补全人员信息！')

        else:
            self.textEdit.setText('\n\n\n\n          Unknow')
            self.label_photo.setPixmap(QtGui.QPixmap(''))






class newdata(QtWidgets.QDialog, new_data):
    _signal = QtCore.pyqtSignal(int)
    def __init__(self):
        super(newdata, self).__init__()
        self.setupUi(self)
        # self.user_path = 'data/user_data/user_info/'
        self.photo_path = 'photo/'
        self.tmp_path = 'tmp/'
        self.dt = datetime.now()
        self.ym = self.dt.strftime('%Y%m')
        self.mon = self.dt.strftime('%m')
        self.lineEdit.editingFinished.connect(self.getname)
        self.lineEdit_2.editingFinished.connect(self.getnum)
        self.lineEdit_3.editingFinished.connect(self.getdepart)
        sex = ['男', '女']
        self.comboBox.addItems(sex)
        self.comboBox.setCurrentText(sex[0])
        self.buttonBox.accepted.connect(self.log_show)
        self.buttonBox.rejected.connect(self.close)

    def getname(self):
        self.name = self.lineEdit.text()
        # print(self.name)


    def getnum(self):
        self.num = self.lineEdit_2.text()
        # print(self.num)


    def getdepart(self):
        self.depart = self.lineEdit_3.text()
        # print(self.depart)


    def log_show(self):
        self.sex = self.comboBox.currentText()
        user_data = {'name': self.name, 'sex': self.sex, 'number': self.num, 'department': self.depart}
        # status_1 = 'ok'
        status_1 = db.save_info(user_data,self.name+'.jpg')
        # print(status_1)
        if status_1 == 'ok':
            print('ready')
            feature = face_feature.return_features_mean_personX(self.tmp_path)
            print(feature)
            if feature == 0:
                self.info = QtWidgets.QMessageBox.information(self, '提示', '特征提取失败！请重试！')
            else:
                status_2 = db.save_feature(self.num,feature)
                if status_2 == 'ok':
                    os.rename(self.tmp_path + 'tmp.jpg', self.tmp_path + self.name + '.jpg')
                    # print('re ok')
                    shutil.copy(self.tmp_path + self.name + '.jpg', self.photo_path)
                    # print('copy ok')
                    shutil.rmtree(self.tmp_path)
                    os.mkdir(self.tmp_path)
                    no = self.num + '-' + self.ym
                    db.statistics(self.num,no,self.mon)
                    self.info = QtWidgets.QMessageBox.information(self, '提示', '保存成功！请刷新页面！')
                    self.close()
                else:
                    self.info = QtWidgets.QMessageBox.information(self, '提示', '特征保存失败！请重试！')

        else:
            self.info = QtWidgets.QMessageBox.information(self, '提示', '用户信息保存失败！请重试！')
            # self.facerec.show()

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    myshow = FaceRec()    # 创建实例
    myshow.show()           # 使用Qidget的show()方法
    sys.exit(app.exec_())
