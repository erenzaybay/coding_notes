# good books to be read
pep 8
hickhikers way to python
real python


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
