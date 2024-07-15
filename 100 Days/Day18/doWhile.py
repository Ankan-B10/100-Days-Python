# Do-While loop in python - execute once always
while True:     #True: runs until the condition is getting fales
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    print("Loop is ended")
    break       #break-> stop the iteration