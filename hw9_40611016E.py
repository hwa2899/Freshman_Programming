# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 16:16:18 2017

@author: Ching
"""

zodiac=['Aquarius', 'Pisces', 'Aries', 'Taurus', 'Gemini',
              'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagitarius',
              'Capricorn']
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

characteristics=[aquarius, pisces, aries, taurus, gemini, cancer,
                 leo, virgo, libra, scorpio, sagitarius, capricorn]

big=[1,3,5,7,8,10,12] #31 days
small=[4,6,9,11] #30 days
def invalid():
    print('Invalid date, please re-enter\n')
    global date
    date=int(input('Enter your date of birth:'))
    
def results():
    print('Your zodiac sign is the',zodiac[month-1],'\n')
    print('Your personal characteristics...')
    print(characteristics[month-1])
    
def try_again():
    global response
    response=input("\nWould you like to try another? (y/n): ")
    while response !='y' and response !='n':
        response=input("Please enter 'y' or 'n':")
def check():
    if month in big:
        while date>31 or date<=0:
            invalid()
    elif month in small:
        while date>30 or date<=0:
            invalid()
    elif month==2:
        while date>29 or date<=0:
            invalid()
terminate=False
#greeting
print('This program will display your zodiac sign and associated')
print('personal characteristics.\n')

while not terminate:
    #get month of birth and date of birth
    pikachu=True
    while pikachu:
        try:
            month=input('Enter your month of birth: ')
            month=int(month)
            pikachu=False
        except ValueError:
            print('Error: ',month,'is not an integer.')
        try:
            date=input('Enter your date of birth: ')
            date=int(date)
            month=int(month)
            pikachu=False
        except ValueError:
            print('Error: ',date,'is not an integer.')
            pikachu=True
            
    #check month and date if correct
    while month not in (1,2,3,4,5,6,7,8,9,10,11,12):
        print("Invalid month, please re-enter\n")
        month=int(input('Enter your month of birth: '))
    check()
    #output results
    if date<21:
        results()
    else:
        if month==12:
            print('Your zodiac sign is the',zodiac[0],'\n')
            print('Your personal characteristics...')
            print(characteristics[0])
        else:
            results()
    #ask to continue
    try_again()
    if response=='n':
        terminate= True
print("Thanks for playing!")
    