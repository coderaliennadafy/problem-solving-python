def Premier(n):
    
    if n <= 1:
        
        return False  #les nomber <= 1 il sant pas premier
    
    
    for i in  range(2,n // 2 + 1):
    
        if i % 2 == 0:
            
            return False # Trouvé un diviseur, donc pas premier
        
    else:

        return True #Aucun diviseur trouvé, donc premier        
         
    