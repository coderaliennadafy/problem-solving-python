from math import *

a = float (input("Enter la valeur de number a :"))
b = float (input("Enter la valeur de number b :"))
c = float (input ("Enter la valeur de number c :"))

if a == 0:
    print("pas possible")
    
else:
    delta = (b**2 - 4*a*c)
print("delta = ",delta)

if delta > 0:
    x1 =  (-b + sqrt (delta)) / (2*a)
    x2 = (-b + sqrt  (delta)) / (2*a)
    print("deux solution:")
    print("x1=",x1)
    print("x2=",x2)

elif delta == 0:
    x = -b / (2*a)
    
    print("l'equation admet une solution X :" , x)
    
else :
    print("pas de solution  ")