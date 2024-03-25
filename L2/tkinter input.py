# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 10:51:02 2018

@author: user
"""

import tkinter 

win=tkinter.Tk()
win.geometry("800x600")
win.title("game")

f1=tkinter.Frame(win)
f1.pack()

l1=tkinter.Label(f1,text='name')
l1.pack()
yourname=tkinter.StringVar()
el=tkinter.Entry(f1,textvariable=yourname)
el.pack()

al=tkinter.Button(f1,text='ok',width=20)
al.pack()

win.mainloop()