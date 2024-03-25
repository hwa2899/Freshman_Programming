# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 10:52:01 2018

@author: user
"""

import tkinter 

win=tkinter.Tk()
win.geometry("800x600")
win.title("game")

f1=tkinter.Frame(win)
f1.pack()

okbutton=tkinter.Button(f1,text="ok")
okbutton.pack(padx=20,pady=20)
button=tkinter.Button(f1,text="ok",width=20)
button.pack(padx=20,pady=20)

f2=tkinter.Frame(win)
f2.pack()

b1=tkinter.Button(f2,text="ok",width=10)
b2=tkinter.Button(f2,text="ok",width=10)
b3=tkinter.Button(f2,text="ok",width=20)
b4=tkinter.Button(f2,text="ok",width=20)
b1.grid(row=0,column=0,padx=10,pady=10,sticky='e')
b2.grid(row=0,column=1,padx=10,pady=10,sticky='w')
b3.grid(row=1,column=0,padx=10,pady=10)
b4.grid(row=1,column=1,padx=10,pady=10)


win.mainloop()