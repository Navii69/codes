var,cash,var2=1,250,2
bjval=['2','2','2','2','3','3','3', '3','4','4','4', '4','5','6','7','8','9', '10','J','K','Q', 'A']
bjfaceval=['J','K','Q']
player=None
bot=None
player_ace,bot_ace=0,0
import random
from rich import print
print("[#A1045A]Welcome to BlackJack[/#A1045A]")
#USER DEFINED FUNCTIONS_______________________________________
def cardsshow(a):
    print("Dealer-\nCards: ")
    for i in range(0,a):
        print(bot[i],end=' ')
    print("\nTotal: ",botpoints)
    print("______________")
    print("You-\nCards: ")
    for j in range(0,a):
        print(player[j],end=' ')
    print("\nTotal: ",playerpoints)
    
#_____________________________________________________
def cards(a):
    print("[#d279a6]Dealer-\nCards: \n[/#d279a6]",bot[0],"?"*(a-1))
    print("[#d279a6]Total: ?[/#d279a6]")
    print("______________")
    print("[#FFB6C1]You-\nCards: [/#FFB6C1]")
    for j in range(0,a):
        print(player[j],end=' ')
    print("[#FFB6C1]\nTotal: [/#FFB6C1]",playerpoints)
#_____________________________________________________
def stand():
        print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
        global cash
        if playerpoints>botpoints:
            print("YOU WON")
            cash+=cash_to_bid*2
            print("Your cash now is",cash)
        elif playerpoints<botpoints:
            print("YOU LOST")
            print("Your cash now is",cash)
        else:
            print("TIED")
            cash+=cash_to_bid
            print("Your cash now is",cash)
#__________________________________________
def situation():
        global cash,con
        if playerpoints==21:
            print("YOU WON")
            cash+=cash_to_bid*2
            print("Your cash now is",cash)
            con=1
        elif playerpoints>21:
            print("YOU LOST")
            print("Your cash now is",cash)
            con=1
        elif botpoints==21:
            print("YOU LOST")
            print("Your cash now is",cash)
            con=1
        elif botpoints>21:
            print("YOU WON")
            cash+=cash_to_bid*2
            print("Your cash now is",cash)
            con=1
#__________________________________________
def points():
        global player_ace,bot_ace,botpoints,playerpoints
        if player.count('A')>1:
            player_ace+=1
        elif player_ace==0 and 'A' in player:
            player_ace+=1
        elif bot.count("A")>1:
            bot_ace+=1
        elif bot_ace==0 and "A" in bot:
            bot_ace+=1
        botpoints,playerpoints=0,0
        for i in bot:
            if i in bjfaceval:
                botpoints+=10
            elif i=="A":
                continue
            else:
                botpoints+=int(i)
        botpoints+=bot_ace
        for j in player:
            if j in bjfaceval:
                playerpoints+=10
            elif j=='A':
                continue
            else:
                playerpoints+=int(j)
        playerpoints+=player_ace
#_____________________________________________
def res():
    global var,var2
    restart=int(input("Do you wanna play again\nWrite 1 for YES and 2 for NO: "))
    if restart==1:
        var2=1
    elif restart==2:
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\nHave a great time\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        var=2
        pass
#START_______________________________________________________
while var==1:
    var2,con=2,0
    random.shuffle(bjval)
    bjstartmenu=int(input('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n1.Start\n2.View Cash\n3.Exit\nEnter you choice: '))
    if bjstartmenu==3:
        print("Have a great time")
        break
#_________________________________________________________________
    elif bjstartmenu==2:
        print('You have', cash)
        continue
#________________________________________________________________
    elif bjstartmenu==1:
        cash_to_bid=int(input("Enter the amount you wanna bid: "))
        if cash_to_bid>cash:
            print("You dont have enough cash")
            continue
        elif cash_to_bid<125:
            print("Minimum value to bid is  125")
            continue
        else:
            cash-=cash_to_bid
#RANDOM CARDS DISTRIBUTION FIRST PHASE____________________
            while var2==2:
                if var==1:
                    botpoints,playerpoints=0,0
                    player=random.sample(bjval,2)
                    bot=random.sample(bjval,2)
                    if 'A' in player:
                        player_ace=11
                    if 'A' in bot:
                        bot_ace=11
    #POINTS CALCULATION FIRST PHASE_________________________-
                    points()
                    a=2
                    cards(a)
    #SITUATION HANDLING FIRST PHASE_______________________________
                    situation()
                    if con==1:
                        cardsshow(a)
                        res()
    #FIRST CODE PHASE COMPLETED.$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                    choice=int(input("1 for Hit and 2 for Stand: "))
    #RANDOM CARD DISTRIBUTION SECOND PHASE__________________________
                    if choice==1:
                        player.append(random.choice(bjval))
                        bot.append(random.choice(bjval))
    #POINTS CALCULATION SECOND PHASE___________________________________
                        points()
                        a=3
                        cards(a)
    #SITUATION HANDLING SECOND PHASE____________________________
                        situation()
                        if con==1:
                            cardsshow(a)
                            res()
    #SECOND PHASE CODE COMPLETED________________________________
                        choice_second=int(input("Press 1 to Hit and 2 to Stand: "))
    #THIRD PHASE CODE_________________________________________________
                        if choice_second==1:
                            player.append(random.choice(bjval))
                            bot.append(random.choice(bjval))
    #POINTS CALCULATION THRID PHASE_____________________________________
                            points()
                            a=4
                            cards(a)
    #SITUATION HANDLING THIRD PHASE___________________________________
                            situation()
                            if con==1:
                                cardsshow(a)
                                res()
    #THIRD PHASE CODE COMPLETED_____________________________
                            choice_third=int(input("Press 1 to Hit and 2 to Stand: "))
    #FOURTH PHASE CODE_________________________________________________
                            if choice_third==1:
                                player.append(random.choice(bjval))
                                bot.append(random.choice(bjval))
    #POINTS CALCULATION FOURTH PHASE_______________________________________
                                points()
                                a=5
                                cards(a)
    #SITUATION HANDLING_________________________________________________
                                situation()
                                if con==1:
                                    cardsshow(a)
                                    res()
    #FOURTH PHASE COMPLETED_________________________________________
                                choice_fourth=int(input("Press 2 to Stand and 0 to Fofeit"))
    #STAND SITUATION(FOURTH PHASE)_________________________________________
                                if choice_fourth==2:
                                    stand()
                                    a=5
                                    cardsshow(a)
                                    res()
                                if choice_fourth==0:
                                    print("Dealer took all your money LOL")
                                    res()
    #STAND SITUATION(THIRD PHASE)__________________________________
                            elif choice_third==2:
                                stand()
                                a=4
                                cardsshow(a)
                                res()
    #STAND SITUATION(SECOND PHASE)____________________________________
                        elif choice_second==2:
                                stand()
                                a=3
                                cardsshow(a)
                                res()
    #STAND SITUATION(FIRST PHASE)___________________
                    elif choice==2:
                            stand()
                            a=2
                            cardsshow(a)
                            res()