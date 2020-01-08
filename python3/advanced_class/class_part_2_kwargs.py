class dog:

    eyes=2                                              # These are class attributes
    legs=4
    intelligence="smart"

    def __init__(self,**kwargs):                        # This is called keyword argumnet
        self._name=kwargs.get("name")                   
        self._age=kwargs.get("age",None)                # if there of default value, it is usually declared explicitly
        self._color=kwargs.get("color","white")         # You can even give it default values
        self.temper=kwargs.get("temper","gentle")

    def angry(self):                                    # This is instance methods
        print(f"{self._name} is angry, it barks at you!, because he has only {self.eyes} eyes!")
                                                        # Notice this is how you access class attribute in instance methods
    def introduction(self):
        print(f"Wuf!Wuf!my name is {self._name}, I am {self._age},my hair is {self._color}, and I am {self._temper}!")

    def change_color(self,color):
        self._color=color

    def getcolor(self):
        return self._color

    def getname(self):
        return self._name


gooddog=dog()

print("the gooddog's name is ",gooddog.getname(),",and it's color is ",gooddog.getcolor())

baddog=dog(name="bad dude",color="black")


print("the baddog's name is ",baddog.getname(),",and it's color is ",baddog.getcolor())
"""
# This is our olde way of initializing an object

    def __init__(self,name,age,color,temper):           # This initialized an instance using the argument given
                                                        # Using self is the convention      
        self._name=name                                 # These are instance attributes
        self._age=age                                   # the age on the left and right is not the same thing!
        self._color=color                               # the reason we use "_" is to mean it is local
        self._temper=temper                             # do not access them from the main programe, concept "encapsulation"
"""


