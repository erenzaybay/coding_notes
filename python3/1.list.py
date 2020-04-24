from collections import deque                # import deque module
target = []                                   # intializing a list variable
target = [0, 1, 2, 3, 4, 5]                        # you can assign values
# it can has complicated nesting
target2 = [1, 2, "hello", ["what", 1, (23, 45, "t")]]
lista = [1, 2, 3, 4]
listb = ["a", "b", "c", "d"]
list_together = lista+listb                   # you can concatenate the list
print(list_together)
print(target)
# you can change the element in the list
target[3] = "three"
# changeing the element in nested list
target2[3][0] = "where"
print(target2)
# you can change the entire content of the list
target = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# it adds an element at the end of the list
target.append("another element")
print(target)
# it remove only the first instance of the element
target.remove("another element")
print(target)
# it delete the exact element according to the index given
del(target[0])
# it add an element at the place according to the index
target.insert(0, "frist element")
print(target)
# check for wether element 3 is in the list, return boolean
evaluation = (3 in target)
print(evaluation)
# check for wether element 3 is not in the list,return boolean
evaluation = (3 not in target)
print(evaluation)

# if you want to extend the list with a iterable object
target.extend(range(5))
target.extend(target2)
target.extend(("a", "b", "c"))
print(target)

# insert an element ,other element move an index back
target.insert(5, "inserted element")
print(target)

# you can change iterable object in to list
print(list(range(10)))
# get a list of keys ["a","b","c"]
print(list({"a": 1, "b": 2, "c": 3}))

# count the number of 'a' in the list
print(listb.count("a"))
# give the index of the first occurance of "a"
print(listb.index("a"))

target4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# it push out the last element of target4, and assign it to outlast
outlast = target4.pop()
print(outlast, "$$$", target4)
# it push out the first elemnt of target4, and assign it to outfrist
outfirst = target4.pop(0)
print(outfirst, "$$$", target4)
# it push out the element of your choosing
outindex = target4.pop(3)
print(outindex, "$$$", target4)


# using list as a stack, first one in first one out

target3 = [1, 2, 3, 4]
# it push out the last element of target3, and assign it to a
a = target3.pop()
print("list as stack", target3, f"a={a}")

# using list as a deque, first one in last one out

target3 = [1, 2, 3, 4]
queue = deque(target3)                        # create deque object
# it push out the first element of queue,and assign it to a
a = queue.popleft()
print("list as deque", queue, f"a={a}")
