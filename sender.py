#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 2018

@author: Anton Kushnikov
"""

import pandas as pd 
import smtplib

 
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
        try:
            self.__emailTable = pd.read_excel(filePath)
            if len(self.__emailTable.columns) != 2:
                raise Exception("Bad columns!")
            return ""
        except Exception as e:
            return str(e)
            
        
    def setGroup(self, filePath):
        try:
            self.__gradeTable = pd.read_excel(filePath)
            for grade in self.__gradeTable:
                if len(self.__gradeTable.columns) < 2:
                    raise Exception("Wrong grades!")
            return ""
        except Exception as e:
            return str(e)
            
        
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
        # The number of the column should be changed depending on the format of the table
        # Implying that the name goes first
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
        
    def send(self, f):
        try:
            group = self.getGroup()
            # Here we send a letter to each student
            for student in group:
                if student != None:
                    studentName = student[0]
                    TO = self.getEmail(studentName)
                    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
                    # Enable encoding
                    smtpObj.starttls()
                    # Logging in. Data should be taken from the UI
                    login = self.getAddresser()[0]
                    password = self.getAddresser()[1]
                    smtpObj.login(login, password)
                    # Trying to make a letter
                    rawMsg = ""
                    for i in range(len(self.__gradeTable.columns)):
                        rawMsg += (self.__gradeTable.columns[i] + ": " + str(student[i]) + "\n")
                    msg = "\n" + self.getMessage()[1] + "\n\n" + rawMsg
                    BODY = '\r\n'.join(['To: %s' % TO,
                                        'From: %s' % login,
                                        'Subject: %s' % self.getMessage()[0],
                                        '', msg])

                    smtpObj.sendmail(login, [TO], BODY)
                    f()
                    smtpObj.quit()
            return ""
        except Exception as e:
            return str(e)
        
    

    
