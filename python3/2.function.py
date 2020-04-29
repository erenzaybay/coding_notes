# function take in parameter and return result or perform functions, how to actually connote a function:
def increment(number: int = 10, by: int = 20) -> tuple:
    print(number+by)
    return (number, number+by)


print(increment(number=3, by=1))


# It can take in a function as a parameter


def function_mother(function, x):
    return function(x)


def function_child(a):
    return a*a


print(function_mother(function_child, 5))  # result is 25

# Function can takin a function as values
function_a = function_b

# using key word argument and unpacking tuple,list, and string


def function_unpacking(one_element, *kwargs):
    print(one_element, end=" ")
    for i in kwargs:
        print(i, end="|")
    print("\n")


list_input = [1, 2, 3, 4, 5, 6, 7]
tuple_input = (1, 2, 3, 4, 5, 6, 7)
string_input = "1234567"
function_unpacking("list input", *list_input)
function_unpacking("tuple input", *tuple_input)
function_unpacking("string input", *string_input)
function_unpacking("direct input", 1, 2, 3, 4, 5, 6, 7)

# using key word argument and unpacking dictionary
# the non unpacking variable should be at the beging


def function_for_dictionary(**kwargs):
    for key in kwargs:
        print(key, kwargs[key])


function_for_dictionary(**the_dictionary_variable)


# This example includes all the type we learned ,the order is important
def function_with_all(integer, string, *args, **kwargs):
    pass
    print(integer, string, args[i], kwargs["name"])


# funtion_with_default_values(x=1,2)   This is not valid
# once you use using key word arguments, you have to use it for the rest of the variables
# This is allowed
funtion_with_default_values(1, c=40, d=50)

# you can assign a function to another variable
function_print = function_printing


# make sure of the details and rewrite the following part
def function_with_key_value_argument():
    pass


def function_with_list_or_tuple_as_inputs():
    pass
