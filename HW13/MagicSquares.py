#  File: MagicSquares.py
#  Description: 

#
#  Date Created: 4/21 00:00PM
#  Date Last Modified: 4/23 9:46PM

class MagicSquare():
    
    def __init__(self,sides):
        self.sideLength = sides
        self.grid = []
        
        #make blank grid
        for row1 in range(0,self.sideLength):
            r = [0]
            for col1 in range(0,self.sideLength-1):
                r.append(0)
            self.grid.append(r)

        
        #equation
        col = self.sideLength//2 
        row = 0

        self.grid[row][col] = 1
        
        
        for i in range(2,self.sideLength**2 + 1):

            if (i-1) % self.sideLength == 0: #multiples move down
                
                row +=1
                self.grid[row][col] = i

            elif row == 0: #if its the top edge

                row = self.sideLength-1

                col += 1

                self.grid[row][col] = i


            elif col == self.sideLength-1: #if its at the right edge

                col = 0

                row -= 1

                self.grid[row][col] = i


            else:
                row -=1
                col +=1
                self.grid[row][col] = i #move diagonally
                

                    

    def display(self):

        numRows = len(self.grid)
        numCols = len(self.grid[0])

        for row in range(numRows):
            for col in range(numCols):
                print(format(self.grid[row][col],"5d"), end="")
            print("")
        
            
    

def main():

    listSides = [1,3,5,7,9,11,13]
    for i in range(0,len(listSides)):
        print("Magic Square of", listSides[i])
        print()
        square = MagicSquare(listSides[i])
        square.display()
        print("")
          
main()
