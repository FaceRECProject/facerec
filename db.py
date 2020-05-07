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

def fetch_id():
    db = mysql.connector.connect(host='localhost', user='user', passwd='user123', db='fs')
    cursor = db.cursor()
    sql = "SELECT ID FROM user_info "
    cursor.execute(sql)
    val = cursor.fetchall()
    return val
    db.close()

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

def save_att(no,id,datetime,date,abs='0',latetime='0',overtime='0'):
    db = mysql.connector.connect(host='localhost', user='user', passwd='user123', db='fs')
    print(db)
    cursor = db.cursor()
    sql_get = "SELECT * FROM attendance WHERE date=%s AND id = %s"
    NO = (date,id)
    cursor.execute(sql_get, NO)
    val = cursor.fetchall()
    # print(val)
    if val == []:
        sql = "INSERT INTO attendance(no,id,start,end,date,latetime,overtime,abs)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        time = (no,id,datetime,datetime,date,latetime,overtime,abs)
        try:
            cursor.execute(sql, time)
            db.commit()
            return 'ok'
        except:
            db.rollback()
            return 'error'
    else:
        sql = "UPDATE attendance SET end = %s,overtime=%s WHERE date=%s AND id = %s"
        time = (datetime,overtime,date,id)
        cursor.execute(sql, time)
        db.commit()
    db.close()

def get_his(id,date):
    db = mysql.connector.connect(host='localhost', user='user', passwd='user123', db='fs')
    cursor = db.cursor()
    sql = "SELECT * FROM attendance WHERE date=%s and id=%s"
    NO = (date,id)
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
    if val == []:
        insert = "INSERT INTO statistics(s_no,s_id,mon,late,absence)VALUES(%s,%s,%s,%s,%s)"
        data = (no,id,mon,late,absence)
        cursor.execute(insert,data)
        db.commit()
    else:
        update = "UPDATE statistics SET mon = %s,late=%s , absence = %s WHERE s_no=%s AND s_id = %s"
        data = (mon,late,absence,no,id)
        cursor.execute(insert, data)
        db.commit()

def get_statistics(month,id):
    db = mysql.connector.connect(host='localhost', user='user', passwd='user123', db='fs')
    cursor = db.cursor()
    sql = "SELECT late,absence FROM statistics WHERE mon = %s AND s_id = %s"
    no = (month,id)
    try:
        cursor.execute(sql, no)
        val = cursor.fetchall()
        return val
    except:
        db.rollback()
        return 'error'
    db.close()
