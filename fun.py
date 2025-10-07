def greet_user():
    print('Hello')
    print('Welcome aboard')
    
print('Start')
greet_user()
print('Finish')


#parameters

def great_user(first_name, last_name):
    print(f"Hello {first_name} {last_name}")
    print("Welcome aboard")


print("start")

great_user("Fatima","smith") #position argument before keyword argument keyword = value = first_name = "Fatima"
print ("finish")