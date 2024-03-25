# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
e=100 #energy
s=0 #star
hp=10
def stats():
    print("目前有",e,"點能量")
    print("現在有",s,"顆星星")
    print("現在有",hp,"HP")
def gameover():
    if e<=0:
        print("能量不夠, GAME OVER")
    elif hp<=0:
        print("HP不夠, GAME OVER")
    elif s>=10:
        print("恭喜您! 成功達成遊戲目的!")

    
print("歡迎艦長, 你有100點能量, 10HP")
print("遊戲目的: 拿到10顆星星")


while True:
    mycom=input("請輸入命令 a前進 b偵測 c看數據 d離開:")
    if mycom == "a":
        print("曲速一級 -5能量, 曲速二級-10能量, 瞬移-15能量")
        ans=input("是否繼續聽說明? (y/n): ")
        while ans!="y" and ans!="n":
            ans=input("是否繼續聽說明? (y/n): ")
        if ans=='y':
            print("用曲速一級可提高偵測星球機率\n")
            print("用曲速二級可提升偵測生命機率\n")
            print("用瞬移逃脫黑洞和危險引力")
            
        mycom=input("請輸入命令 1曲速一級 2曲速二級 3瞬移: ")
        if mycom == "1":
            print("艦長!目前已使用曲速一級前進中...")
            e=e-5
            stats()
        elif mycom == "2":
            print("艦長!目前已使用曲速二級前進中...")
            e=e-10
            stats()
        elif mycom== "3":
            print("使用瞬移中...")
            chance=random.randint(0,100)
            if chance<=95:
                print("瞬移成功")
            else:
                print("瞬移失敗")
            e=e-15
            stats()
        else:
            print("辨識失敗!")
            
    elif mycom=='b':
        print('使用偵測功能')
        print('可偵測到生命或星球\n')
        x=random.randint(0,1)
        if x==0:
            print('偵測生命中...')
            y=random.randint(0,1)
            if y==0:
                print("偵測到惡意生命體")
                print("成功擊敗惡意生命體可得2顆星星")
                print("使用武器攻擊: 加農砲 或 原子光束")
                ans=input("是否聽使用說明? (y/n): ")
                while ans!="y" and ans!="n":
                     ans=input("是否聽使用說明? (y/n): ")
                if ans=='y':
                    print("加農砲 成功機率80% -15能量\n")
                    print("原子光束 成功機率 60% -10能量\n")
                weapon=input("請選擇 1.加農砲 2.原子光束: ")
                while weapon!='1' and weapon!='2':
                    weapon=input("請選擇 1.加農砲 2.原子光束: ")
                if weapon=='1':
                    hit=random.randint(1,10)
                    e=e-15
                    print("準備發射加農砲...")
                    if hit<=8:
                        print("成功擊中惡意生命體 得到兩顆星星")
                        s=s+2
                    else:
                        print("未擊中惡意生命體")
                        print("遭到惡意生命體反擊! 扣1HP")
                        hp=hp-1
                    stats()
                elif weapon=='2':
                    hit=random.randint(1,10)
                    e=e-10
                    print("準備發射原子光束...")
                    if hit<=6:
                        print("成功擊中惡意生命體 得到兩顆星星")
                        s=s+2
                    else:
                        print("未擊中惡意生命體")
                        print("遭到惡意生命體反擊! 扣1HP")
                        hp=hp-1
#                        cont=input("是否繼續挑戰? (y/n): ")
#                        while cont!='y' and cont!='n':
#                            cont=input("是否繼續挑戰? (y/n): ")  
                    stats()
            else:
                print("偵測到友善生命體")
                print("友善生命體可提供 +15能量,+1星星,或+1HP")
                reward=input("請選擇: 1.能量 2.星星 3.HP 4.都不要: ")
                while reward!='1' and reward!='2' and reward!='3' and reward!='4':
                    reward=input("請選擇: 1.能量 2.星星 3.HP 4.都不要: ")
                if reward=="1":
                    print("友善生命體提供了15能量!")
                    e=e+15
                    stats()
                elif reward=="2":
                    print("友善生命體提供了1顆星星!")
                    s=s+1
                    stats()
                elif reward=="3":
                    print("友善生命體提供了1HP!")
                    hp=hp+1
                    stats()
                else:
                    r=random.randint(0,3)
                    if r=='0':
                        print("友善生命體感到難過")
                    stats()
                    
        else:
            print('偵測星球中..')
            z=random.randint(0,1)
            if z==0:
                print("抵達安全區域")
                print("前往星球中...")
                w=random.randint(0,1)
                if w==0:
                    print("成功抵達那美克星")
                    print("那美克星人幫助您增加15能量!")
                    e=e+15
                    stats()
                else:
                    print("成功抵達賽亞星")
                    print("賽亞人幫助您增加1HP!")
                    hp=hp+1
                    stats()
            else:
                print("進入危險區域!")
                w=random.randint(0,1)
                if w==0:
                    print("快進入黑洞了!")
                    ask=input("是否使用瞬移? (y/n): ")
                    while ask!='y' and ask!='n':
                        ask=input("是否使用瞬移? (y/n): ")
                    if ask=='y':
                        print("使用瞬移中...")
                        chance=random.randint(0,100)
                        if chance<=95:
                            print("瞬移成功")
                            print("安全逃離黑洞!")
                        else:
                            print("瞬移失敗")
                            print("差點死在黑洞中, 扣1HP, 扣5能量")
                            hp=hp-1
                            e=e-5
                        e=e-15
                        stats()
                    else:
                        print("犧牲1HP, 5能量逃出黑洞")
                        hp=hp-1 
                        e=e-5
                        stats()
                else:
                    print("快進入危險引力區!")
                    ask=input("是否使用瞬移? (y/n): ")
                    while ask!='y' and ask!='n':
                        ask=input("是否使用瞬移? (y/n): ")
                    if ask=='y':
                        print("使用瞬移中...")
                        chance=random.randint(0,100)
                        if chance<=95:
                            print("瞬移成功")
                            print("安全逃離危險引力!")
                        else:
                            print("瞬移失敗")
                            print("差點死在危險引力中,扣5能量")
                            e=e-5
                        e=e-15
                        stats()
                    else:
                        print("犧牲5能量逃出危險引力")
                        e=e-5
                        stats()
                
    elif mycom=='c':
        stats()
    elif mycom=='d':
        print('掰掰')
        break
    else:
        print('辨識失誤')
