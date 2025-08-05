#For loops is used to iterate over a sequence such as a list, tuple, string or range. It allow to execute a block of code repeatedly, once for each item in the sequence.

#Syntax:
#for iterator_variable in sequence:
#   statement(s)

# Example 1: Using a for loop to iterate over a list
n = 4
for i in range(0, n):
    print(i)

# Example 2: Using a for loop to iterate over a list, tuple, string, dictionary.
li = ["Intro", "to", "for", "loops"]
for i in li:
    print(i)

tup = ("Intro", "to", "for", "loops")
for i in tup:
    print(i)

s = "Intro to for loops"
for i in s:
    print(i)

d = dict({'x': 1, 'y': 2, 'z': 3})
for i in d:
    print(i, ":", d[i])

set1 = {1, 2, 3, 4}
for i in set1:
    print(i)