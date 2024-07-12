 # Match Case Statements -> switch case
'''
The match case consists of three main entities :
1. The match keyword
2. One or more case clauses
3. Expression for each case
'''
x = int(input("Enter the value of x: "))
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4 if x % 2 == 0:
        print("x % 2 == 0 and case is 4")
    # Empty case with if-condition
    case _ if x < 10:
        print(x,"is < 10")
    case _ if x!=90:
        print(x,"is not 90")
    # default case(will only be matched if the above cases were not matched)
    # so it is basically just an else:
    case _: # "_" undersorded use for default case
        print(x)