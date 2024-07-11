a = "1"
b = "2"
print("String add -",a+b)
c = 1
d = 2
print("Integer add -",c+d)

print("###Explicit typecasting: ")
e = "1"
f = "2"
print("TypeCast add -",int(a)+int(b))
string = "15"
number = 7
string_number = int(string) #throws an error if the string is not a valid integer
sum = number + string_number
print("The Sum of both the numbers is: ", sum)

print("###Implicit type casting: ")
x = 1.9
y = 8
print(x+y) #converts a smaller data type to a higher data type to prevent data loss.
a = 7
print(type(a))

b = 3.0
print(type(b))

c = a + b
print(c)
print(type(c))