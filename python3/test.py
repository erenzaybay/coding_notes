def function_mother(function, x):
    return function(x)


def function_child(a):
    return a*a


lalala = function_child
print(function_mother(lalala, 5))  # result is 25
