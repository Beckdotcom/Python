#  File: DayOfTheWeek.py
#  Description: print out the day of the week for prompted date.

#
#  Date Created: 2/19 07:35PM
#  Date Last Modified: 2/20 10:11PM

def main():

    #Ask for input
    year = int(input("Please enter the year (an integer): "))

    month = input("Please enter the month (a string): ")

    b = int(input("Please enter the day (an integer): "))

    date = " "

    #Zeller's Congruence
    if( month == "January"):
        a = 11
        year -=1

    elif( month == "February"):
        a = 12
        year -=1

        
    elif( month == "March"):
        a = 1
        
        
    elif( month == "April"):
        a = 2
        
    elif( month == "May"):
        a = 3
        
    elif( month == "June"):
        a = 4
        
    elif( month == "July"):
        a = 5

    elif( month == "August"):
        a = 6
            
    elif( month == "September"):
        a = 7
        
    elif( month == "October"):
        a = 8
        
    elif( month == "November"):
        a = 9
        
    elif( month == "December"):
        a = 10

    c = year % 100

    d = year // 100

    w = (13 * a - 1 ) // 5

    x = c // 4

    y = d // 4

    z = w + x + y + b + c - 2 * d

    r = z % 7

    r = (r + 7) % 7

    #r gives the day
    if( r == 0):
        date = "Sunday"

    elif( r == 1):
        date = "Monday"
        
    elif( r == 2):
        date = "Tuesday"
        
    elif( r == 3):
        date = "Wednesday"
        
    elif( r == 4):
        date = "Thursday"
        
    elif( r == 5):
        date = "Friday"
        
    elif( r == 6):
        date = "Saturday"

    #Print out date
    print("The day of the week is", date, end=".")
    
          
main()
