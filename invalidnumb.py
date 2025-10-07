try:
    age = int (input("age: "))
    print(age)
    
except ValueError:
    print("Invalid number")

    age = int (input("age: "))
    print (age)
    
age = int (input ("age: "))
income = 20000
risk = income / age   
print (age)

#error if age = 0 because division by zero is not allowed

try:
    age = int (input("age: "))
    print(age)
    income = 20000
    risk = income / age 
except ZeroDivisionError:
    print("Age cannot be zero.")