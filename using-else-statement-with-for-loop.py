#We can also combine else statement with for loop like in while loop. But as there is no condition in for loop based on which the execution will terminate so the else block will be executed immediately after for block finishes execution. 

li = ["Intro", "to", "for", "loops"]
for index in range(len(li)):
    print(li[index])
else:
    print("End of for loop execution")