#  File: NextDay.py
#  Description: enter a date and computes its immediate successor

#
#  Date Created: 2/15 06:45PM
#  Date Last Modified: 2/17 11:10PM

def main():
    
    #Ask for input
    year = int(input("Please enter the year: "))

    month = input("Please enter the month: ")

    day = int(input("Please enter the day: "))

    #Filter through months and change accordingly
    if( month == "January"):
        
        if day == 31:
            month = "February"
            day = 1
            
        else:
            day +=1

    elif( month == "February"):
        #divide by 100 or 400 - in textbook
        if day == 28 and (year % 4 == 0):
            day = 29

        elif day == 28 or day == 29:
            month = "March"
            day = 1
        
        else:
            day +=1
        
    elif( month == "March"):
        if day == 31:
            month = "April"
            day = 1
        else:
            day +=1
        
    elif( month == "April"):
        if day == 30:
            month = "May"
            day = 1
        else:
            day +=1
        
    elif( month == "May"):
        if day == 31:
            month = "June"
            day = 1
        else:
            day +=1
        
    elif( month == "June"):
        if day == 30:
            month = "July"
            day = 1
        else:
            day +=1
        
    elif( month == "July"):
        if day == 31:
            month = "August"
            day = 1
        else:
            day +=1

    elif( month == "August"):
        if day == 31:
            month = "September"
            day = 1
        else:
            day +=1
            
    elif( month == "September"):
        if day == 30:
            month = "October"
            day = 1
        else:
            day +=1
        
    elif( month == "October"):
        if day == 31:
            month = "November"
            day = 1
        else:
            day +=1
        
    elif( month == "November"):
        if day == 30:
            month = "December"
            day = 1
        else:
            day +=1
        
    elif( month == "December"):
        if day == 31:
            month = "January"
            day = 1
            year +=1
        else:
            day +=1

    #Print out date
    print("The next day is", month, day, end=", ")
    print(year, end=".")
          
main()
