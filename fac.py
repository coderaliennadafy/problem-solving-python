def fact(nbr):
        
    if nbr != 0:
        
        return nbr  * fact(nbr - 1)
    
    else:
        
        return 1
    
nbr = int(input("enter the number : "))

print(fact(nbr))