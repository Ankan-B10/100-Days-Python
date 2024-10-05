dic={
    "Ankan": "Indian",
    "Age": "21",
    "City": "Kolkata",
    "Gender": "Male"
}

print(dic["Age"])
print(dic["Gender"])

info = {
    244: "Ankan",
    3: "Rudra",
    "567": "Bappa",
    440: "Ankita"
}

print(info[3])


### II. Accessing multiple values:
print(info.values())

## Or-> Everything
print(info)

##  Or -> Keys
print(info.keys())

print(info.items())

details = {'name':'Karan', 'age':19, 'eligible':True}
for key, value in details.items():
    print(f"The value corresponding to the key {key} is {details[key]}")
## OR ->
for key, value in details.items():
    print(f"The value corresponding to the key {key} is {value}")