#1. The problem is to take shopping items as input from the user and display them one by one in a structured format.

items = input("Enter shopping items separated by commas: ").split(',')

for item in items:
    print("Buy:", item.strip())

#2. Display the square of each number starting from 1 up to a number provided by the user.
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print("Square of", i, "is", i**2)


    