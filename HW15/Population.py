#  File: Population.py
#  Description: 
#  Unique Number: 50180
#
#  Date Created: 5/1 03:00PM
#  Date Last Modified: 5/ 06:46PM


def main():

    numberSet = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    cities = 0

    nameFile = open("2009CensusData.txt","r")

    line = nameFile.readline() #ignore first line
    line = nameFile.readline() #get first line

    while line != "": #until empty
        
        splitLine = line.split() #split into list
        numberLine = splitLine[len(splitLine)-1] #use number part of list

        number = int(numberLine[0]) #get first number

        numberSet[number] = numberSet.get(number) + 1 #add to dict
        
        line = nameFile.readline()#get another line

        cities +=1 #+1 cities
        
    nameFile.close()

    print(format("Digit","8s") + format("Count","10s") + format("%", "2s"))
    print("-" * 20)

    for i in range(1,10):
        percent = (numberSet.get(i)/cities) * 100
        print(format(i,"<8d") + format(numberSet.get(i),"5d")
              + format(percent, "8.1f"))
    
    
          
main()
