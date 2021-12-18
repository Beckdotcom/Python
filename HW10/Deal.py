#  File: Deal.py
#  Description: simulate the game and demonstrate that Marilyn vos Savant did

#
#  Date Created: 3/17 09:16PM
#  Date Last Modified: 3/21 09:31PM

import random


def roll(n): #return random number

    number = random.randint(1,n)

    return number

def runOneTrial(): #steps 3 to 7, return "win" or "lose", print

    #roll random numbers
    result = ""
    prize = roll(3)#step 3, random number
    guess = roll(3)#step 4, random number
    view = roll(3)#step 5, random number
    newGuess = roll(3)
    
    #step 5:can't be same
    while view == prize or view == guess:
        view = roll(3)

    #step 6:player switches
    while newGuess == guess or newGuess == view:
        newGuess = roll(3)

    print( "   " + format(prize,"^5d") + format(guess,"^9d")+
           format(view,"^5d")+ format(newGuess,"^13d"))

    #step 7:return win or lose, increment in main
    if newGuess == prize: 
        result = "win"
    else:
        result = "lose"
            
    return result 

def main():

    trials = int(input("   How many trials do you want to run? "))
    switchWin = 0
    
    print("")
    print("   Prize  "+"Guess  "+"View  "+"New Guess  ")

    #run trial x times
    for i in range(1,trials+1): 

        result = runOneTrial()

        if result == "win":
            switchWin+=1

        
    
    #print out possibility
    possibility = switchWin/trials
    print("")
    print("   Probability of winning if you switch =",format(possibility,"4.2f"))
    print("   Probability of winning if you do not switch =", format(1 - possibility,"4.2f"))
        
     
main()
