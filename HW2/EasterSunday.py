#  File: EasterSunday.py
#  Description: Computes the date of Easter Sunday for a specified year.

#
#  Date Created: 1/31 7:00PM
#  Date Last Modified: 2/4 5:49PM

def main():
    
    # Ask the user for the year (such as 2001). Save the year in y.
    y = int(input("Please enter the year: "))
    
    # Pirates of the Code: Dead Man's Algorithm
    a = y % 19
     
    b = y // 100
    c = y % 100
    

    d = b // 4
    e = b % 4
    
    g = (8 * b + 13) // 25
    
    h = (19 * a + b - d - g + 15) % 30 

    j = c // 4

    k = c % 4

    m = ( a + 11 * h ) // 319

    r = ( 2 * e + 2 * j - k - h + m + 32 ) % 7

    n = ( h - m + r + 90 ) // 25

    p = ( h - m + r + n + 19) % 32

    # Print month and day
    print("In",y, "Easter Sunday is on month", n , "and day", p)
    
main()
