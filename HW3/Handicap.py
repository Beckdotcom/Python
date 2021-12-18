#  File: Handicap.py
#  Description:
#
#  Date Created: 2/5 8:45PM
#  Date Last Modified: 10:00PM

def main():
    
    # Ask User for Game Scores
    game1 = int(input("Enter Game 1: "))
    
    game2 = int(input("Enter Game 2: "))
    
    game3 = int(input("Enter Game 3: "))

    
    # Calculate average
    avg = int((game1 + game2 + game3) / 3)

    # Calculate handicap    
    handicap = int((200 - avg) *.8)

    # Print info
    print("The bowler's average is: ", avg)
    
    print("The bowler's handicap is: ", handicap)
    
main()
