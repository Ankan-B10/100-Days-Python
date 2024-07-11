# String Slicing
names = "Ankan,Rudra,Bappa"
print(names[0:5])
# Length of String
fruit = "Mango"
len1 = len(fruit)
print(len1)
print("Mango is a", len1, "letter word.")
print(fruit[0:4])
print(fruit[:4])
print(fruit[0:-3])#-3 = [len(fruit)-3]
print(fruit[:])
print(fruit[-1:-3]) #4:2 -> NA
print(fruit[-3:-1]) #2:4

pie = "ApplePie"
print(pie[:5])      #Slicing from Start
print(pie[5:])      #Slicing till End
print(pie[2:6])     #Slicing in between
print(pie[-8:])     #Slicing using 
print(pie[-1])

#Quick Quiz
print(fruit,"ans =",fruit[-4:-2])