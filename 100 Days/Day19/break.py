#break: skip the loop iteration
i=0
while(i<12):
    print("5 X", i+1, "=", 5 * (i+1))
    if(i == 9):
        break
    i+=1

print("Loop ended")


for i in range(10,101,5):
    print(i ,end=" ")
    if(i==50):
        break
    else:
        print("Mississippi")
print("Thank you")