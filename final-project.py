#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 16:18:57 2018

@author: yufanyeh
"""

#分鐘轉小時
def hour(h):
    print(h//60,"小時",h%60,"分鐘")
    return h//60,'小時',h%60,'分鐘'
#檢查小時
def check_hr(hr):
    while hr>=24 or hr<0:
        hr=int(input("請輸入0-23 小時: "))
#檢查分鐘
def check_min(m):
    while m>=60 or m<0:
        m=int(input("請輸入0-59分鐘: "))
#檢查範圍
def rangecheck(x):
    while x>5 or x<1:
        x=int(input('請輸入1-5： '))
#intro
print("此程式會計算您的睡眠效率")
print("請以24小時制輸入(如23:00)")
n=int(input("How many days do you want to calculate? "))
t=1
a=[]
b=[]
c=[]
d=[]
et=[]
r=[]
avgs=0
while t<=n:
    #前一晚上床時間 A
    ah=int(input("請輸入前晚上床時間(小時): ")) #ah represents hour
    check_hr(ah)
    am=int(input("請輸入前晚上床時間(分鐘): ")) #am represents minute
    check_min(am)
    at=ah*60+am #時間轉換 t for total
    a.append(at)
    #多久入睡 B
    bh=int(input("多久入睡(小時): "))
    check_hr(bh)
    bm=int(input("多久入睡(分鐘): "))
    check_min(bm)
    bt=bh*60+bm
    b.append(bt)
    #醒來時間 C
    ch=int(input("醒來時間(小時): "))
    check_hr(ch)
    cm=int(input("醒來時間(分鐘): "))
    check_min(cm)
    ct=ch*60+cm
    c.append(ct)
    #起床時間 D
    dh=int(input("起床時間(小時): "))
    check_hr(dh)
    dm=int(input("起床時間(分鐘): "))
    check_min(dm)
    dt=dh*60+dm
    d.append(dt)
    #睡多久 E=C-A-B
    if at>ct:
        ct=ct+1440
    e=ct-at-bt
    print("\n您睡了:")
#    hour(e)
    et.append(hour(e))
    #臥床時間 F=D-A
    if at>dt:
        dt=dt+1440
    f=dt-at
    print("您的臥床時間為:")
    hour(f)
    #睡眠效率 睡著時間E/臥床時間F
    rate=e/f*100
    g=float(format(rate,'.2f'))
    avgs+=g
    r.append(g)
    print('睡眠效率為: ',g)
    t+=1
#print(a,b,c,d)
print("\n每天睡的紀錄:",et)
print("您的睡眠效率紀錄為:",r)
x=avgs/n
print('睡眠效率的平均為:',x)
#效率的好壞
if 92<=x<=100:
    print("睡眠效率: 好")
elif 85<=x<92:
    print("睡眠效率: 可")
else:
    print("睡眠效率: 差")

#睡眠品質    
print('\n接著來分析你的睡眠品質')    

f = 1
sleep_sum = 0
awake_sum = 0
print("睡眠品質分為: 1.非常差 2.不好 3.還可以 4.很好 5.非常好")
print("覺醒程度分為: 1.非常想睡 2.有點想睡 3.不想睡但不清醒 4.清醒 5.非常清醒")
while f <= n:
    sleep_quality = int(input('請輸入睡眠品質(1-5)：'))
    rangecheck(sleep_quality)
    awake_quality = int(input('請輸入覺醒程度(1-5):'))
    rangecheck(awake_quality)
    f = f+1
    sleep_sum = sleep_sum + sleep_quality
    awake_sum = awake_sum + awake_quality
    
sleep_avg = sleep_sum/n
awake_avg = awake_sum/n
#睡眠品質與覺醒程度的好壞(平均值)
if sleep_avg >= 1.0 and sleep_avg <= 2.0:
    print('睡眠品質有點差')
elif sleep_avg >= 2.1 and sleep_avg <= 4.0:
    print('睡眠品質還可以')
else:
    print('睡眠品質很好')
    
if awake_avg >= 1.0 and awake_avg <= 2.0:
    print('覺醒程度有點差')
elif awake_avg >= 2.1 and awake_avg <= 4.0:
    print('覺醒程度還可以')
else:
    print('覺醒程度很好')
    
#運動量計算  
print('接著分析你的運動狀態')
sports_day = int(input('請輸入一週幾天運動：'))
minute_sum = 0
g = 1
personal_record = []
while g <= sports_day:
    #先輸入小時再輸入分鐘
    hour = int(input('請輸入一天的運動量(小時)：'))
    minute = int(input('請輸入一天的運動量(分鐘)：'))
    final_min = hour*60 + minute
    minute_sum = minute_sum + final_min
    #將每天的運動量輸入到 personal_record
    personal_record.append(final_min)
    g = g+1
avg = float(format(minute_sum/sports_day,'.2f'))
print('這',g-1,'天的運動時間分別為：',personal_record)
print('平均每天運動量為:',avg,'分鐘')
if avg < 30:
    print('運動量不足')
elif avg >= 30 and avg <60:
    print('達到標準運動量')
else:
    print('運動量充足')
