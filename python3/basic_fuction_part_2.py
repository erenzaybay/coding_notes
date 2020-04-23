# function with tuple as the argumet
# the tuple can not be changed,it is imutables


def function_with_tuple_simple(*args):
    for name in args:
        print(f"{name} is winner!")


function_with_tuple_simple("Jane", "Jack", "Jude", "Jasimin")

winer_list = ["Jane", "Jack", "Jude", "Jasimin"]

# You can not directly use a list, it will see the list as an one element
function_with_tuple_simple(winer_list)  # check the result

# You need to use * to note that you want it to be splited
function_with_tuple_simple(*winer_list)  # check and compare the result


# function with key word argumets as the argumet
# It is like a dictionary
# it is convention to name it **kwargs
def function_with_key_word_argument_simple(**kwargs):
    for key in kwargs:
        print(key, kwargs[key])


function_with_key_word_argument_simple(name="Eren", Age="33", gender="male")

# the named argument should at the begining


def function_with_tuple(complement, *names):
    for name in names:
        print(f"{name} is {complement}!")


function_with_tuple("the winner", "Jane", "Jack", "Jude", "Jasimin")

# the named argument should be at the begining


def function_with_key_word_argument(message, **kwargs):
    print(message)
    for key in kwargs:
        print(key, kwargs[key])


function_with_key_word_argument(
    "We have a soldier!", name="Eren", Age="33", gender="male")


# This example includes all the type we learned
# the order is important , the name argumet, the tuple argument and the key word arguments
def function_with_all(mynumber, mystring, *args, **kwargs):
    # you don't need to know what kwargs they may use ,see line 35
    print(mynumber, mystring, args, kwargs["name"], kwargs["age"])


mylist = [132, 32, 32, 4, 5]
function_with_all(123, "hello", *mylist, name="Jack",
                  age=15)  # compare the difference
function_with_all(123, "hello", mylist, name="Jack", age=15)


# how to actually connote a function:
def increment(number: int = 10, by: int = 20) -> tuple:
    return (number, number+by)


print(increment(number=3, by=1))

# how to use multiple input as parameter


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(1, 2, 3, 4, 5))

# how to use keywords argument in function


def save_user_info(**user_info):
    print(user_info["name"])


save_user_info(id=1, name="admin")

# python , in python there are two types of scopes, local variables with function scope and the global variable with file scope.In python there no block level scope.
# odd cases, python create a new local variable in function if you call global variable with in a function with the same value as the globle variable. in order to actually call a global variable within a function, you need to declear it explicitly. difference bewtween the following two functions:
# using global variable within a function is bad practice.
message = "a"


def greeting():
    global message
    message = "b"
# This is Bad ,calling global variable in functions


def greeting2():
    message = "b"
