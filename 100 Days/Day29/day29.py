# Docstrings in python

def square(n):
    '''Takes in a number n, returns the square of n''' #not comment, docString
    print(n**2)
square(5)
print(square.__doc__) #docstring


## Python Comments vs Docstrings
# Comments are descriptions that help programmers better understand the intent and functionality of the program.
# docstrings are used to document our code. used right after the definition of a function
# access these docstrings using the ( __doc__ )attribute.


#pep8 -> Python Enhancement Proposal
#primary focus of PEP 8 is to improve the readability and consistency of Python code

# The Zen of Python -> import this in terminal to print Zen
'''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those! 
'''




