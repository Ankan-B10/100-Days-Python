# Enumerate function in python
#allows you to loop over a sequence (such as a list, tuple, or string) and get the index and value of each element in the sequence at the same time.

index = 0
marks = [12, 56, 34, 98, 45, 1, 4]
for i in marks:
    print(i)
    if(index == 3):
        print("Ankan is good coder")
    index += 1

# Using Enumerate function ->
index = 0
marks = [12, 56, 34, 98, 45, 1, 4]
for index, i in enumerate(marks):
    print(i)
    if(index == 3):
        print("Ankan is good coder")



