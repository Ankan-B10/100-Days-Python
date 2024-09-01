# Recursion in python
def factorial(num): 
    if (num == 1 or num == 0):
        return 1
    else:
        return num * factorial(num - 1)
print("Factorial is - ")
print(factorial(5))


# Fibonacci series
def fibo(n):
    if n <= 1:
        return n
    else:
        return (fibo(n-1)+fibo(n-2))

nterms = int(input("How many terms? - "))
if nterms <= 0:
    print("Please enter a positive number - ")
else:
    print("fibonacci seq is -")
    for i in range(nterms):
        print(fibo(i))