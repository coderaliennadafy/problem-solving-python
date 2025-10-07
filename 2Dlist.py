matrix = [  
    [1, 2, 3],
    [5, 4, 6],
    [9, 8, 7]
]

matrix[0][1] = 20
print(matrix[1][2])
print(matrix)

numbers = [5, 2, 1, 7, 4]
numbers.append(20)
print(numbers)

numbers.insert(2, 10)
print(numbers)

numbers.remove(5)
print(numbers)

numbers.clear()
print(numbers)

numbers = [5, 2, 1, 7, 4]

numbers.pop()
print(numbers)

print(numbers.index(7))
print(50 in numbers)

numbers = [4,0,9,4,6,7]
print(numbers.count(4))
print(len(numbers))
print(sorted(numbers))
print(numbers.count(0))
numbers.sort()
print(numbers)
numbers = [5,2,1,3,4] 
numbers.reverse()
print(numbers)

numbers = [5,2,1,3,4]
numbers2 = numbers.copy()
print(numbers2)
numbers = [5,2,1,3,4]
numbers3 = numbers.append(5)
print(numbers3)


numbers4 = [9,9,2,7,4,9,7,3,0]
numbers4 = list(set(numbers4))
print(numbers4)

numbers4 = [9,9,2,7,4,9,7,3,0]
for x in numbers4:
    iniquenumbers =[]
for iniquenumber in numbers4:
    if iniquenumber not in iniquenumbers:
        iniquenumbers.append(iniquenumber)
        print (iniquenumbers)
