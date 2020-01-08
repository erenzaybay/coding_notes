class Animal:                                                              # This is the parent class

    def mew(self):                                                         # it has new ,bark ,behappy ,there 3 methods
        print("Miao, miao, miao")

    def bark(self):
        print("Wuff, wuff, wuff")

    def behappy(self):
        print(" I love my owner!")

    def walking(self):
        print(" I am walking!")

class Dog(Animal):                                                         # declaring that it is a child of Animal
    
    def mew(self):                                                         # mew() have been overwriten by the local mew()
        print("I am a dog, I can not mew , mewing is for losers!")         # walking() is not overwriten

    def behappy(self):                                                     # behappy() is over writen ,but parent behappy()
        print(" I wave my tail and I am drooling!")                        # can be accessed by using super().behappy()
        self.bark()
        super().behappy()

class Cat(Animal):                                                         # put parent class in the bracket

    def bark(self):
        print(" I am a cat , I refuse to make that unpleasent noise!")

    def behappy(self):
        print(" I am caressing you, I am purring!")
        self.mew()
        super().behappy()
        
def in_the_garden(pet):
    print("The pet is in the garden.")
    pet.bark()
    pet.mew()
    pet.behappy()
    pet.walking()

wangcai=Dog()

huahua=Cat()

for pet in (wangcai,huahua):
    pet.mew()
    pet.bark()
    pet.behappy()
    pet.walking()


for pet in (wangcai,huahua):
    in_the_garden(pet)

