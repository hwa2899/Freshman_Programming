# -*- coding: utf-8 -*-

import tkinter
import random
import pygame
import time
    
#遊戲初始設定
def initGame():
    global win,er,control2
    win=tkinter.Tk()
    win.geometry("800x600")
    win.title("horse")     
    er=0
    control2=0
    
    frame1=tkinter.Frame(win)
    frame1.pack()
    des1=tkinter.Label(frame1,text="馬匹資訊：")
    des2=tkinter.Label(frame1,text="賠率：")
    con1=tkinter.Label(frame1,text="絕塵：每秒可跑2或3公尺" )
    con2=tkinter.Label(frame1,text="赤兔：每秒可跑1或4公尺")
    con3=tkinter.Label(frame1,text="飛電：每秒可跑1或2或8公尺")
    con11=tkinter.Label(frame1,text=3,width=10)
    con22=tkinter.Label(frame1,text=3,width=10)
    con33=tkinter.Label(frame1,text=2,width=10)
    
    des1.grid(row=0,column=0)
    des2.grid(row=0,column=1)
    con1.grid(row=1,column=0)
    con11.grid(row=1,column=1)
    con2.grid(row=2,column=0)
    con22.grid(row=2,column=1)
    con3.grid(row=3,column=0)
    con33.grid(row=3,column=1)

def initMoney():
    global money
    money=100
    play()

#關閉視窗
def end():
    win.destroy()
    
#輸入
def play(): 
    global frame2,v1,v2,v3,h11,h22,h33
    if er==1:
        frame4.destroy()
    elif er==2:
        frame5.destroy()
    if control2==1:
        frame2.destroy()
        frame3.destroy()
        frame6.destroy()
    frame2=tkinter.Frame(win)
    frame2.pack() 
    des3=tkinter.Label(frame2,text="您有"+str(money)+"元,請下注",height=3)
    h1=tkinter.Label(frame2,text="絕塵：")
    h2=tkinter.Label(frame2,text="赤兔：")
    h3=tkinter.Label(frame2,text="飛電：")
    v1=tkinter.StringVar() 
    v2=tkinter.StringVar()
    v3=tkinter.StringVar() 
    
    h11=tkinter.Entry(frame2,textvariable=v1)
    h22=tkinter.Entry(frame2,textvariable=v2)
    h33=tkinter.Entry(frame2,textvariable=v3)
    button=tkinter.Button(frame2,text="ok",width=15,height=2,command=error)
                
    des3.grid(row=0,column=1)
    h1.grid(row=1,column=0)
    h11.grid(row=1,column=1)
    h2.grid(row=2,column=0)
    h22.grid(row=2,column=1)
    h3.grid(row=3,column=0)
    h33.grid(row=3,column=1)
    button.grid(row=4,column=1)

#除錯        
def error():
    global m1,m2,m3,frame4,frame5,er
    try:
        m1=int(v1.get())
        m2=int(v2.get())
        m3=int(v3.get())
        control=1
    except:
        control=0
        frame2.destroy()
        frame4=tkinter.Frame(win)
        frame4.pack()
        ve=tkinter.Label(frame4,text="請輸入整數",height=3)
        button2=tkinter.Button(frame4,text="我知道了",width=15,height=2,command=play)
        ve.pack()
        button2.pack()
        er=1 
                
    if control==1 and m1+m2+m3>money:
        frame2.destroy()
        frame5=tkinter.Frame(win)
        frame5.pack() 
        error=tkinter.Label(frame5,text="您只有"+str(money)+"元，請重新下注",height=3)
        button3=tkinter.Button(frame5,text="我知道了",width=15,height=2,command=play)
        error.pack()
        button3.pack()
        er=2 
    elif control==1:
        run()

#運算
def run():
    global money,ss1,ss2,ss3,s1,s2,s3,n1,n2,n3,winner
    s1=0
    s2=0
    s3=0
    n1=0
    n2=0
    n3=0
    ss1=random.choice([2,3])
    ss2=random.choice([1,4])
    ss3=random.choice([1,2,8])
    
    while s1<100:   
        s1+=ss1
        n1+=1
    while s2<100:
        s2+=ss2
        n2+=1
    while s3<100:
        s3+=ss3
        n3+=1
    
    if n1<n2 and n1<n3:
        winner="絕塵"
        money=money+m1*3-m2-m3
    elif n2<n1 and n2<n3:
        winner="赤兔"
        money=money+m2*3-m1-m3
    elif n3<n1 and n3<n2:
        winner="飛電"
        money=money+m3*2-m1-m2
    else:
        winner="絕塵和飛電"
        money=money+m1*3+m3*2-m2
    display()

#比賽畫面呈現        
def display():
    end()
    pygame.init()
    screen=pygame.display.set_mode([1100,300]) 
    pygame.display.set_caption("race")
    clock=pygame.time.Clock()
    canvas=pygame.Surface(screen.get_size()) 
    canvas=pygame.image.load("草地.jpg")
    canvas.convert() 
    pygame.draw.rect(canvas,[255,0,0],[885,0,15,300])
    horse1=pygame.image.load("絕塵.png")
    horse1.convert()
    horse2=pygame.image.load("赤兔.png")
    horse2.convert()
    horse3=pygame.image.load("飛電.png")
    horse3.convert()
    pygame.mixer.init()
    pygame.mixer.music.load("Master_of_the_Feast.ogg")
