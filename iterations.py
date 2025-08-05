#This Python code iterates through a list called fruits, containing "apple", "orange" and "kiwi." It prints each fruit name on a separate line, displaying them in the order they appear in the list.
fruits = ["apple", "orange", "kiwi"]
for fruit in fruits:
    print(fruit)

#This Python code manually iterates through a list of fruits using an iterator. It prints each fruit's name one by one and stops when there are no more items in the list.
fruits = ["apple", "orange", "kiwi"]
iter_obj = iter(fruits)
while True:
    try:
        fruit = next(iter_obj)
        print(fruit)
    except StopIteration:
        break