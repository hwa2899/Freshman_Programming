# -*- coding: utf-8 -*-
"""
Created on Mon May 28 13:04:44 2018

@author: Ching
"""

# -*- coding: utf-8 -*-
"""
Created on Sun May 27 21:25:59 2018

@author: Ching
"""

import tkinter 
import random
import pygame
import time

def mess():
    global flag
    flag=0
def initmoney():
    global money
    money=100
    window()
def window():
    global bet1,bet2,bet3,msg1,msg2,msg3,f1,money
    global a,b,c,gameinfo,times,ok
    global h1,h2,h3,t1,t2,t3,info1,info2,info3,flag
    global m1,m2,m3
    if flag==1:
        f2.destroy()
        flag=0
    f1=tkinter.Frame(win)
    f1.pack()
    #-------------------------------
    aa=0
    gameinfo=tkinter.Label(f1,text=money)
    gameinfo.grid(row=aa,column=0,padx=5,pady=5)
    #--------------------------------
    times=tkinter.Label(f1,text="賠率")
    times.grid(row=aa,column=3,padx=5,pady=5)
    #input bet horse one
    bb=1
    info1=tkinter.Label(f1, text="絕塵可以跑每秒2或3公尺")
    info1.grid(row=bb,column=0,padx=5,pady=5)
    h1=tkinter.Label(f1,text='絕塵:')
    h1.grid(row=bb,column=1,padx=5,pady=5)
    bet1=tkinter.StringVar()
    a=tkinter.Entry(f1,textvariable=bet1)
    a.grid(row=bb,column=2,padx=5,pady=5)
    x=random.randint(1,5)
    m1=1+(x/5)
    t1=tkinter.Label(f1,text=m1) #bets
    t1.grid(row=1,column=3,padx=5,pady=5)    
    #--------------------------------
    #input bet horse two
    cc=2
    info2=tkinter.Label(f1, text="赤兔可以跑每秒1或4公尺")
    info2.grid(row=cc,column=0,padx=5,pady=5)
    h2=tkinter.Label(f1,text="赤兔:")
    h2.grid(row=cc,column=1,padx=5,pady=5)
    bet2=tkinter.StringVar()
    b=tkinter.Entry(f1,textvariable=bet2)
    b.grid(row=cc,column=2,padx=5,pady=5)
    y=random.randint(1,5)
    m2=1+(y/5)
    t2=tkinter.Label(f1,text=m2) #bets
    t2.grid(row=cc,column=3,padx=5,pady=5)
    #---------------------------------
    #input bet horse three
    dd=3
    info3=tkinter.Label(f1, text="飛電可以跑每秒1或2或8公尺")
    info3.grid(row=dd,column=0,padx=5,pady=5)
    h3=tkinter.Label(f1,text="飛電:")
    h3.grid(row=dd,column=1,padx=5,pady=5)
    bet3=tkinter.StringVar()
    c=tkinter.Entry(f1,textvariable=bet3)
    c.grid(row=dd,column=2,padx=5,pady=5)
    z=random.randint(1,5)
    m3=1+(z/5)
    t3=tkinter.Label(f1,text=m3) #bets
    t3.grid(row=dd,column=3,padx=5,pady=5)
    #---------------------------------
    #ok button
    ok=tkinter.Button(f1,text='ok',width=20,command=bet)
    ok.grid(row=4,column=0,padx=5,pady=5)
    #---------------------------------
    #message after betting
    msg1=tkinter.StringVar()
    labelmsg=tkinter.Label(f1,textvariable=msg1)
    labelmsg.grid(row=5,column=0,padx=5,pady=5)
    
    msg2=tkinter.StringVar()
    msgs=tkinter.Label(f1, textvariable=msg2)
    msgs.grid(row=6,column=0,padx=5,pady=5)
    
    msg3=tkinter.StringVar()
    mesg=tkinter.Label(f1, textvariable=msg3)
    mesg.grid(row=7,column=0,padx=5,pady=5)

    win.mainloop()
    #---------------------------------
def bet():
    global bet1,bet2,bet3,msg1,msg2,msg3,money1,money2,money3
    money1=int(bet1.get())
    money2=int(bet2.get())
    money3=int(bet3.get())
    check()

