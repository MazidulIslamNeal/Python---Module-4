attempts = 0
while attempts < 5:
username = input("Enter username: ")
password = input ("Enter password: ")
if username == "python" and password == "rules":
print("Welcome! Login successful!")
break
else:
print("Invalid username or password")
attempts += 1
if attempts == 5:
print("You have tried more than 5 times!!")
print ("Access Denied!!!")
