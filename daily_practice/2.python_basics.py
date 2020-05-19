# number and operation

a = 1
b = 2

a+b
a-b
a*b
a/b
a**b
a//b
a % b

a += b
a -= b
a *= b
a /= b
a **= b
a //= b
a %= b

a, b = b, a


# The logic

if variable_1 is True:
    pass
elif variable_2 is True:
    pass
else:
    pass


for i in for_list:
    pass
    if something is True:
        break
else:
    "This only get executed when entire for loop is completed without 'break'"

for i in range(5, 8):
    print(i)


while contition is True:
    pass
    if somthing is True:
        break
else:
    "This only get executed when entire for loop is completed without 'break'"

for index, element in enumerate(trick_list):
    pass

for index, element in enumerate(trick_tuple):
    pass

for index, key in enumerate(trick_dict):
    pass

for index, element in enumerate(range(8)):
    pass

for key, value in trick_dict.items():
    print(key, value)


# list

target = []
target = [0, 1, 2, 3, 4, 5]
target2 = [1, 2, "hello", ["what", 1, (23, 45, "t")]]
the_list = list(range(10)))
the_list=list({"only": 0, "keys": 1, "will": 2, "become": 3, "elements"}))

new_list=old_list_a + old_list_b

target[3]="three"
target2[3][0]="where"


target=["the", "new", "content", "to", "replace", "the", "old", "one"]
target.append("another element")


target.remove("only the first instance")


del(target[0])
target.insert(0, "first element")

evaluation=(3 in target)
evaluation=(3 not in target)

target.extend(range(5))
target.extend(target2)
target.extend(("a", "b", "c"))


target.insert(5, "inserted element,other's move back")


listb.count("how many of this element")
listb.index("index of the first occurrance")

outlast=["pop out the last element"].pop()
outfirst=target4.pop(0)
outindex=target4.pop(3)

target3=["list", "as", "a", "stack", "first",
    "one", "in", "first", "one", "out"]
a=target3.pop()


from collections import deque
target3=["list", "as", "deque", "fist", "one", "in", "last", "one", "out"]
queue=deque(target3)
a=queue.popleft()








# Dictionary

target={}
target={"Damein": "Whiplash", "Speilberg": "Jaw"}
target2=dict(eren="hangzhou", adina="shanghai")

element=target.get("eren", "default value when not found")

target["new key"]="new value"
target["old key"]="new value"

element=target.pop("name of the key, also remove this value pair")
del target["delete key value pair of this key"]

dict3=dict(**dict1, **dict2)
dict4=dict(x=5, z=8, **dict1)

"key" in dict4
"key" not in dict4

class_keys_object=target.keys()
keys_list=list(keys_object)

class_values_object=target.values()
values_list=list(values_object)

target.clear()

del target

# string

target1="Is your code name '007'"
target2='a'
target="have to add"
target[0]
target[1]

# first included, last one not included
target[3:8]
target[3:]
target[:3]
target[:]
print(target[-1])
print(r"good for path'c:/windows/secret/topsecret', or 'regular expression'")
print(f"Your line is {target},and {target}")

target3='''\
This is how you use long string,
 "\" in the first line will be ignored.
'''

print("Your line is {},and {}".format(target, target2))

string_1, string_2, string_3="one", "two", "three"
print("The second is {1}, the third one is {2}, and the first one is {0}".format(
    string_1, string_2, string_3))

# you can use a dictionary, and the same variable can be refereed many times
num_1=111
num_2=222
my_dictionary=dict(foo=num_1, bar=num_2)
print("The big number is {bar}, the small number is {foo}, the small number is {foo}".format(
    **my_dictionary))

"A MOVIE IS A GOOD ONE".upper()
"A Movie Is A Good One".capitalize()
"a movie is a good one".lower()
"a mOVIE iS a gOOD oNE".swapcase()

target3.find("return the index of the first occurrance")

target3.replace("to be replaced element,all occurrance", "the new element")

"ttt123ttt".strip("ttt")
"    the white space  ".strip()

"only remove white space at end of the line   ".rstrip()
"this string has a new line ending\n".rstrip("\n")
"only remove if it exist".rstrip("st")

"abcdefg123".isalnum()

list_object="Default is splitting at white space".split()

list_object="Or you can specify a rule".split("o")

joined_words_1=" ".join(word_list_1)    # joined by " "
joined_words_2="@@".join(word_list_1)   # joined by "@@"




# tuple

tuple_2=("a", "b", "c", "d", "e", "a", "a")
tuple_single=("notice the comma",)

a=tuple_1[0]
b=tuple_2[-2]

a=len(("find ", " the", "length", "of ", "the", "tuple"))
a=min(("smallest", "element"))
a=max(("biggest", "element"))

a=tuple(range(10))
a=tuple({"get": 1, "the": 2, "keys": 3})

evaluation=(3 in tuple_1)
evaluation=(3 not in tuple_1)

number_of_a=tuple_2.count("how many this element in this tuple")

tuple_2.index("the index of the first occurrance of this element"))


















# small infos

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

PI=3.14  # using Uppercase to indicate the constant, python don't really have constant
