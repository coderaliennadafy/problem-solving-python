import listorganiser

def find_max(numbers):
    
    max = numbers[0] 
    for number in numbers:
        if number > max:
            max = number
            return max

numbers = [2, 3, 5, 7, 11]

max = listorganiser.find_max()

print(max)
