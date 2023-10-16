import random
target_num = random.randint(1,10)
while True:
guess_num = int(input("Enter your guess (between 1 to 10): "))
if guess_num < target_num :
print ("Too low")
elif guess_num > target_num :
print ("Too high")
else:
print(f"Well done! Your guessed number is {guess_num} and your guess is correct!.")
break
