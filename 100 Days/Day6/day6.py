## In python everything is Object
# Variables and Data Types
a = 5
b = True
c = complex(8,2)
d = 1.1
e = None
f = "Ankan"
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
a1 = 9
print(a + a1)
print("The type of a is ", type(a))
print("The type of b is ", type(b))
print("The type of c is ", type(c))
print("The type of e is ", type(e))
print("The type of f is ", type(f))

#list -> mutable , tuple -> immutable
list1 = [8, 2.3, [-4,5], ["apple, banana"]]
print(list1)

tuple1 = (("parret", "Lion"), 8, 9.99, ("Tiger", "monkey"))
print(tuple1) 

# dictnary -> colletion of key value pairs
dict1 = {"name": "Ankan", "age": 20, "canVote": True}
print(dict1)