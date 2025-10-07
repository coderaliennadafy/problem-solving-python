import random

for i in range(3):
    print(random.random())
    
for j in range(3):
    print(random.randint(10,20))

members = ['john','oussama','alaa','mohammed']
leader = random.choice(members)
print(leader)