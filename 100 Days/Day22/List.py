# Python Lists
# Lists are ordered collection of data items.

marks = [3, 5, 6]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])

print(marks[-3]) #negative index
print(marks[len(marks)-3]) #positive
print(marks[5-3]) 


details = ["Ankan", 20, "FYBScIT", 9.8, True]
print(details)
# print(details[9]) #9 not available


colors = ["Red", "Green", "Blue", "Yellow", "Green"]
if "Yellow" in colors:
    print("Yellow is present.")
else:
    print("Yellow is absent.") 

## Range of Index: listName[start : end : jumpIndex]

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[1:8:3])

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[4:])	#using positive indexes
print(animals[-4:])	#using negative indexes

num = [1,2,3]
print(num[:])


# List Comprehension
lst = [i*i for i in range(10)]
print("list Comprehension",lst)

lst2 = [i*i for i in range(10) if i%2 == 0]
print(lst2)



