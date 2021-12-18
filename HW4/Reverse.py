#  File: Reverse.py
#  Description: Reverses a four-digit number with no zeros and prints it
#
#  Date Created: 2/7 11:21AM
#  Date Last Modified: 2/8 1:50PM

def main():

    # Ask User four-digit number with no zeros
    givenNum = int(input("Enter an integer: "))

    #Slicing last digits off
    lastNum = givenNum % 10
    givenNum = givenNum // 10
    
    thirdNum = givenNum % 10
    givenNum = givenNum // 10

    secondNum = givenNum % 10
    givenNum = givenNum // 10
    
    firstNum = givenNum % 10
    givenNum = givenNum // 10

    #putting digits back together
    revNum = (lastNum * 1000) + (thirdNum * 100) + (secondNum * 10) + (firstNum)
    

    print("The reversed number is:", revNum,end="")
    print(".")
    
main()
