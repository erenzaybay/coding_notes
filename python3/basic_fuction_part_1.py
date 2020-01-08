# function can return a value
def function_adding(a,b):
    return a+b

# function can do things
def function_printing(a,b,c):
    print(f"I want to print {a}, {b}, and {c}!")

# they can return value and do things at the same time
def function_print_and_add(a,b):
    print(a,b)
    return a+b

def function_with_default_values(a=2,b=3,c=4,d=5):
    print("result of function with default values are ",a," ",b," ",c," and ",d)

# you can use a function within a function using function as input variable
def function_mother(function,x):
    return function(x)

def function_child(a):
    return a*a


# make sure of the details and rewrite the following part
def function_with_key_value_argument():
    pass

def function_with_list_or_tuple_as_inputs():
    pass


# funtion_with_default_values(x=1,2)   This is not valid
# once you use using key word arguments, you have to use it for the rest of the variables

# This is allowed
funtion_with_default_values(1,c=40,d=50)

function_print=function_printing # you can assign a function to another variable

