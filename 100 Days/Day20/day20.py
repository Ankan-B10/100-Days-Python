# here two types of functions:
# 1. Built-in functions -> min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.
# 2. User-defined functions

def isGreater(a,b):
    if(a>b):
        print("first num is greater")
    else:
        print("second num is greater or equal")
def isLesser(x,y):
    pass #pass means we do this later
def caliGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)


a = 9
b = 15
isGreater(a,b)

c = 10
d = 5
isGreater(c,d)