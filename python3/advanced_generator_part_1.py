# This is how you do it without knowing the generator and yield
def square_numbers(numbers_list):
    result=[]
    for i in numbers_list:
        result.append(i*i)
    return result

number_list=[1,2,3,4,5]

print(square_numbers(number_list))

#################################################################################################################################
# This is how you create a yield object
def generator_object(number_list):
    for i in number_list:
        yield i*i 

generator_object=generator_object(number_list)
print(type(generator_object))

"""
print(next(generator_object))
print(next(generator_object))
print(next(generator_object))
print(next(generator_object))
print(next(generator_object))
print(next(generator_object))  #if you do it once more ,you will get 'iteration stop' error because out of range
"""
for number in generator_object: # if you uncomment the last five next(),it will fail because we finished using the generator object     
    print("ok",number)

###################################################################################################################################
# generator is similar to the list comprehension

list_object=[ i*i for i in number_list]
print(type(list_object))
print(list_object)

generator_object_another=( i*i for i in number_list)
print(type(generator_object_another))
for i in generator_object_another:
    print("hello",i)

print(list(generator_object_another)) # It is empty because we have already printed it, comment out the for loop to try it



