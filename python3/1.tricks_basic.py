



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

#-----------------------------------------------------------------------------------------------------------------