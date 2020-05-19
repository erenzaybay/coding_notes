




# use to comment a line

# use following way  to comment an entire section,it is not recommended

'''
I think
this 
is 
an 
great
idea
'''

# To declare an encoding other than the default one,
# a special comment line should be added as the first line of the file.
# The syntax is as follows:
# -*- coding: encoding -*-
# -*- coding: cp1252 -*-        # This means Windows-1252 encoding is to be used


# One exception to the first line rule is when the source code starts with a UNIX �"shebang" line.
# In this case, the encoding declaration should be added as the second line of the file. For example:
#!/usr/bin/env python3
# -*- coding: cp1252 -*-

# It is better to start the beginning like this  including "#"

#!/user/bin/python3
# what code written by who
# what the code does
# copywrite description


# In interactive mode, the last printed expression is assigned to the variable _. ,it is usefull for calculation

# the usefull excape sequences
# \n  newline
# \t  tab
# \\  \
# \'  '
# \"  "

# "methods" are function lives inside a class ,and "functions" are just functions.


# python3 tools for making command user interface


# why use tuple when list has more functions
#             tuple is a smaller type
#             tuple is faster in searching and some other operation
#             most importantly, you can't change tuple

# when you are coding, dictionary object can be a half way point
# between simple flat type and class method,
# you can put all you date in a dictionary
# so is became manageable

# try use more if __name__=="__main__":main() in non trivial code

PI = 3.14  # using Uppercase to indicate the constant, python don't really have constant


#-----------------------------------------------------------------------------------------------------------------
# python , in python there are two types of scopes,
# local variables with function scope and the global variable with file scope.
# In python there no block level scope.
# odd cases: python create a new local variable in function
# if you call global variable with in a function with the same value as the global variable.
# in order to actually call a global variable within a function,
# you need to declear it explicitly. difference between the following two functions:
# using global variable within a function is bad practice.
# you can access global variable within the function, but don't do it.

bad_greeting_1 = "a"


def greeting_1():
    bad_greeting_1 = "b"
    print(bad_greeting_1, "this shows b")


greeting_1()
print(bad_greeting_1, "This show a")


# there is global variable within the function , and its value is changed.
bad_greeting_2 = "a"


def greeting2():
    # this is how you access global variable within a function ,DON'T DO IT!
    global bad_greeting_2
    bad_greeting_2 = "b"
    print(bad_greeting_2, "this shows b")


greeting2()
print(bad_greeting_2, "this shows b")






#  use range to count down
for i in range(5, -1, -1):    # it count down from 5 to 0
    print(i, " ", end="")
for i in range(10, -1, -1):   # it count down from 10 to 0
    print(i, " ", end="")
# similar logic, count down from 100 to 1 is range(100,0,-1), understand its logic
for i in range(100, 0, 1):
    print(i, " ", end="")


# the usage of determining a variable is empty or not.
name = " "
if not name.strip():
    print("name variable is empty.")
# a clean way of writing some if expressions
age = 30
if 18 <= age < 65:
    print("Eligible")
else:
    print("Not Eligible")
# it can also be writen as the following:
message = "Eligible" if 18 <= age < 65 else "not eligible"
print(message)


# the dumb way
names = ["John", "Mary"]
found = False
for name in names:
    if name.startswith("J"):
        print("Found")
        found = True
        break  # to same time
if not found:
    print("Not found")
# the clean way, becase else will only be executed when for loop is completed without immediate break , it is the same with while loops , else only get execute when there is no break
names = ["John", "Mary"]
for name in names:
    if name.startswith("J"):
        print("Found")
        break  # to same time
else:
    print("Not found")


# This is how real code was writen in ,with in the main()
# In this way , you can define function at the end of the main content
"""
main():
    yourfuction1()
    yourfuction2()

def yourfuction1():
    pass

def yourfuction2():
    pass

if __name__="__main__":main()
"""


# This is called list comprehension
my_numbers1 = [x*x for x in [1, 2, 3, 4]]
my_numbers2 = [x*2 for x in range(1, 11)]
print(my_numbers1)
print(my_numbers2)

# This is a way to write short function in one line
def function_hello(yourname): print("Hello! ", yourname)

