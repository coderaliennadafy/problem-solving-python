
def puissance(base,exposant):
    
    #cas ou L'exposant est 0
    
    if exposant == 0:
    
        return 1
    
    #cas ou L'exposant est negatif
    
    if exposant < 0:
        
        base = 1 / base
             
    exposant = -exposant
    
        
    #cas ou l'exposant est negatif
        
    result = 1
        
    for i in  exposant:
            
        result *= base 
    

