#Else clause is only executed when our while condition becomes false. If we break out of the loop or if an exception is raised then it won't be executed. 
#Syntax:
#while condition:
#   statement(s)    
#else:
#   statement(s)

cnt = 0
while (cnt < 5):
    cnt = cnt + 1
    print("Hello")
else:
    print("End of while loop execution")

#Infinite while loop
while (True):
    print("This will run forever unless you stop it manually")
    # Uncomment the next line to break the loop
    # break