def run():   
    msg1.set("下注 " +bet1.get() +" 點給絕塵!")
    msg2.set("下注 " +bet2.get() +" 點給赤兔!")
    msg3.set("下注 " +bet3.get() +" 點給飛電!")
    next1=tkinter.Button(f1,text='next',width=20,command=speed)
    next1.grid(row=8,column=0,padx=5,pady=5)
def speed():
    global f1, s1, s2,s3
    x=random.randint(0,1)
    if x==0:
        r1=tkinter.Label(f1,text="絕塵以2m/s前進!")
        r1.grid(row=9,column=0,padx=5,pady=5)
        s1=2
    else:
        r1=tkinter.Label(f1,text="絕塵以3m/s前進!")
        r1.grid(row=9,column=0,padx=5,pady=5)
        s1=3
    #---------------------------------------
    y=random.randint(0,1)
    if y==0:
        r2=tkinter.Label(f1,text="赤兔以1m/s前進!")
        r2.grid(row=10,column=0,padx=5,pady=5)
        s2=1
    else:
        r2=tkinter.Label(f1,text="赤兔以4m/s前進!")
        r2.grid(row=10,column=0,padx=5,pady=5)
        s2=4
    #----------------------------------------
    z=random.randint(0,2)
    if z==0:
        r3=tkinter.Label(f1,text="飛電以1m/s前進!")
        r3.grid(row=11,column=0,padx=5,pady=5)
        s3=1
    elif z==1:
        r3=tkinter.Label(f1,text="飛電以2m/s前進!")
        r3.grid(row=11,column=0,padx=5,pady=5)
        s3=2
    else:
        r3=tkinter.Label(f1,text="飛電以8m/s前進!")
        r3.grid(row=11,column=0,padx=5,pady=5)
        s3=8
    #----------------------------------------
    viz()
    next2=tkinter.Button(f1,text='next',width=20,command=winner)
    next2.grid(row=12,column=0,padx=5,pady=5)
def viz():
    global screen, canvas, clock, sound
    global green, red, yellow
    global gx,gy,ya,yb,rc,rd
    pygame.init()
    screen=pygame.display.set_mode([574,648])
    pygame.display.set_caption("Horse")
    clock=pygame.time.Clock()

    canvas=pygame.image.load("map.jpg")
    canvas.convert()
    green=pygame.image.load("yoshi green.png")
    green.convert()
    gy=57
    yellow=pygame.image.load("yoshi yellow.png")
    yellow.convert()
    yb=275
    red=pygame.image.load("yoshi red.png")
    red.convert()
    rd=496
    
    pygame.mixer.init()
    pygame.mixer.music.load("mario bro.mp3")
    pygame.mixer.music.play(-1)
    gx=0    
    ya=0    
    rc=0    
    
    running=True
    while running:
        clock.tick(30)
        if gx<453:
            gx+=s1*10
        if ya<450:
            ya+=s2*10
        if rc<453:
            rc+=s3*10
        time.sleep(0.5)
        screen.blit(canvas,[0,0])
        screen.blit(green,[gx,gy])
        screen.blit(yellow,[ya,yb])
        screen.blit(red,[rc,rd])
        font=pygame.font.Font("DFTTNC5.TTC",40)
        text1=font.render("絕塵",True,[100,50,0])
        text2=font.render("赤兔",True,[255,255,255])
        text3=font.render("飛電",True,[0,0,0])
        screen.blit(text1,[25,10])
        screen.blit(text2,[25,230])
        screen.blit(text3,[25,460])
        pygame.display.update()
        if gx>=453 and ya>=450 and rc>=453:
            time.sleep(0.5)
            break
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
    pygame.quit()
