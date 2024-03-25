# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
zodiac=['魔羯座Capricorn','水瓶座Aquarius', '雙魚座Pisces', '牧羊座Aries', '金牛座Taurus', '雙子座Gemini',
              '巨蟹座Cancer', '獅子座Leo', '處女座Virgo', '天秤座Libra', '天蠍座Scorpio', '射手座Sagitarius',
             ]
aquarius='Forthright, industrius, sensitive, intellectual, sociable'
pisces='Dependable, methodical, modests, born leader, patient'
aries='Unpredictable, rebellious, passionate, daring, impulsive'
taurus='Good friend, kind, soft-spoken, cautious, artistic'
gemini='Strong, self-assured, proud, decisive, loyal'
cancer='Deep thinker, creative, responsible, calm, purposeful'
leo='Cheerful, quick-witted, perceptive, talkative, open-minded'
virgo='Sincere, sympathetic, shy, generous, mothering'
libra='Motivator, inquisitive, flexible, innovative, problem solver'
scorpio='Organized, self-assured, decisive, perfectionist, zealous'
sagitarius='Honest, unpretentious, idealist, moralistic, easy going'
capricorn='Peace-loving, hard-working, trusting, understanding, thoughtful'

characteristics=[ capricorn,aquarius, pisces, aries, taurus, gemini, cancer,
                 leo, virgo, libra, scorpio, sagitarius]

big=[1,3,5,7,8,10,12] #31 days
small=[4,6,9,11] #30 days
terminate=False
#greeting
print('This program will display your zodiac sign and associated')
print('personal characteristics.\n')

while not terminate:
    #get month of birth and date of birth
    month=int(input('Enter your month of birth: '))
    date=int(input('Enter your date of birth: '))
    
    #check month and date if correct
    while month not in (1,2,3,4,5,6,7,8,9,10,11,12):
        print("Invalid month, please re-enter\n")
        month=int(input('Enter your month of birth: '))
    if month in big:
        while date>31 or date<=0:
            print("Invalid date, please re-enter\n")
            date=int(input('Enter your date of birth: '))
    elif month in small:
        while date>30 or date<=0:
            print("Invalid date, please re-enter\n")
            date=int(input('Enter your date of birth: '))
    elif month==2:
        while date>29 or date<=0:
            print("Invalid date, please re-enter\n")
            date=int(input('Enter your date of birth: '))
    #output results
    
    if date<21:
        print('Your zodiac sign is the',zodiac[month-1],'\n')
        print('Your personal characteristics...')
        print(characteristics[month-1])
    elif date>=21:
        if month==12:
            print('Your zodiac sign is the',zodiac[0],'\n')
            print('Your personal characteristics...')
            print(characteristics[0])
        else:
            print('Your zodiac sign is the',zodiac[month],'\n')
            print('Your personal characteristics...')
            print(characteristics[month])
        
    #ask to continue
    response=input("\nWould you like to try another? (y/n): ")
    while response !='y' and response !='n':
        response=input("Please enter 'y' or 'n':")
    if response=='n':
        terminate= True
print("Thanks for playing!")
    
        
    