# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 11:50:38 2018

@author: user
"""

import tkinter
def myDialogue3():
    global choice,ball,msg
    #create window
    win=tkinter.Tk()
    win.geometry("800x600")
    win.title("dialogue")
    #-------------------------
    #multiple choice
    label_name=tkinter.Label(win,text="請選擇最喜歡的球類運動:")
    label_name.pack()
    ball=["足球","籃球","棒球"]
    choice=[]
    for i in range(0,len(ball)):
        choice.append(tkinter.IntVar())
        item=tkinter.Checkbutton(win,text=ball[i],variable=choice[i],command=clickOK3)
        item.pack()
    #--------------------------
    msg=tkinter.StringVar()
    label_msg=tkinter.Label(win,textvariable=msg)
    label_msg.pack()
    win.mainloop()
def clickOK3():
    global choice,ball,msg
    str="你最喜歡的活動是:"
    for i in range(0,len(ball)):
        if(choice[i].get()==1):
            str=str+ball[i]+" "
    msg.set(str)
myDialogue3()