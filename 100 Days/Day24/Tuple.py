# Tuple: Tuples are unchangeable
tup1 = (10, 20, 30)
print(type(tup1), tup1)
tup2 = (1) # no py makes it integer
print(type(tup2), tup2)
tup3 = (1,) #now this becomes a tuple'
print(type(tup3), tup3)

details = ("Abhijeet", 18, "FYBScIT", 9.8, True)
print(details)
print(details[-1])

## Check for item:
if 18 in details:
    print("Yes 18 is present in details")
else:
    print("not present")

country = ("Spain", "Italy", "India", "England", "Germany")
if "Russia" in country:
    print("Russia is present.")
else:
    print("Russia is absent.")

### Range of Index:

tup = (1,2,76,342,10,999,"green")
tup2 = tup[1:4]
print(tup2)
print(tup2[:]) #print all val of tup2

### Example: Print alternate values
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[::2])     #using positive idx
print(animals[-8:-1:2]) #using negative indexes
print(animals[1:8:2])
