import random
money = 9
plays = 1

while True:
    print ("You have", money, "monies")
    print ()
    whichcard = input("Which card you you want to buy? (2 monies, 10 monies, or 100 monies)?: ")
    if whichcard == "2":
        moneycheck = money
        numberofpick = 10
        numberofcell = 10
        highesttrip1 = 15
        highesttrip2 = 14
        triplet1 = random.randint(0, highesttrip1)
        triplet2 = random.randint(0, highesttrip2)
        triplet3 = random.randint(0, highesttrip2)
        while True:
            if triplet2 == triplet1:
                triplet2 = random.randint(0, highesttrip2)
            else:
                break
        while True:
            if triplet3 == triplet1:
                triplet3 = random.randint(0, highesttrip2)
            elif triplet3 == triplet2:
                triplet3 = random.randint(0, highesttrip2)
            else:
                break
        triplet = [triplet1, triplet1, triplet1, triplet2, triplet2, triplet2, triplet3, triplet3, triplet3]
        winningcombinations = ["A0", "B0", "C0", "D0", "E0", "A1", "B1", "C1", "D1", "A3", "B3", "C3", "A5", "B5", "A10", "A100"]
        wincheck = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        numoftrip = 3
        moneyprize1 = 6
        moneyprize2 = 10
        moneyprize3 = 13
        moneyprize4 = 15
        moneyprizeamount1 = 0
        moneyprizeamount2 = 1
        moneyprizeamount3 = 3
        moneyprizeamount4 = 5
        moneyprizeamount5 = 10
        moneyprizeamount6 = 100
        def cardplay():
            global numberofpick
            global numberofcell
            global randomlist
            global cellboardnum
            global numoftrip
            global wincheck
            global triplet
            global select
            global winningcombinations
            global moneyprize1
            global money
            global moneyprize2
            global moneyprize3
            global moneyprize4
            global moneycheck
            global i
            global cell1
            global cell2
            global cell3
            global cell4
            global cell5
            global cell6
            global cell7
            global cell8
            global cell9
            global pick1
            global pick2
            global pick3
            global pick4
            global pick5
            global pick6
            global pick7
            global pick8
            global pick9
            global moneyprizeamount1
            global moneyprizeamount2
            global moneyprizeamount3
            global moneyprizeamount4
            global moneyprizeamount5
            global moneyprizeamount6
            for i in range(numberofpick):
                globals()["pick" + str(i)] = 0
            select = 1
            for i in range(numberofcell):
                globals()["cell" + str(i)] = "X"
            randomlist = random.sample(range(1, numberofcell), numberofcell-1)
            while True:
                cellboardnum = 0
                for i in range (numoftrip):
                    print(globals()["cell" + str(cellboardnum + 1)], " ", globals()["cell" + str(cellboardnum + 2)], " ", globals()["cell" + str(cellboardnum + 3)])
                    cellboardnum = cellboardnum + 3
                if wincheck[triplet[randomlist[int(select)-1]-1]-1] == 3:
                    print ()
                    print ("Winner!")
                    print ("You won with", winningcombinations[triplet[randomlist[int(select)-1]-1]-1])
                    if (triplet[randomlist[int(select)-1]-1] < moneyprize1):
                        if winningcombinations[triplet[randomlist[int(select)-1]-1]-1] == "A100":
                            money = money + moneyprizeamount6
                        else:
                            money = money + moneyprizeamount1
                    elif (moneyprize2 > triplet[randomlist[int(select)-1]-1] > moneyprize1):
                        money = money + moneyprizeamount2
                    elif (moneyprize3 > triplet[randomlist[int(select)-1]-1] > moneyprize2-1):
                        money = money + moneyprizeamount3
                    elif (moneyprize4 > triplet[randomlist[int(select)-1]-1] > moneyprize3-1):
                        money = money + moneyprizeamount4
                    elif triplet[randomlist[int(select)-1]-1] == moneyprize4:
                        money = money + moneyprizeamount5
                    else:
                        money = money + moneyprizeamount1
                    print ("And earned ", money - moneycheck , "monies")
                    break
                while True:
                    select = (input("Which cell do you want to reveal? (1-"+ str(numberofcell-1) +"): "))
                    try:
                        int(select)
                    except ValueError:
                        print ("This is not a valid value.")
                        print ()
                        select = 1
                    if globals()["pick" + str(select)] == 0:
                        globals()["cell" + str(select)] = winningcombinations[triplet[randomlist[int(select)-1]-1]-1]
                        globals()["pick" + str(select)] = globals()["pick" + str(select)] + 1
                        break
                    else:
                        print ("You already picked this value.")
                        print ()
                wincheck[triplet[randomlist[int(select)-1]-1]-1] = wincheck[triplet[randomlist[int(select)-1]-1]-1] + 1
        cardplay()
        replay = input("Do you want to play again? (Y or N): ")
        if replay == "N":
            print ("You ended with", money, "monies")
            print ("You played", plays ,"times")
            break
        plays = plays + 1
        money = money - 2
        if (money <= 0):
            print ("You ran out of monies")
            print ("You played", plays ,"times")
            break
        print ()
    if whichcard == "10":
        if (money < 10):
            print ("You don't have enough money, try again")
            print ()
        else:
            moneycheck = money
            numberofpick = 13
            numberofcell = 13
            highesttrip1 = 15
            highesttrip2 = 14
            triplet1 = random.randint(0, highesttrip1)
            triplet2 = random.randint(0, highesttrip2)
            triplet3 = random.randint(0, highesttrip2)
            triplet4 = random.randint(0, highesttrip2)
            while True:
                if triplet2 == triplet1:
                    triplet2 = random.randint(0, highesttrip2)
                else:
                    break
            while True:
                if triplet3 == triplet1:
                    triplet3 = random.randint(0, highesttrip2)
                elif triplet3 == triplet2:
                    triplet3 = random.randint(0, highesttrip2)
                else:
                    break
            while True:
                if triplet4 == triplet1:
                    triplet4 = random.randint(0, highesttrip2)
                elif triplet4 == triplet2:
                    triplet4 = random.randint(0, highesttrip2)
                elif triplet4 == triplet3:
                    triplet4 = random.randint(0, highesttrip2)
                else:
                    break
            triplet = [triplet1, triplet1, triplet1, triplet2, triplet2, triplet2, triplet3, triplet3, triplet3, triplet4, triplet4, triplet4]
            winningcombinations = ["A2", "B2", "C2", "A5", "B5", "C5", "A10", "B10", "C10", "D10", "A25", "B25", "C25", "D25", "A75", "A250"]
            wincheck = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            numoftrip = 4
            moneyprize1 = 4
            moneyprize2 = 7
            moneyprize3 = 11
            moneyprize4 = 15
            moneyprizeamount1 = 2
            moneyprizeamount2 = 5
            moneyprizeamount3 = 10
            moneyprizeamount4 = 25
            moneyprizeamount5 = 75
            moneyprizeamount6 = 250
            cardplay()
            replay = input("Do you want to play again? (Y or N): ")
            if replay == "N":
                print ("You ended with", money, "monies")
                print ("You played", plays ,"times")
                break
            plays = plays + 1
            money = money - 10
            if (money <= 0):
                print ("You ran out of monies")
                print ("You played", plays ,"times")
                break
            print ()
    if whichcard == ("100"):
        if (money < 100):
            print ("You don't have enough money, try again")
            print ()
        else:
            moneycheck = money
            numberofpick = 16
            numberofcell = 16
            highesttrip1 = 15
            highesttrip2 = 14
            triplet1 = random.randint(0, highesttrip1)
            triplet2 = random.randint(0, highesttrip2)
            triplet3 = random.randint(0, highesttrip2)
            triplet4 = random.randint(0, highesttrip2)
            triplet5 = random.randint(0, highesttrip2)
            while True:
                if triplet2 == triplet1:
                    triplet2 = random.randint(0, highesttrip2)
                else:
                    break
            while True:
                if triplet3 == triplet1:
                    triplet3 = random.randint(0, highesttrip2)
                elif triplet3 == triplet2:
                    triplet3 = random.randint(0, highesttrip2)
                else:
                    break
            while True:
                if triplet4 == triplet1:
                    triplet4 = random.randint(0, highesttrip2)
                elif triplet4 == triplet2:
                    triplet4 = random.randint(0, highesttrip2)
                elif triplet4 == triplet3:
                    triplet4 = random.randint(0, highesttrip2)
                else:
                    break
            while True:
                if triplet5 == triplet1:
                    triplet5 = random.randint(0, highesttrip2)
                elif triplet5 == triplet2:
                    triplet5 = random.randint(0, highesttrip2)
                elif triplet5 == triplet3:
                    triplet4 = random.randint(0, highesttrip2)
                elif triplet5 == triplet4:
                    triplet5 = random.randint(0, highesttrip2)
                else:
                    break
            triplet = [triplet1, triplet1, triplet1, triplet2, triplet2, triplet2, triplet3, triplet3, triplet3, triplet4, triplet4, triplet4, triplet5, triplet5, triplet5]
            winningcombinations = ["A10", "B10", "C10", "D10", "A50", "B50", "C50", "A100", "B100", "C100", "D100", "A250", "B250", "C250", "A500", "A3333"]
            wincheck = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            numoftrip = 5
            moneyprize1 = 5
            moneyprize2 = 8
            moneyprize3 = 12
            moneyprize4 = 15
            moneyprizeamount1 = 10
            moneyprizeamount2 = 50
            moneyprizeamount3 = 100
            moneyprizeamount4 = 250
            moneyprizeamount5 = 500
            moneyprizeamount6 = 3333
            cardplay()
            replay = input("Do you want to play again? (Y or N): ")
            if replay == "N":
                print ("You ended with", money, "monies")
                print ("You played", plays ,"times")
                break
            plays = plays + 1
            money = money - 100
            if (money <= 0):
                print ("You ran out of monies")
                print ("You played", plays ,"times")
                break
            print ()