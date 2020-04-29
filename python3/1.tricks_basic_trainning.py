'''
pass
'''

# There types of head of the file
# -*- coding: cp1252 -*-

#!/usr/bin/env python3
# -*- coding: cp1252 -*-

#!/user/bin/python3
# what code written by who
# what the code does
# copywrite description

# the last printed expression is assigned to the variable
_.

\n  newline
\t  tab
\\  \
    \'  '
\"  "

# "methods" in class ,and "functions" are just functions.

# python3 tools for making command user interface

# why use tuple ,smaller type, faster, immutable

# dictionary  a half way point between simple flat type and class method,

if __name__ == "__main__":
    main()

PI = 3.14  # using Uppercase to indicate the constant, python don't really have constant


bad_greeting_2 = "a"


def greeting2():
    # this is how you access global variable within a function ,DON'T DO IT!
    global bad_greeting_2
    bad_greeting_2 = "b"
    print(bad_greeting_2, "this shows b")


greeting2()
print(bad_greeting_2, "this shows b")
