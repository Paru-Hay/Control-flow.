#Loop control statements change execution from their normal sequence. When execution leaves a scope, all automatic objects that were created in that scope are destroyed.

#Continue statement: It skips the current iteration and continues with the next iteration of the loop.

for letter in 'controlflow':
    if letter == 'e' or letter == 's':
        continue
    print('Current Letter:', letter)

#Break statement: It terminates the loop and transfers execution to the statement immediately following the loop.
for letter in 'controlflow':
    if letter == 'e' or letter == 's':
        break
    print('Current Letter:', letter)

#Pass statement: It does nothing and is used when a statement is required syntactically but you do not want any command or code to execute.
for letter in 'controlflow':
    pass
print('last letter:', letter)