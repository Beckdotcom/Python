#  File: GuessingGame.py
#  Description: allows the user to play a guessing game.
#   The game will choose a "secret number", a positive integer less than 10000.
#   The user has 10 tries to guess the number.

#
#  Date Created: 2/25 02:17PM
#  Date Last Modified: 2/27 4:24PM

def main():

    secretNum = 1458
    count = 0

    #Welcome and Ask for input
    print("Welcome to the guessing game. You have ten tries to guess my number.")
    guess = int(input("Please enter your guess: "))


    #10 guesses
    while count <= 10:
        count +=1

        #guess range
        if guess <= 0 or guess >= 10000 :
            print("Your guess must be between 0001 and 9999." )
            guess = int(input("Please enter a valid guess: "))
            count-=1
        
        #first try
        elif guess == secretNum and count == 1:
            print("That's correct!" )
            print("Congratulations! You guessed it on the first try!" )
            break

        #guess right and output guesses       
        elif guess == secretNum:
            print("That's correct!" )
            print("Congratulations! You guessed it in",count,"guesses." )
            break

        #low guess
        elif guess < secretNum:
            print("Your guess is too low." )
            print("Guesses so far:",count )

            #10 guesses
            if count == 10:
                print("Game over: you ran out of guesses.")
                break
            guess = int(input("Please enter your guess: "))
    

        #high guess 
        elif guess > secretNum:
            print("Your guess is too high." )
            print("Guesses so far:",count )

            #10 guesses
            if count == 10:
                print("Game over: you ran out of guesses.")
                break
            guess = int(input("Please enter your guess: "))
            

  
          
main()
