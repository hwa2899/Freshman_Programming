# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 11:14:25 2018

@author: user
"""

import tkinter
def myDialogue2():
    global choice,msg
    #creates window
    win=tkinter.Tk()
    win.geometry("800x600")
    win.title("dialogue")
    #-------------------------
    choice=tkinter.StringVar()
    msg=tkinter.StringVar()
    #-------------------------
    #selection
    label_name=tkinter.Label(win,text="請選擇最喜歡的球類運動:")
    item1=tkinter.Radiobutton(win,text="足球",value="足球",variable=choice,command=clickOK2)
    item2=tkinter.Radiobutton(win,text="籃球",value="籃球",variable=choice,command=clickOK2)
    item3=tkinter.Radiobutton(win,text="棒球",value="棒球",variable=choice,command=clickOK2)
    label_msg=tkinter.Label(win,textvariable=msg)
    #-------------------------
    #show in window
    label_name.pack()
    item1.pack()
    item2.pack()
    item3.pack()
    item1.select()
    label_msg.pack()
    win.mainloop()
def clickOK2():
    global choice,msg
    msg.set("你最喜歡的活動是:"+choice.get())
myDialogue2()