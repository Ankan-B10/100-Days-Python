#Loops ~
# - for loop
# - while loop 
name = "Ankan"
for i in name:
    print(i)
    if(i == "k"):
        print("This is very special")

colors = ["Red", "Green", "Blue", "Pink", "White"]
for color in colors:
    print(color)
    if(color == "green"):
        print("Dil garden garden ho gaya")
    
    for i in color:
        print(i)

## range():if we want to use for loop for a specific number of times
# print("Range ~ ")
# for k in range(5):
#     print(k)
# print("To print 1 to 5")
# for l in range(5):
#     print(l+1)
# print("range(9,15) :")
# for m in range(9,15):
#     print(m)

# 3 parameter
for x in range(1, 12, 3):
    print(x)