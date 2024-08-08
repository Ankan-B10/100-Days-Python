# String formatting in python

letter = "hey my name is {} and I am from {}"
name = "Rudra"
country = "India"

print(letter.format(name, country))

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))



# f-strings in python: f"" It is a new string format mechanism 
print(f"hey my name is {name} and I am from {country}")

print(f"{2 * 30}")
print(type(f"{2 * 30}"))
print("")
print("To see raw f-string {} braces")
print(f"hey my name is {{name}} and I am from {{country}}")

