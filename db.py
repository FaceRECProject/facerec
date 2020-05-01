#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2020/4/30 
# @Author    :Beobachter

import numpy as np
import mysql.connector

def save_info(dict,image_path):
    db = mysql.connector.connect(host='localhost',user='user',passwd='user123',db='fs')
    cursor =db.cursor()
    sql = "INSERT INTO user_info(ID,name,sex,department,img_path)VALUES(%s,%s,%s,%s,%s)"
    info = (dict['number'],dict['name'],dict['sex'],dict['department'],image_path)
    try:
        cursor.execute(sql,info)
        db.commit()
        return 'ok'
    except:
        db.rollback()
        return 'error'
    db.close()

def fetch_info(id):
    db = mysql.connector.connect(host='localhost',user='user',passwd='user123',db='fs')
    cursor =db.cursor()
    sql = "SELECT * FROM user_info WHERE ID = %s"
    uid = (id,)
    try:
        cursor.execute(sql,uid)
        val = cursor.fetchall()

    except:
        db.rollback()
        return 'error'
    db.close()
    return val

def save_feature(id,feature):
    db = mysql.connector.connect(host='localhost', user='user', passwd='user123', db='fs')
    cursor = db.cursor()
    sql = "INSERT INTO face_features(face_ID,feature)VALUES(%s,%s)"
    x = ','.join([str(i) for i in feature])
    face_info = (id,x)
    try:
        cursor.execute(sql, face_info)
        db.commit()
        return 'ok'
    except:
        db.rollback()
        return 'error'
    db.close()

def get_features():
    db = mysql.connector.connect(host='localhost', user='user', passwd='user123', db='fs')
    cursor = db.cursor()
    sql = "SELECT * FROM face_features"
    try:
        cursor.execute(sql)
        val = cursor.fetchall()
        return val
    except:
        db.rollback()
        return 'error'
    db.close()

def save_att(no,id,datetime,date):
    db = mysql.connector.connect(host='localhost', user='user', passwd='user123', db='fs')
    cursor = db.cursor()
    sql_get = "SELECT * FROM attendance WHERE no=%s AND id = %s"
    NO = (no,id)
    cursor.execute(sql_get, NO)
    val = cursor.fetchall()
    if val == NULL:
        sql = "INSERT INTO attendance(no,id,start,end,date,count)VALUES(%s,%s,%s,%s,%d)"
        time = (no,id,datetime,datetime,date,1)
        try:
            cursor.execute(sql, time)
            db.commit()
            return 'ok'
        except:
            db.rollback()
            return 'error'
    else:
        sql = "UPDATE attendance SET end = %s,count=%d WHERE no=%s AND id = %s"
        time = (datetime,2,no,id)
        cursor.execute(sql, time)
        db.commit()
    db.close()

def get_count(no):
    db = mysql.connector.connect(host='localhost', user='user', passwd='user123', db='fs')
    cursor = db.cursor()
    sql = "SELECT count FROM attendance WHERE no = %s"
    NO = (no,)
    try:
        cursor.execute(sql,NO)
        val = cursor.fetchall()
        return val
    except:
        db.rollback()
        return 'error'
    db.close()

def statistics(id,no,mon=0,late=0,absence=0):
    db = mysql.connector.connect(host='localhost', user='user', passwd='user123', db='fs')
    cursor = db.cursor()

    sql = "SELECT * FROM statistics WHERE s_no = %s AND s_id = %s"
    NO = (no,id)
    cursor.execute(sql, NO)
    val = cursor.fetchall()
    if val == NULL:
        insert = "INSERT INTO statistics(s_no,s_id,mon,late,absence)VALUES(%s,%s,%d,%d,%d)"
        data = (no,id,mon,late,absence)
        cursor.execute(insert,data)
        db.commit()
    else:
        update = "UPDATE statistics SET mon = %d,late=%d , absence = %d WHERE s_no=%s AND s_id = %s"
        data = (mon,late,absence,no,id)
        cursor.execute(insert, data)
        db.commit()

def get_statistics(no,id):
    db = mysql.connector.connect(host='localhost', user='user', passwd='user123', db='fs')
    cursor = db.cursor()
    sql = "SELECT mon,late,absence FROM statistics WHERE s_no = %s AND s_id = %s"
    no = (no,id)
    try:
        cursor.execute(sql, no)
        val = cursor.fetchall()
        return val
    except:
        db.rollback()
        return 'error'
    db.close()
# f = np.array([1,2,3])
# f= f.tolist()
# # print(f)
# save_feature('0221',f)
# features = get_features()
# id = []
# feature = []
# if features != 'error':
#     for val in features:
#         id.append(val[0])
#         c = [int(y) for y in (val[1].split(','))]
#         feature.append(c)
# print(id,feature)

# f = [1,2,3,3]
# x = ','.join([str(i)for i in f])
# print(type(x))
# c = [int(y) for y in (x.split(','))]
# print(type(c),c)
