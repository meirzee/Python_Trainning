import random
import sys

play = "yes"
count = 0
flow = ""

while play == "yes":

    p1 = input("Select Rock , paper or scissors: ")
    options = ['ROCK', 'PAPER','SCISSORS' ]

    print ("\nYou choosed: ", p1.upper() )
    p2 = (random.choice (options))
    print ("Player two choosed: ", p2)

    p1 = p1.upper()
    p2 = p2.upper()

    print ("count is : " , count)    #to be deleted
    
    if p1 not in options and count <= 3:
        print ("Not a valid option!, please try again..")
        count = count + 1
        flow = 'restart'
    else:
        count = 0
    
    if count > 3:
        sys.exit("You choosed wrong options for more then 3 times.. Exiting the game")
        
        
    if flow != 'restart':
        if p1 == p2:
                print("It is a tie , No one wins.")
        elif (p1 == 'ROCK' and p2 == 'SCISSORS'):
                print ("You win..")
        elif (p1 == 'ROCK' and p2 == 'PAPER'):
                print ("player two win..")
        elif (p1 == 'PAPER' and p2 == 'ROCK'):
                print ("You win..")
        elif (p1 == 'PAPER' and p2 == 'SCISSORS'):
                print ("player two win..")
        elif (p1 == 'SCISSORS' and p2 == 'PAPER'):
                print ("You win..")
        elif (p1 == 'SCISSORS' and p2 == 'ROCK'):
                print ("player two win..")
        play = input("Do you want to play again? yes/no: ")