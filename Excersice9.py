import random
import sys

bingo = 0

while True:
    mygeus = int(input("please take a guess between 1 to 9: "))
    choosed_num = random.randint(1,9)
    if choosed_num == mygeus:
        print ("Bingo you got it")
        bingo = bingo + 1
        q = input("Do you like to continue gussing? (y/n) ")
    if mygeus > choosed_num:
        print ("Too big")
        q = input("Do you like to continue gussing? (y/n) ")
    elif mygeus < choosed_num:
        print ("Too small")
        q = input("Do you like to continue gussing? (y/n) ")

    if q == "y":
        continue
        #print ("Lets try again.")
    else:
        print ("you managed to guess: " , bingo , "times")
        break
            