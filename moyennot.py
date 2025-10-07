iter = float(input())
somme = 0
for i in range (iter):
    note = float(input())
    somme += note
    moy = somme / iter
print(moy)