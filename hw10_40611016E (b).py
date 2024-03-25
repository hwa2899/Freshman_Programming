# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 22:47:17 2017

@author: Ching
"""
import pandas
import matplotlib.pyplot as plt
student = pandas.read_csv("stu_utf8.csv",encoding = "utf-8")
student.columns=['id','school','day_night','level',
                 'one_male','one_female',
                 'two_male','two_female',
                 'three_male','three_female',
                 'four_male','four_female',
                 'five_male','five_female',
                 'six_male','six_female',
                 'seven_male','seven_female',
                 'delay_male','delay_female',
                 'position','type']
city=['南投縣','嘉義市','嘉義縣','基隆市','宜蘭縣','屏東縣',
      '彰化縣','新北市','新竹市','新竹縣','桃園市','澎湖縣',
      '臺中市','臺北市','臺南市','臺東縣','花蓮縣','苗栗縣',
      '金門縣','雲林縣','高雄市']

stu_pos=student.groupby('position')

for i in range(21):
    a=stu_pos.get_group(city[i])
    gender={'male':a['one_male']+a['two_male']+a['three_male']+a['four_male']+a['five_male']
    +a['six_male']+a['delay_male'],'female':a['one_female']+a['two_female']+a['three_female']
    +a['four_female']+a['five_female']+a['six_female']+a['delay_female']}
    total=pandas.DataFrame(gender)
    totalsum=total.sum()
    plt.figure(figsize=(6,6))
    totalsum.plot(kind='pie',title=city[i],label='Gender',shadow=True)
    plt.figure()
    totalsum.plot(kind='bar',title=city[i])
