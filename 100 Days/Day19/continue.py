# continue: skips that value loop iteration
for i in range(12):
    if(i == 4):
        print("skip the iteration")
        continue
    if(i == 9):
        print("skip the iteration")
        continue
    print("5 X", i, "=", 5 * i)
