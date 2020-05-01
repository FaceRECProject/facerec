#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2020/4/15
# @Author    :Beobachter

import cv2
import os
import dlib
from skimage import io
import json
import numpy as np



# Dlib 正向人脸检测器
detector = dlib.get_frontal_face_detector()

# Dlib 人脸预测器
predictor = dlib.shape_predictor("data/data_dlib/shape_predictor_68_face_landmarks.dat")

# Dlib 人脸识别模型
face_rec = dlib.face_recognition_model_v1("data/data_dlib/dlib_face_recognition_resnet_model_v1.dat")


# 返回单张图像的 128D 特征
def return_128d_features(path_img):
    img_rd = io.imread(path_img)
    faces = detector(img_rd, 1)



    # 检测到人脸的人脸图像算特征
    if len(faces) != 0:
        shape = predictor(img_rd, faces[0])
        face_descriptor = face_rec.compute_face_descriptor(img_rd, shape)
    else:
        face_descriptor = 0
        # print("no face")

    return face_descriptor

def return_features_mean_personX(path_faces_personX):
    features_list_personX = []
    photos_list = os.listdir(path_faces_personX)
    if photos_list:
        features_128d = return_128d_features(path_faces_personX + "/" + photos_list[0])
        features_list_personX.append(features_128d)
    else:
        features_128d = 0

    # 计算 128D 特征的均值
    # personX 的 N 张图像 x 128D -> 1 x 128D
    if features_128d != 0:
        features_mean_personX = np.array(features_list_personX).mean(axis=0)
        features_mean_personX = features_mean_personX.tolist()
    else:
        features_mean_personX = 0

    return features_mean_personX


