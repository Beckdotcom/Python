#  File: Grades.py
#  Description: 

#
#  Date Created: 4/24 00:00PM
#  Date Last Modified: 4/26 05:55PM

def main():

    nameFile = open("gradeInput.txt","r")
    outFile = open("gradeOutput.txt","w")

    #header
    outFile.write(format(" ", "30s") + format("HW  ", "^7s") +
          format("Exam", "^7s") + format("Final", "^7s") + "\n")
    outFile.write(format("Last Name", "15s") + format("First Name", "15s") +
                format("Avg ", "^7s") + format("Avg ", "^7s") +
                format("Grade", "^7s") + "\n")
    outFile.write(("-" * 50) + "\n" )

    char = nameFile.readline(1)
    
    while char != "":

        #get last name
        lastName = ""
        while char != ",":
            lastName += char
            char = nameFile.read(1)

        #char is , at this point
        char = nameFile.read(1) #ignore the comma I currently have and move on

        #get first name
        firstName = ""
        while char != " ":
            firstName += char
            char = nameFile.read(1)

        #get numbers
        numberString = ""
        while char != "\n":
            numberString +=char
            char = nameFile.read(1)

        numberList = [eval(x) for x in numberString.split()]

        #calculate hw average
        hwAvg = 0
        for i in range(0,15):
            hwAvg +=numberList[i]

        hwAvg = hwAvg / 15

        #calculate exam average
        examAvg = 0
        for i in range(15,18):
            examAvg +=numberList[i]

        examAvg = examAvg / 3

        #calculate final grade
        finalGrade = (hwAvg * .55) + (examAvg * .45)

        
        # char is \n at this point
        outFile.write(format(lastName, "15s") + format(firstName, "15s") +
                format(hwAvg, "^7.1f") + format(examAvg, "^7.1f") +
                format(finalGrade, "^7.1f") + "\n")

        char = nameFile.read(1) #end it

    nameFile.close()
    outFile.close()
    

          
main()
