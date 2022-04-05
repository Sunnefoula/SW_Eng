class Animal:
    friends=[]

    def __init__(self,height=100, weight=100):
        self.height= height
        self.weight= weight
        self._private_weight=50
        self.__very_private_weight =30

    def print_height(self):
        print(f'this animal has height of {self.get_height()}')


    def get_height(self):
        return self.height

    def get_fur_colour(self):
        return self.fur_color

    def get_friends(self):
        return self.friends

    def greet(self):
        print("no sound")


class Dog(Animal):
    def __init__(self, height, weight, fur_color):
        self.fur_color= fur_color
        super().__init__(weight=weight, height=height)

    @staticmethod
    def greet(greeting): #doesn t depend on anything in the class, no need for self
       print(f"{greeting}")

    @classmethod
    def greetDog(self):
        print("woof woof!")  # no need for initialization

# initialize
sample_dog=Dog(50,25,"brown")
print(sample_dog.fur_color,sample_dog.get_height())
sample_dog.print_height()
sample_dog.greet("woof")

Dog.greetDog()
print("dog s friend are: ", Dog.friends) #global attributes of class

