## How importing in python works

import math
print(math.floor(4.3333))

result = math.sqrt(9)
print(result)  # Output: 3.0

## from keyword
from math import sqrt, pi
result = sqrt(9) * pi
print(result)
print(pi)

## importing everything
from math import *
#this is generally not recommended as it can lead to confusion and make it harder to understand where specific functions and variables are coming from


## The "as" keyword
import math as m

result = m.sqrt(9) * m.pi
print(result)  # Output: 3.0
print(m.pi)  # Output: 3.141592653589793


## The dir function
#dir that you can use to view the names of all the functions and variables defined in a module
import math

print(dir(math)) #dir print all function in math
