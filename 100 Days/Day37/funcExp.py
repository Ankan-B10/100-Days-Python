def func1():
    try:
        ls = [1, 5, 6, 9]
        i = int(input("Enter the index: "))
        print(ls[i])
        return 1
    except:
        print("Some error occured")
        return 0
    finally:
        print("I am always executed") # always executed

x = func1()
print(x)

## If Not use Finally 
def func2():
    try:
        ls = [1, 5, 6, 9]
        i = int(input("Enter the index: "))
        print(ls[i])
        return 1
    except:
        print("Some error occured")
        return 0
    
print("I am always executed") #not always exucuted

x = func2()
print(x)