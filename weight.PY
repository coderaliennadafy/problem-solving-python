weight = int(input("weight : "))
lbs = (input(" (L)bs or (K)g : "))

if lbs.upper() == "L":
	converted = weight * 0.45
	print(f"you are {converted} kilos")

else:
	converted = weight / 0.45
	print(f"you are {converted} pounds")

