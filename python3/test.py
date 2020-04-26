# using key word argument and unpacking tuple,list, and string
def function_unpacking(one_element, *keyword):
    print(one_element, end=" ")
    for i in keyword:
        print(i, end="|")
    print("\n")

# using key word argument and unpacking dictionary


def function_for_dictionary(**kwargs):
    for key in kwargs:
        print(key, kwargs[key])


dictionary_input = {"a": 1, "b": 2, "c": 3}
function_for_dictionary(**dictionary_input)
function_for_dictionary(name="Eren", Age="33", gender="male")
