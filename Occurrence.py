valeur = input("enter The val number: ")

cmp = 0
for i in range (1,6):
    nb = input("enter un number: ")
    
    if nb == valeur:
        cmp += 1
        
print(cmp)