# Manipulating Tuples

countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)

tuple1 = (0, 1, 2, 39, 2, 3, 1, 2, 3, 3)
# ans = tuple1.index(3)
# print("3 present in tuple1 is: ",ans)
res = tuple1.index(3,5,9)
print(res)

 