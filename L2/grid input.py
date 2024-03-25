# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 10:52:42 2018

@author: user
"""

import tkinter 

def window():
    global name,password,msg
    win=tkinter.Tk()
    win.geometry("800x600")
    win.title("game")

    f1=tkinter.Frame(win)
    f1.pack()
    #-------------------------------
    #input name
    l1=tkinter.Label(f1,text='name:')
    l1.grid(row=0,column=0,padx=5,pady=5)
    name=tkinter.StringVar()
    el=tkinter.Entry(f1,textvariable=name)
    el.grid(row=0,column=1,padx=5,pady=5)
    #--------------------------------
    #input password
    l2=tkinter.Label(f1,text="password:")
    l2.grid(row=1,column=0,padx=5,pady=5)
    password=tkinter.StringVar()
    enter=tkinter.Entry(f1,textvariable=password)
    enter.grid(row=1,column=1,padx=5,pady=5)
    #---------------------------------
    #ok button
    al=tkinter.Button(f1,text='ok',width=20,command=welcome)
    al.grid(row=2,column=0,padx=5,pady=5)
    #---------------------------------
    #message after entering
    msg=tkinter.StringVar()
    labelmsg=tkinter.Label(f1,textvariable=msg)
    labelmsg.grid(row=2,column=1,padx=5,pady=5)
    win.mainloop()
    #---------------------------------
def welcome():
    global name,password,msg
    msg.set("Welcome " +name.get() +" !")

window()
    