# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
yes=True
while yes:
    import random
    num=random.randint(1,99)
    flag=True

#intro
    print("The purpose of this exerise is to enter a number of coin values")
    print("that add up to a diplayed target value.")
    print("\nEnter coins value as 1-penny, 5-nickel, 10-dime and 25-quarter.")
    print("Hit return after the last entered coin value.")
    print("-----------")
#game

    print("Enter coins that add up to",num,"cents, one per line.")
    money=[1,5,10,25]
    #first coin
    coin=int(input("\nEnter first coin: "))
    if coin not in money:
        print("Invalid entry")
    else:
        coinsum=coin 
    #next coin
    while coinsum<= num and flag:
        ncoin=input("Enter next coin: ") #ncoin represents next coin
        if ncoin== "":
            flag=False
        else:
            nextcoin=int(ncoin)
            if nextcoin not in money:
                print("\nInvalid entry")
            else:
                coinsum=coinsum+nextcoin
    if coinsum<num:
        print("\nSorry - you only entered",coinsum,"cents.")
    elif coinsum>num:
        print("\nSorry - total amount exceeds",num,"cents.")
    elif coinsum==num:
        print("Correct!")
    
#ask to play again
    again=input('Try again(y/n)? ')
    while again!='y' and again!='n':
        again=input("Please enter y or n: ")
    if again=='n': #if player says no
            yes=False
print("\nThanks for playing ... goodbye")
            
