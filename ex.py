from math import *
a = float(input("enter le  nombre a :"))
b = float(input("enter le nombre b :"))
c = float(input("enter le nombre c :"))
if a == 0:
    print("pas possible")
else:
    delta = b**2-4*a*c
    print ("delta = ",delta)
    if delta >0:
        x1 = (-b +sqrt(delta))/2*a
        x2 = (-b -sqrt(delta))/2*a
        print("deux solution :" ,x1, x2)
    elif delta == 0:
        x = -b/(2*a)
        print("un seule= solution :")
        print("x =",x)
    else:
        print("pas de solution")
       
        