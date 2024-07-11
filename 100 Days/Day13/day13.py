# Strings are immutable
a = "Ankan"
print(len(a))
print(a.upper())
print(a.lower())
#rstrip() removes any trailing characters.
str3 = "Hello !!!"
print(str3.rstrip("!"))

str2 = "Silver Spoon"
print(str2.replace("Sp", "M"))

str3 = "Hi, I am Ankan Bera"
print(str3.split(" "))

#The capitalize() turns only first character to uppercase
str2 = "hello WorlD"
capStr2 = str2.capitalize()
print(capStr2)
#OR-> 
print(str2.capitalize())

#The center() method aligns the string to the center as per the parameters given by the user.
str1 = "Welcome to the Console!!!"
print(str1.center(50))
str2 = "Welcome to the Console!!!"
print(str2.center(50, "."))

a = "Ankan, !!!! hey Ankan, !!! how are you Ankan"
print(a.count("Ankan"))

## endswith() : 
str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))
str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))

## find() : searches for the first occurrence of the given value
str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))
str1 = "He's name is Dan. He is an honest man."
print(str1.find("Daniel"))

## index() :
str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Dan"))


## isalnum() :returns True if string only consists of A-Z, a-z, 0-9.
str1 = "WelcomeToTheConsole"
print(str1.isalnum())

## isalpha() :returns True only if entire string only consists of A-Z, a-z
str1 = "Welcome"
print(str1.isalpha())
str2 = "Welcome123"
print(str2.isalpha())

## islower() :
## isupper() :
## isprintable() : \n is not printable
str1 = "We wish you a \nMerry Christmas"
print(str1)
print(str1.isprintable())

## isspace() :returns True only and only if string contains white spaces
str1 = "        "       #using Spacebar
print(str1.isspace())
str2 = "Hi"
print(str2.isspace())

## istitle() : if the first letter of each word is Capital
str1 = "World Health Organization" 
print(str1.istitle())

## startswith() :
str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

## swapcase() : Upper case -> lower case & lower case -> upper case.
str1 = "Python is a Interpreted Language" 
print(str1.swapcase())

### title() : convert first letter to Capital
str1 = "He's name is Dan. Dan is an honest man."
print(str1.title())
