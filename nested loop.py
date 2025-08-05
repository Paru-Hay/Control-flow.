
for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()  # New line after each inner loop completion

#1. Generate a multiplication table for numbers from 1 to a user-defined limit, showing all multiples from 1 to 10.
n = 3

for i in range(1, n + 1):
    for j in range(1, 11):
        print(i * j, end=' ')
    print()

#3. Construct a square matrix of 1s and 0s where only diagonal elements are 1, mimicking an identity matrix.
n = 4
for i in range(n):
    for j in range(n):
        if i == j:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()  # move to the next row



