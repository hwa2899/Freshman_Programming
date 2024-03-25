# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 11:51:47 2017

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
#print(student.columns)

stu_pos=student.groupby('position')
stpe=stu_pos.get_group('臺北市') #students in taipei, stu_taipei
students={'1':stpe['one_male']+stpe['one_female'],
          '2':stpe['two_male']+stpe['two_female'],
          '3':stpe['three_male']+stpe['three_female'],
          '4':stpe['four_male']+stpe['four_female'],
          '5':stpe['five_male']+stpe['five_female'],
          '6':stpe['six_male']+stpe['six_female'],
          '7':stpe['seven_male']+stpe['seven_female'],
          'delay':stpe['delay_male']+stpe['delay_female']}
total=pandas.DataFrame(students)
total_sum=total.sum()
print(total_sum)
plt.figure()
total_sum.plot(kind='bar',title='Students in each grade level')

#print(stu_Taipei)