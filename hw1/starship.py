# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random

mypw=input("請輸入密碼:")
while mypw!= "123":
    print("密碼錯誤!")
    mypw=input("請輸入密碼:")
print("歡迎艦長!")

while True:
    mycom=input("請輸入命令 a前進 b瞬移 c偵測 d射擊 e離開:")
    if mycom == "a":
        mycom=input("請問以以曲速幾級前進 1 or 2:")
        if mycom == "1":
            print("艦長!目前已使用曲速一級前進中...")
        elif mycom == "2":
            print("艦長!目前已使用曲速二級前進中...")
        else:
            print("辨識失敗!")
            
    elif mycom=='b':
        print('瞬移了')
        
    elif mycom=='c':
        x=random.randint(0,1)
        if x==0:
            print('遇到壞人')
        else:
            print('遇到好人')
            
    elif mycom=='d':
        mycom=input('加農砲1 或 原子光束2: ')
        x=random.randint(0,1)
        if mycom=='1':
            print('使用加農砲...')
            if x==0:
                print('攻擊成功')
            else:
                print('攻擊失敗')
        elif mycom=='2':
            print('使用原子光束...')
            if x==0:
                print('攻擊成功')
            else:
                print('攻擊失敗')
        else:
            print('辨識失敗')
            
    elif mycom=='e':
        break
    
    else:
        print('辨識失敗')
    
print('掰掰')