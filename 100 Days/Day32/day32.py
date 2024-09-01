s1 = {1, 2, 5, 6}
s2 = {3, 6, 9}
print(s1, s2)
print("Union = ",s1.union(s2))
s1.update(s2)
print(s1, s2)


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2)
print(cities3)
cities4 = cities.symmetric_difference(cities2)
print(cities4) 


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)

## isdisjoint():
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))

## issubset():
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities))

# add()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)

## update()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print(cities)

# remove()/discard()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)
# cities.remove("Seoul") #gives error
cities.discard("Seoul")


# pop()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
item = cities.pop()
print(cities)
print(item)

## del
cities101 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities101
# print(cities101) #can not print, bcoz no cities are left

#if we don’t want to delete the entire set
## clear():
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)

## Check if item exists
info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")