condition = (1,2,3)
x , y, z = condition
print(x)

#dictionaries

phone = input("Phone: ")
digits_mapping = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four'}
output = ""
for ch in phone:
    output = output + digits_mapping.get(ch, "!") + " "
print(output)