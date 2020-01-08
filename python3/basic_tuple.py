# The difference between tuple and list is list is mutable ,and tuple is imutable

tuple_1=1,2,3,4,5                            # this way , simple ,but do not use it
tuple_2=("a","b","c","d","e","a","a")        # another ,mor clear way of creating a tuple

tuple_single=(1,)                            # This is how you creat a sigle element tuple ,notice the ","

integer_1=(1)                                # notice , the result is an integer 1, not a tuple

print(tuple_1[0])                            # you can refer to element with the index
print(tuple_2[-2])

print(len(tuple_1))                          # find the length of the tuple

print(min(tuple_1))                          # find the smallest number


print(max(tuple_1))                          # fing the bigest number

print(tuple(range(10)))                      # change an iterable object into a tuple

print(tuple({"a":1,"b":2,"c":3}))            # get a tuple of keys ("a","b","c")

evaluation= (3 in tuple_1)                   # check for wether element 3 is in the tuple, return boolean
print(evaluation)
evaluation= (3 not in tuple_1)               # check for wether element 3 is not in the tuple,return boolean
print(evaluation)

number_of_a=tuple_2.count("a")               # count the number of "a" is the tuple
print("There are ",number_of_a," 'a' in the tuple_3")

print(tuple_2.index("d"))                    # the index of the first occurance of "d"

