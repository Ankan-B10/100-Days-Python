# List Methods

## append(): appends items to the end of list.
l = [1, 2, 4, 6]
print(l)
l.append(9)
print("After append-",l)

## list.sort()
num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort()
print(num)

## reverse()
colors = ["voilet", "indigo", "blue", "green"]
print(colors)
colors.reverse()
print(colors)

## index(): returns the index of the first occurrence
colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.index("green"))
print(colors.index("voilet"))

## count(): Returns the count of the number of items 
colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.count("green"))


## copy()
l = [1, 2, 4, 6, 99, 23]
print(l)

m = l.copy()
m[0] = 0
m[1] = 0
print("m -",m)
print("l -",l)

## insert(): This method inserts an item at the given index.
colors = ["voilet", "indigo", "blue"]
print(colors)
colors.insert(0, "Red")
colors.insert(1, "Green")
print("Updated -",colors)


## extend(): his method adds an entire list or any other collection datatype (set, tuple, dictionary)
n = [1, 2, 4, 6, 99, 23]
m = [900, 1000, 1100]
n.extend(m) # m added to n 
print(n)
# k = n+m
# print(k)        #same work as extend

## Concatenating two lists:
colors = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
print(colors + colors2)



