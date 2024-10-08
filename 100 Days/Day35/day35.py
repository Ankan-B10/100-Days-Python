# Python - else in Loop

for i in []:
    print(i)

else:
    print("Please give range")


# check by break ->
for i in range(6):
    print(i)
    if(i==4):
        break

else:
    print("Thank you, not able to Print")


## Example:
for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
    
print ("Out of loop")
