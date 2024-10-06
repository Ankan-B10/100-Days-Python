ep1 = {
    122: 45, 123: 89, 567: 69, 670: 99
}

ep2 = {
    222: 67, 123: 90, 566: 99
}
 ## update() 
ep1.update(ep2)
print(ep1)

### clear():The clear() method removes all the items from the list. 
ep1.clear()
print(ep1)

#### pop():
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info.pop('eligible')
print(info)

### popitem():
info = {'name':'Karan', 'age':19}
info.popitem()
print(info)


### del: we can also use the del keyword to remove a dictionary item. 
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info['age']
print(info)

# If key is not provided, then the del keyword will delete the dictionary entirely.
# info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
# del info
# print(info)


