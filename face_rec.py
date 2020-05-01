#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2020/4/15
# @Author    :Beobachter

import dlib         # 人脸处理的库 Dlib
import numpy as np   # 数据处理的库 numpy


# 人脸识别模型，提取128D的特征矢量
facerec = dlib.face_recognition_model_v1("data/data_dlib/dlib_face_recognition_resnet_model_v1.dat")


# 计算两个128D向量间的欧式距离
def return_euclidean_distance(feature_1, feature_2):
    feature1 = np.array(feature_1)
    feature2 = np.array(feature_2)
    dist = np.sqrt(np.sum(np.square(feature1 - feature2)))
    return dist


def Face_REC(image,face,feature):
        # 用来存放所有录入人脸特征的数组
    features_known_arr = feature
    if features_known_arr[0] != 0:
        # Dlib 检测器和预测器
        predictor = dlib.shape_predictor('data/data_dlib/shape_predictor_68_face_landmarks.dat')
        features_cap_arr = []
        shape = predictor(image, face)
        features_cap_arr.append(facerec.compute_face_descriptor(image, shape))
        e_distance_list = []
        for i in range(len(features_known_arr)):
            e_distance_tmp = return_euclidean_distance(features_cap_arr, features_known_arr[i])
            e_distance_list.append(e_distance_tmp)
        similar_person_num = e_distance_list.index(min(e_distance_list))
        if min(e_distance_list) < 0.4:
            return similar_person_num
        else:
            return 'unknow'
    else:
        return 'unknow'


