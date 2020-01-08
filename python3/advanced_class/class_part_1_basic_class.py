class dog:

    eyes=2                                              # These are class attributes
    legs=4
    intelligence="smart"

    def __init__(self,name,age,color,temper):           # This initialized an instance using the argument given
                                                        # Using self is the convention      
        self._name=name                                 # These are instance attributes
        self._age=age                                   # the age on the left and right is not the same thing!
        self._color=color                               # the reason we use "_" is to mean it is local
        self._temper=temper                             # do not access them from the main programe, concept "encapsulation"

    def angry(self):                                    # This is instance methods
        print(f"{self._name} is angry, it barks at you!, because he has only {self.eyes} eyes!")
                                                        # Notice this is how you access class attribute in instance methods
    def introduction(self):
        print(f"Wuf!Wuf!my name is {self._name}, I am {self._age},my hair is {self._color}, and I am {self._temper}!")

    def change_color(self,color):
        self._color=color

    def getcolor(self):
        return self._color

    @staticmethod                                             # This is staticmethod, they can't access the instance
    def play():                                               # attribute or classmethod , it does it own thing
        print("The dog waved his tails and jumped around!")

    @staticmethod                                             # The @staticmethod is called decorater
    def bark():                                               # we need them to tell python that we 
        for i in range(7):                                    # are defining classmethod or static method
            print(f"It barks {i} times!")                     # instance methods do not need to have it

    @classmethod                                              # This is class method ,it can access the class attribute
    def dog_information(cls):                                 # but can not access the instance methods
        print(f"A dog has {cls.eyes} eyes,{cls.legs} legs, and They are {cls.intelligence}!")

mydog=dog("Wang cai",3,"brown","gentle")                      # This is how you create a dog class object
print(type(mydog))
# accessing the class attribute
print(mydog.eyes)
print(mydog.legs)
print(mydog.intelligence)

# calling the instance methods
mydog.angry()
mydog.introduction()

# calling the static methods
mydog.play()
mydog.bark()

#calling the class method
mydog.dog_information()

# never do this !!!!!!! You have to use instance method to acces the instance attributes!
# you can access it directly but not change it
mydog._color = "rainbow color"
print(f'never do this !: mydog._color = "{mydog._color}", never do it be cause of encaptulation!')

# also never do this , because you could make mistake.never access any variable in the class directly
the_color_of_dog_house=mydog._color

# the right way of doing things,using method to access the attributes
the_color_of_dog_house=mydog.getcolor()
print(the_color_of_dog_house)

mydog.change_color("black and white")
print(f'I have change the color of the dog to "{mydog._color}" in the correct way!')
