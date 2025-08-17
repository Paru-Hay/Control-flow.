#3. Display the multiplication table of a number provided by the user in one line, only the numbers.
n = input("Enter a number: ")   
for i in range(1, 11):
    print(int(n) * i, end=' ')

#4. In a given string s, print its characters at even indices.
n = input("Enter a string: ")
for i in range(0, len(n), 2):
    print(n[i], end=' ')