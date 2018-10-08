#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 2018
    
@author: Roman Starikov
"""

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk

import sender


class UI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Sender")
        self.root.geometry('600x600')
        self.root.resizable(False, False)
        self.root.config(bg = "white")
        if hasattr(sys, '_MEIPASS'):
            self.root.iconbitmap(os.path.join(sys._MEIPASS, 'icon.ico'))
        else:
            self.root.iconbitmap(os.path.join(os.path.abspath("."), 'icon.ico'))

        self.drawFrameAddresser()
        self.drawFrameAddressees()
        self.drawFrameGrades()
        self.drawFrameMessage()
        self.drawProgressBar()

        self.pathFileAddressees = ""
        self.pathFileGrades = ""

        self.sender = sender.Sender()


    def drawFrameAddresser(self):
        frame = Frame(self.root)
        frame.place(x = 20, y = 50, width = 560, height = 65)
        frame.config(relief = FLAT, highlightbackground = "grey",  highlightthickness = 3)
        frame.config(bg = "white")

        labelHeader = Label(self.root, text = "Addresser")
        labelHeader.place(x = 30, y = 10, width = 200, height = 40)
        labelHeader.config(font = ("Calibri", 20, "bold"), fg = "grey", anchor = W)
        labelHeader.config(bg = self.root['bg'])
    
        self.__entryEmail = Entry(frame)
        self.__entryEmail.place(x = 7, y = 10, width = 265, height = 40)
        self.__entryEmail.insert(0, "Enter e-mail..")
        self.__entryEmail.config(font=("Calibri", 13))
        self.__entryEmail.config(relief = FLAT, highlightbackground = "grey",  highlightthickness = 3)
        self.__entryEmail.config(bg = "white")

        self.__entryPassword = Entry(frame, show="*")
        self.__entryPassword.place(x = 282, y = 10, width = 265, height = 40)
        self.__entryPassword.insert(0, "Enter password..")
        self.__entryPassword.config(font=("Calibri", 13))
        self.__entryPassword.config(relief = FLAT, highlightbackground = "grey",  highlightthickness = 3)
        self.__entryPassword.config(bg = "white")

 
    def drawFrameAddressees(self):
        frame = Frame(self.root)
        frame.place(x = 20, y = 165, width = 270, height = 90)
        frame.config(relief = FLAT, highlightbackground = "grey",  highlightthickness = 3)
        frame.config(bg = "white")

        labelHeader = Label(self.root, text = "Addressees")
        labelHeader.place(x = 30, y = 125, width = 200, height = 40)
        labelHeader.config(font = ("Calibri", 20, "bold"), fg = "grey", anchor = W)
        labelHeader.config(bg = self.root['bg'])

        self.__labelFileAddressees = Label(frame, text = "None")
        self.__labelFileAddressees.place(x = 7, y = 5, width = 250, height = 25)
        self.__labelFileAddressees.config(font = ("Calibri", 13, "bold"), fg = "grey")
        self.__labelFileAddressees.config(bg = self.root['bg'])

        frameOpen = Frame(frame)
        frameOpen.place(x = 7, y = 40, width = 250, heigh = 40)
        frameOpen.config(relief = FLAT, highlightbackground = "grey",  highlightthickness = 3)
        buttonOpen = Button(frameOpen, text = "Select", relief = FLAT)
        buttonOpen.place(x = 0, y = 0, width = 244, height = 34)
        buttonOpen.config(font = ("Calibri", 13, "bold"), fg = "grey")
        buttonOpen.config(bg = "white")
        buttonOpen.config(command=self.onAddresseesSelect)


    def drawFrameGrades(self):
        frame = Frame(self.root)
        frame.place(x = 310, y = 165, width = 270, height = 90)
        frame.config(relief = FLAT, highlightbackground = "grey",  highlightthickness = 3)
        frame.config(bg = "white")

        labelHeader = Label(self.root, text = "Grades")
        labelHeader.place(x = 320, y = 125, width = 200, height = 40)
        labelHeader.config(font = ("Calibri", 20, "bold"), fg = "grey", anchor = W)
        labelHeader.config(bg = self.root['bg'])

        self.__labelFileGrades = Label(frame, text = "None")
        self.__labelFileGrades.place(x = 7, y = 5, width = 250, height = 25)
        self.__labelFileGrades.config(font = ("Calibri", 13, "bold"), fg = "grey")
        self.__labelFileGrades.config(bg = self.root['bg'])        

        frameOpen = Frame(frame)
        frameOpen.place(x = 7, y = 40, width = 250, heigh = 40)
        frameOpen.config(relief = FLAT, highlightbackground = "grey",  highlightthickness = 3)
        buttonOpen = Button(frameOpen, text = "Select", relief = FLAT)
        buttonOpen.place(x = 0, y = 0, width = 244, height = 34)
        buttonOpen.config(font = ("Calibri", 13, "bold"), fg = "grey")
        buttonOpen.config(bg = "white")
        buttonOpen.config(command=self.onGradesSelect)


    def drawFrameMessage(self):
        frame = Frame(self.root)
        frame.place(x = 20, y = 305, width = 560, height = 225)
        frame.config(relief = FLAT, highlightbackground = "grey",  highlightthickness = 3)
        frame.config(bg = "white")
        
        labelHeader = Label(self.root, text = "Message")
        labelHeader.place(x = 30, y = 265, width = 200, height = 40)
        labelHeader.config(font = ("Calibri", 20, "bold"), fg = "grey", anchor = W)
        labelHeader.config(bg = self.root['bg'])

        self.__entryTopic = Entry(frame)
        self.__entryTopic.place(x = 7, y = 10, width = 430, height = 40)
        self.__entryTopic.insert(0, "Enter topic..")
        self.__entryTopic.config(font=("Calibri", 13))
        self.__entryTopic.config(relief = FLAT, highlightbackground = "grey",  highlightthickness = 3)
        self.__entryTopic.config(bg = "white")

        frameSend = Frame(frame)
        frameSend.place(x = 445, y = 10, width = 102, height = 40)
        frameSend.config(relief = FLAT, highlightbackground = "grey",  highlightthickness = 3)
        buttonSend = Button(frameSend, text = "Send", relief = FLAT)
        buttonSend.place(x = 0, y = 0, width = 96, height = 34)
        buttonSend.config(font = ("Calibri", 13, "bold"), fg = "grey")
        buttonSend.config(bg = "white")
        buttonSend.config(command = self.onSend)

        frameScroll = Frame(frame)
        frameScroll.place(x = 522, y = 60, width = 25, height = 150)
        frameScroll.config(relief = FLAT, highlightbackground = "grey",  highlightthickness = 3)
        scrollMessage = Scrollbar(frameScroll, relief = FLAT)
        scrollMessage.place(x = 0, y = 0, width = 19, height = 144)
        scrollMessage.config(bg = "white")
        
        self.__textMessage = Text(frame)
        self.__textMessage.place(x = 7, y = 60, width = 505, height = 150)
        self.__textMessage.insert(0.0, "Enter text of message before grade..")
        self.__textMessage.config(relief = FLAT, highlightbackground = "grey",  highlightthickness = 3)
        self.__textMessage.config(font = ("Calibri", 13))
        self.__textMessage.config(bg = "white")

        scrollMessage.config(command = self.__textMessage.yview)
        self.__textMessage.config(yscrollcommand = scrollMessage.set)


    def drawProgressBar(self):
        self.__progressBar = ttk.Progressbar(self.root, orient = 'horizontal', mode = 'determinate')
        self.__progressBar.place(x = 20, y = 540, width = 560, height = 40)


    def updateProgressBar(self):
        self.__progressBar['value'] += 1
        self.root.update_idletasks()
    
    
    def onAddresseesSelect(self):
        self.pathFileAddressees = filedialog.askopenfilename(title = "Select file with addressees")

        result = self.sender.setEmails(self.pathFileAddressees)
        if result == "":
            p = self.pathFileAddressees.split('/')
            self.__labelFileAddressees['text'] = p[len(p)-1]
        else:
            messagebox.showerror("Error!", result)
            self.pathFileAddressees = ""
            self.__labelFileAddressees['text'] = "None"


    def onGradesSelect(self):
        self.pathFileGrades = filedialog.askopenfilename(title = "Select file")

        result = self.sender.setGroup(self.pathFileGrades)
        if result == "":
            p = self.pathFileGrades.split('/')
            self.__labelFileGrades['text'] = p[len(p)-1]
        else:
            messagebox.showerror("Error!", result)
            self.pathFileGrades = ""
            self.__labelFileGrades['text'] = "None"


    def onSend(self):
        if self.pathFileAddressees == "":
            messagebox.showerror("Error!", "Addressees file is not selected!")
            return
        if self.pathFileGrades == "":
            messagebox.showerror("Error!", "Grades file is not selected!")
            return
        if self.__entryEmail.get() == "":
            messagebox.showerror("Error!", "Addressor email is empty!")
            return
        if self.__entryPassword.get() == "":
            messagebox.showerror("Error!", "Addressor password is empty!")
            return

        dialog = messagebox.askyesno("Send", "Are you sure?")
        if dialog == True:
            self.root.grab_set()
            self.__progressBar['maximum'] = len(self.sender.getGroup())
            
            self.sender.setAddresser(self.__entryEmail.get(), self.__entryPassword.get())
            self.sender.setMessage(self.__entryTopic.get(),self.__textMessage.get("1.0", END))
            
            result = self.sender.send(self.updateProgressBar)
            if result == "":
                messagebox.showinfo("Done!", "Emails have been sent!");
            else:
                messagebox.showerror("Error!", result)

            self.root.grab_release()
            self.__progressBar['value'] = 0


ui = UI()
ui.root.mainloop()
