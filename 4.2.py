inch = 2.54

while True:
inches = float(input("Enter the inches to convert in cm: "))
cm = inch * inches
if inches >=0:
print (f"{inches} inches is equal to {cm} cm")
break
else:
print("Invalid number. Please enter positive number.")
