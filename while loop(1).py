#1. Implement a countdown that starts from a user-given number and decreases to 1, displaying the remaining time at each step.
seconds = int(input("Enter countdown time in seconds: "))

while seconds > 0:
    print("Time left:", seconds)
    seconds -= 1

#2. Keep reading numbers from the user and calculate the cumulative sum until the input is 0.
total = 0
num = int(input("Enter number (0 to stop): "))
while num != 0:
    total += num
    num = int(input("Enter number (0 to stop): "))
print("Total sum:", total)