def winner():
    global f1,s1,s2,s3
    dist=tkinter.Label(f1,text="總共跑100公尺 總共花費秒數:")
    dist.grid(row=8,column=1,padx=5,pady=5)
    d1="%.2f"%(100/s1)
    w1=tkinter.Label(f1,text=d1)
    w1.grid(row=9,column=1,padx=5,pady=5)
    #----------------------------------------
    d2="%.2f"%(100/s2)
    w2=tkinter.Label(f1,text=d2)
    w2.grid(row=10,column=1,padx=5,pady=5)
    #----------------------------------------
    d3="%.2f"%(100/s3)
    w3=tkinter.Label(f1,text=d3)
    w3.grid(row=11,column=1,padx=5,pady=5)
    #----------------------------------------
    win_info=tkinter.Label(f1,text="贏家:")
    win_info.grid(row=13,column=0,padx=5,pady=5)
    #----------------------------------------
    if s1>s2 and s1>s3:
        w=tkinter.Label(f1,text="絕塵")
        w.grid(row=13,column=1,padx=5,pady=5)
    elif s2>s1 and s2>s3:
        w=tkinter.Label(f1,text="赤兔")
        w.grid(row=13,column=1,padx=5,pady=5)
    elif s3>s2 and s3>s1:
        w=tkinter.Label(f1,text="飛電")
        w.grid(row=13,column=1,padx=5,pady=5)
    else:
        w=tkinter.Label(f1,text="絕塵 跟 飛電")
        w.grid(row=13,column=1,padx=5,pady=5)
    results=tkinter.Button(f1,text="Results",width=20,command=result)
    results.grid(row=14,column=0,padx=5,pady=5)
def result():
    global f1,bet1,bet2,bet3,money
    global m1,m2,m3,s1,s2,s3
    
    money=money-(money1+money2+money3)
    total=tkinter.Label(f1,text=money)
    total.grid(row=15,column=0,padx=5,pady=5)
    #----------------------------------------
    if s1>s2 and s1>s3:
        res1=m1*money1
        result1=tkinter.Label(f1,text=res1)
        result1.grid(row=16,column=0,padx=5,pady=5)
    else:
        res1=0
        result1=tkinter.Label(f1,text=res1)
        result1.grid(row=16,column=0,padx=5,pady=5)
    #----------------------------------------
    if s2>s1 and s2>s3:
        res2=m2*money2
        result2=tkinter.Label(f1,text=res2)
        result2.grid(row=17,column=0,padx=5,pady=5)
    else:
        res2=0
        result2=tkinter.Label(f1,text=res2)
        result2.grid(row=17,column=0,padx=5,pady=5)
    #----------------------------------------
    if s3>s2 and s3>s1:
        res3=m3*money3
        result3=tkinter.Label(f1,text=res3)
        result3.grid(row=18,column=0,padx=5,pady=5)
    else:
        res3=0
        result3=tkinter.Label(f1,text=res3)
        result3.grid(row=18,column=0,padx=5,pady=5)
    #----------------------------------------
    if s1==s3 and s1>s2:
        res1=m1*money1
        result1=tkinter.Label(f1,text=res1)
        result1.grid(row=16,column=0,padx=5,pady=5)
        res3=m3*money3
        result3=tkinter.Label(f1,text=res3)
        result3.grid(row=18,column=0,padx=5,pady=5)
    #----------------------------------------
    totalsum=tkinter.Label(f1,text="Total amount:")
    totalsum.grid(row=14,column=1,padx=5,pady=5)
    money=money+res1+res2+res3
    totals=tkinter.Label(f1,text=money)
    totals.grid(row=15,column=1,padx=5,pady=5)
    conti=tkinter.Label(f1,text="Continue?")
    conti.grid(row=14,column=2,padx=5,pady=5)
    if money>0:
        yes=tkinter.Button(f1,text="Yes",width=10,command=cont)
        yes.grid(row=15,column=2,padx=5,pady=5)
    restart=tkinter.Button(f1,text="Restart",width=10,command=clearall)
    restart.grid(row=16,column=2,padx=5,pady=5)
    no=tkinter.Button(f1,text="No",width=10,command=xit)
    no.grid(row=17,column=2,padx=5,pady=5)
def check():
    global wrong,wrongbutton,flag,f2
    #check amount
    if money1+money2+money3>money:
        f1.destroy()
        f2=tkinter.Frame(win)
        f2.pack()
        wrong=tkinter.Label(f2,text="Exceeds amount")
        wrong.grid(row=1,column=0,padx=5,pady=5)
        wrongbutton=tkinter.Button(f2,text="OK",width=10,command=window)
        wrongbutton.grid(row=2,column=0,padx=5,pady=5)
        flag=1
    else:
        run()
def cont():
    f1.destroy()
    window()
def clearall():
    f1.destroy()
    initmoney()
def xit():
    win.destroy()

#---------------------------------------------

win=tkinter.Tk()
win.geometry("800x700")
win.title("game")
mess()
initmoney()