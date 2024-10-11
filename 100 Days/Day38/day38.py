## Raising Custom errors 

a = int(input("Enter any values between 5 amd 9 = "))

if(a<5 or a>9):
    raise ValueError("Value out of range")

salary = int(input("Enter salary amount: "))
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary")

## Defining Custom Exceptions
class CustomError(Exception):
  print("Something")
  # code ...
  pass

try:
    print("Try block")
  # code ...

except CustomError:
    print("Hi please solve this")