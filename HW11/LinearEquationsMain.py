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
