#  File: Combinations.py
#  Description: prints a table listing the number of possible hands of r cards

#
#  Date Created: 3/7 12:41PM
#  Date Last Modified: 3/11 02:14PM

def factorial(num):

    factorialNum = 1
        
    for i in range(1,num+1):

        factorialNum *=i
        
    return factorialNum


def combinations(n,r):

    return factorial(n)//(factorial(r) * factorial(n-r))


def main():

    print("Cards" + format("Combinations",">17s"))
    print("=" * 22)

    for i in range (0,53):  
         print( format( i , ">3d") + format(combinations(52,i),">19d"))   
          
main()
