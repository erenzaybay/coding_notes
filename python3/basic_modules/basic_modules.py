# the following are the example structure

"""
the library calculater includes two modules called cal_adding.py and cal_multiply.py

jiafa() is in cal_adding.py and chengfa() is in cal_multiply.py
folder "calculater" include two folers,"simple" and "complex"

each of the folders should contain an "init file", named as __init__.py, this file tell python that it is a library

so we have files and folders as follows:

    calculater/__init__.py
    calculater/simple/__init__.py
    calculater/complex/__init__.py
    calculater/simple/cal_adding.py               jiafa() is in it
    calculater/complex/cal_multiply.py            chengfa() is in it

This is another view:
    calculater
        __init__.py
        simple
            __init__.py
            cal_adding.py
        complex
            __init__.py
            cal_multiply.py
"""

# This is the best way , it is neither to deep to introduce possible conflicts ,and yet 
# not too shallow to be to cumbersome
"""
from calculater.simple import cal_adding

answer1=cal_adding.jiafa(2,5)
print(answer1)
"""

# This works,but it is better not use this unless its a small program only you use
# because it has the potential of creating conflicts
# if other modules that also imported this way has jiafa(),it may be confusing
"""
from calculater.simple.cal_adding import jiafa

answer2=jiafa(99,99)
print(answer2)
"""

