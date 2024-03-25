# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

name = input("請輸入你的暱稱:")
month = int(input("請輸入你的出生月份:"))
date = int(input("請輸入你的出生日期:"))
if(month==1 and date >=21)or(month==2 and date <=20):
    print("Hi,",name,". 你是水瓶座")
elif(month==2 and date >=21)or(month==3 and date <=20):
    print("Hi,",name,". 你是雙魚座")
elif(month==3 and date >=21)or(month==4 and date <=20):
    print("Hi,",name,". 你是牡羊座")
elif(month==4 and date >=21)or(month==5 and date <=20):
    print("Hi,",name,". 你是金牛座")
elif(month==5 and date >=21)or(month==6 and date <=20):
    print("Hi,",name,". 你是雙子座")
elif(month==6 and date >=21)or(month==7 and date <=20):
    print("Hi,",name,". 你是巨蟹座")
elif(month==7 and date >=21)or(month==8 and date <=20):
    print("Hi,",name,". 你是獅子座")
elif(month==8 and date >=21)or(month==9 and date <=20):
    print("Hi,",name,". 你是處女座")
elif(month==9 and date >=21)or(month==10 and date <=20):
    print("Hi,",name,". 你是天秤座")
elif(month==10 and date >=21)or(month==11 and date <=20):
    print("Hi,",name,". 你是天蠍座")
elif(month==11 and date >=21)or(month==12 and date <=20):
    print("Hi,",name,". 你是射手座")
elif(month==12 and date >=21)or(month==1 and date <=20):
    print("Hi,",name,". 你是魔羯座")