#    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play(-1)
    x1=0
    x2=0
    x3=0
    running=True 
    while running: 
        clock.tick(30)
        if x1<900:
            x1+=ss1*9
        if x2<900:
            x2+=ss2*9
        if x3<900:
            x3+=ss3*9
        time.sleep(0.2)
        screen.blit(canvas,[0,0]) 
        screen.blit(horse1,[x1,0])
        screen.blit(horse2,[x2,110])
        screen.blit(horse3,[x3,220])
        font=pygame.font.Font("DFTTNC5.TTC",40)
        text1=font.render("絕塵",True,[100,50,0])
        text2=font.render("赤兔",True,[255,255,255])
        text3=font.render("飛電",True,[0,0,0])
        screen.blit(text1,[x1-70,10])
        screen.blit(text2,[x2-70,120])
        screen.blit(text3,[x3-70,230])
        pygame.display.update()
        if x1>=900 and x2>=900 and x3>=900:
            time.sleep(0.5)
            break
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                running= False 
    pygame.quit() 
    result()

#結果呈現    
def result():
    global frame2,frame3,money,ss1,ss2,ss3,s1,s2,s3,n1,n2,n3,winner
    initGame()
    frame2=tkinter.Frame(win)
    frame2.pack() 
    bet0=tkinter.Label(frame2,text="")
    bet00=tkinter.Label(frame2,text="您的下注：")
    bet1=tkinter.Label(frame2,text="絕塵："+str(m1))
    bet2=tkinter.Label(frame2,text="赤兔："+str(m2))
    bet3=tkinter.Label(frame2,text="飛電："+str(m3))
    bet4=tkinter.Label(frame2,text="")
    bet0.grid(row=0,column=0)
    bet00.grid(row=1,column=0)
    bet1.grid(row=2,column=0)
    bet2.grid(row=3,column=0)
    bet3.grid(row=4,column=0)
    bet4.grid(row=5,column=0)

    frame3=tkinter.Frame(win)
    frame3.pack()
    h1=tkinter.Label(frame3,text="絕塵：")
    h2=tkinter.Label(frame3,text="赤兔：")
    h3=tkinter.Label(frame3,text="飛電：")
    
    spe0=tkinter.Label(frame3,text="奔馳速率(m/s)")
    spe1=tkinter.Label(frame3,text=ss1)
    spe2=tkinter.Label(frame3,text=ss2)
    spe3=tkinter.Label(frame3,text=ss3)
    
    dis0=tkinter.Label(frame3,text="奔馳距離(m)")
    dis1=tkinter.Label(frame3,text=s1)
    dis2=tkinter.Label(frame3,text=s2)
    dis3=tkinter.Label(frame3,text=s3)
    
    tim0=tkinter.Label(frame3,text="奔馳秒數(s)")
    tim1=tkinter.Label(frame3,text=n1)
    tim2=tkinter.Label(frame3,text=n2)
    tim3=tkinter.Label(frame3,text=n3)
    
    wi1=tkinter.Label(frame3,text="贏的是：",height=3)
    wi2=tkinter.Label(frame3,text=winner,height=3)
    wi3=tkinter.Label(frame3,text="您現在擁有",height=3)
    wi4=tkinter.Label(frame3,text=money,height=3)
    
    spe0.grid(row=0,column=1)
    dis0.grid(row=0,column=2)
    tim0.grid(row=0,column=3)
    h1.grid(row=1,column=0)
    spe1.grid(row=1,column=1)
    dis1.grid(row=1,column=2)
    tim1.grid(row=1,column=3)
    h2.grid(row=2,column=0)
    spe2.grid(row=2,column=1)
    dis2.grid(row=2,column=2)
    tim2.grid(row=2,column=3)
    h3.grid(row=3,column=0)
    spe3.grid(row=3,column=1)
    dis3.grid(row=3,column=2)
    tim3.grid(row=3,column=3)
    wi1.grid(row=4,column=0)
    wi2.grid(row=4,column=1)
    wi3.grid(row=5,column=0)
    wi4.grid(row=5,column=1)
    again()

#結束或繼續
def again():
    global frame6,control2,money
    frame6=tkinter.Frame(win)
    frame6.pack()
    if money>0:
        button4=tkinter.Button(frame6,text="繼續",width=15,command=play)
        button4.grid(row=0,column=1)
        button5=tkinter.Button(frame6,text="重新",width=15,command=initMoney)
        button5.grid(row=0,column=2) 
        button6=tkinter.Button(frame6,text="離開",width=15,command=end)
        button6.grid(row=0,column=3)         
    else:
        button5=tkinter.Button(frame6,text="重新",width=15,command=initMoney)
        button5.grid(row=0,column=1)
        button6=tkinter.Button(frame6,text="離開",width=15,command=end)
        button6.grid(row=0,column=2)   
    control2=1    
   
#主程式
initGame()
initMoney()
win.mainloop()
