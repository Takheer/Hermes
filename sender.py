#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 20:43:38 2018

@author: anton
"""

import os
import pandas as pd 
import smtplib
import sys
from configparser import ConfigParser
# import FileParser
 
class Sender:
    def __init__(self):
        self.__gradeTable = ""
        self.__emailTable = ""
        self.__addresser = ["", ""]    # login, password
        self.__message = ["", ""]      # topic, message
        self.__emails = ""
        self.__grades = ""

###-----------------------------------SETTERS----------------------------------
    
    def setEmails(self, filePath):
        self.__emailTable = pd.read_excel(filePath)
        
    def setGrades(self, filePath):
        self.__gradeTable = pd.read_excel(filePath)        
        
    def setAddresser(self, login, password) :
        self.__addresser = [login, password]
        
    def setMessage(self, topic, msg):
        self.__message = [topic, msg]
        
        
###-----------------------------------GETTERS----------------------------------
        
    def getAddresser(self):
        return self.__addresser
    
    def getMessage(self):
        return self.__message
    
    def getEmails(self):
        return self.__emailTable
        
    def getGroup(self):
        group = []
        # В зависимости от формата таблицы нужно будет изменить номер столбца
        # Сейчас подразумевается, что первым стоит имя
        for i in self.__gradeTable.index:
            student = []
            columns = self.__gradeTable.columns
            for column in range(len(columns)):
                student.append(self.__gradeTable[columns[column]][i])
            group.append(student)
        return(group)
    
    def getEmail(self, name):
        for i in self.__emailTable.index:
            if self.__emailTable[self.__emailTable.columns[0]][i] == name:
                email = self.__emailTable[self.__emailTable.columns[1]][i]
                return(email)
    
###-----------------------------------METHODS----------------------------------
        
    def send(self):
        group = self.getGroup()
        # Будем отправлять сообщение каждому студенту
        for student in group:
            if student != None:
                studentName = student[0]
                studentEmail = self.getEmail(studentName)
                #smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
                # Включаем шифрование
                #smtpObj.starttls()
                # Логинимся. Тут данные надо взять с интерфейса
                login = self.getAddresser()[0]
                password = self.getAddresser()[1]
                #smtpObj.login(login, password)
                msg = "Dear " + studentName + "! Here is your grades, they are going to your email address: " + studentEmail + "\n\n"
                # пытаемся составить сообщение
                for i in range(len(self.__gradeTable.columns)):
                    msg += (self.__gradeTable.columns[i] + ": " + str(student[i]) + "\n")
                
                #smtpObj.sendmail(login, studentEmail, msg)
                #smtpObj.quit()
                print(login)
                print(password)
                print(msg + "\n\n\n")
        
    

    
