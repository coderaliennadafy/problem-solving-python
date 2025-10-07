n = int(input("enter un number: "))
i = int(input("Table de multiplication de number :"))

for i in range (1,13):
    
    mult = i * n
    
    #print(f"{n} * {i} = {mult}")
    print("{} * {} = {}".format(n, i, mult))
