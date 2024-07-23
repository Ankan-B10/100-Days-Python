# Function Arguments and return statement
# - Default Arguments
# - Keyword Arguments
# - Variable length Arguments
# - Required Arguments

def avg(a=9, b=1):
    print("The average is",(a+b)/2)

avg(1,5) # - Default Arguments
avg(5)
avg(b=9)
avg(b=9, a=21) # - Keyword Arguments

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name(mname = "Rudra", lname = "Bera", fname = "Ankan")

### Required arguments:
def sum(a, b, c=1):
    print("sum =", a+b+c)

sum(2, 3) #must give values of a,b


### Variable-length arguments:
def avgAll(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is:", sum / len(numbers))
    # len ->gives length of numbers

avgAll(2, 3)
avgAll(4, 5, 6, 7)


#### Keyword Arbitrary Arguments:
def name(**name): # **name -> act as dictonary
    print(type(name))
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")


## return Statement
def avgAll(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    # return 7   # first wala always return first 
    return sum / len(numbers) # return the operation
    # len ->gives length of numbers

c = avgAll(4, 5, 6, 7) #call the function
print(c)
print("the average is:",avgAll(1, 2, 3))