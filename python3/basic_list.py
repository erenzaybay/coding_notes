target=[]                                   # intializing a list variable
target=[0,1,2,3,4,5]                        # you can assign values
target2=[1,2,"hello",["what",1,(23,45,"t")]]# it can has complicated nesting
lista=[1,2,3,4]
listb=["a","b","c","d"]
list_together=lista+listb                   # you can concatenate the list
print(list_together)
print(target)
target[3]="three"                           # you can change the element in the list
target2[3][0]="where"                       # changeing the element in nested list
print(target2)
target=[0,1,2,3,4,5,6,7,8,9,10]             # you can change the entire content of the list
target.append("another element")            # it adds an element at the end of the list
print(target)
target.remove("another element")            # it remove only the first instance of the element
print(target)
del(target[0])                              # it delete the exact list according to the index given
target.insert(0,"frist element")            # it add an element at the place accoding tot he index
print(target)
evaluation= (3 in target)                   # check for wether element 3 is in the list, return boolean
print(evaluation)
evaluation= (3 not in target)               # check for wether element 3 is not in the list,return boolean
print(evaluation)

target.extend(range(5))                      # if you want to extend the list with a iterable object
target.extend(target2)
target.extend(("a","b","c"))
print(target)

target.insert(5,"inserted element")          # insert an element ,other element move an index back
print(target)

print(list(range(10)))                      # you can change iterable object in to list
print(list({"a":1,"b":2,"c":3}))            # get a list of keys ["a","b","c"]

print(listb.count("a"))                     # count the number of 'a' in the list
print(listb.index("a"))                     # give the index of the first occurance of "a"

target4=[1,2,3,4,5,6,7,8,9]
outlast=target4.pop()                           # it push out the last element of target4, and assign it to outlast
print(outlast,"$$$",target4)
outfirst=target4.pop(0)                     # it push out the first elemnt of target4, and assign it to outfrist
print(outfirst,"$$$",target4)
outindex=target4.pop(3)                     # it push out the element of your choosing 
print(outindex,"$$$",target4)



# using list as a stack, first one in first one out

target3=[1,2,3,4]
a=target3.pop()                             # it push out the last element of target3, and assign it to a
print("list as stack",target3,f"a={a}")

# using list as a deque, first one in last one out

from collections import deque                # import deque module
target3=[1,2,3,4]
queue=deque(target3)                        # create deque object
a=queue.popleft()                           # it push out the first element of queue,and assign it to a
print("list as deque",queue,f"a={a}")
