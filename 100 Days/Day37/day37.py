# Finally Clause -> It is always executed
try:
    ls = [1, 5, 6, 9]
    i = int(input("Enter the index: "))
    print(ls[i])
except:
    print("Some error occured")

finally:
    print("I am always executed")


try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
else:
    print("Integer Accepted.")
finally:
    print("This block is always executed.")