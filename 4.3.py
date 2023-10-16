numbers =[]
while True:
num = input("Enter a number (or Press enter to exit): ")
if num == "":
break
numbers.append(num)
if numbers:
smallest = min(numbers)
largest = max(numbers)
print(f"The largest number is {largest}")
print(f"The smallest number is {smallest}")
else:
print("No number entered. Please enter a number")
