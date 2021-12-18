#  File: LinearEquations.py
#  Description:

#
#  Date Created: 4/3 03:33PM
#  Date Last Modified: 4/4 06:02PM

############################################################################

class LinearEquation():

   def __init__(self,m,b):
      self.slope = m
      self.intercept = b
      

   def showEq(self):
      
      if(self.slope == 0) and (self.intercept == 0):
         return

      elif(self.slope == 0):
         return self.intercept

      elif(self.intercept == 0):
         return str(self.slope) + "x"

      elif(self.slope > 0) and (self.intercept > 0):
         return str(self.slope) + "x + " + str(self.intercept)

      elif(self.slope > 0) and (self.intercept < 0):
         return str(self.slope) + "x - " + str(abs(self.intercept))

      elif(self.slope < 0) and (self.intercept > 0):
         return "- " + str(abs(self.slope)) + "x + " + str(self.intercept)

      elif(self.slope < 0) and (self.intercept < 0):
         return "- " + str(abs(self.slope)) + "x - " + str(abs(self.intercept))


   def add(self,other):

      newSlope = self.slope + other.slope
      newIntercept = self.intercept + other.intercept
      newEquation = LinearEquation(newSlope,newIntercept)
      
      return newEquation
   
   
   def sub(self,other):

      newSlope = self.slope - other.slope
      newIntercept = self.intercept - other.intercept
      newEquation = LinearEquation(newSlope,newIntercept)

      return newEquation

   
   def compose(self,other):

      newSlope = self.slope * other.slope
      newIntercept = (self.slope * other.intercept) + self.intercept
      newEquation = LinearEquation(newSlope,newIntercept)

      return newEquation

   def evaluate(self,num):

      return (self.slope * num) + self.intercept


#unedited 
def main():

   f = LinearEquation(5,3)
   print("f(x) =",f.showEq())
   print("f(3) =",f.evaluate(3),"\n")
         
   g = LinearEquation(-2,-6)
   print("g(x) =",g.showEq())
   print("g(-2) =",g.evaluate(-2),"\n")

   h = f.add(g)
   print("h(x) = f(x) + g(x) =",h.showEq())
   print("h(-4) =",h.evaluate(-4),"\n")

   j = f.sub(g)
   print("j(x) = f(x) - g(x) =",j.showEq())
   print("j(-4) =",j.evaluate(-4),"\n")

   k = f.compose(g)
   print("f(g(x)) =",k.showEq(),"\n")
   
   m = g.compose(f)
   print("g(f(x)) =",m.showEq(),"\n")

   g = LinearEquation(5,-3)
   print("g(x) =",g.showEq())
   print("g(-2) =",g.evaluate(-2),"\n")
   
   h = f.add(g)
   print("h(x) = f(x) + g(x) =",h.showEq())
   print("h(-4) =",h.evaluate(-4),"\n")

   j = f.sub(g)
   print("j(x) = f(x) - g(x) =",j.showEq())
   print("j(-4) =",j.evaluate(-4),"\n")
   
main()
