class Animal():

    def __init__(self,name):
        self.name = name
        print("ANIMAL CREATED!!")

    def speak(self):
        raise NotImplementedError("Please implement this abstract method")


class Dog(Animal):
    # class object attributes: same for any instance of the class
    species = 'mammal'

    def __init__(self, breed, name):
        Animal.__init__(self, name)
        # self: connects the attributes or method to the instance of the class.
        self.breed = breed
        self.name = name

    # magic-dunder methods

    def __str__(self):
        return f'A dog with a breed {self.breed} '

    # methods
    def speack(self):
        return self.name + " says woof"


class Cat(Animal):
    def speack(self):
        return self.name + " says meow"


dog = Dog(breed="Lab", name="huskie")
print(type(dog))

print(str(dog))
print(dog.breed)
# test class object attributes
print(dog.species)

dog2 = Dog('lab2', 'frankie')
print(dog2.breed)

# test polymorphism
fido = Dog('lab3', 'fido')
print(fido.speack())

isis = Cat('Isis')
print(isis.speack())