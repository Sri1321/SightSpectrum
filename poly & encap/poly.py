## in build polymorphism
print(len("geeks"))
print(len([10, 20, 30]))

# Polymorphism using sample function

def add(x, y, z=0):
	return x+y+z
print(add(2, 3))
print(add(2, 3, 4))

##pilymorphism with class methods:
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

# Polymorphic method
def make_sound(animal):
    print(animal.sound())

# Create instances of different classes
dog = Dog()
cat = Cat()

# Call the polymorphic method with different objects
make_sound(dog)  # Output: Woof!
make_sound(cat)  # Output: Meow!

##Polymorphism with inheritance
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Polymorphic method
def print_area(shape):
    print("Area:", shape.area())

# Create instances of different subclasses
rectangle = Rectangle(5, 3)
circle = Circle(4)

# Call the polymorphic method with different objects
print_area(rectangle)  # Output: Area: 15
print_area(circle)     # Output: Area: 50.24

##method overriding
class Shape:
    def area(self):
        print("Calculating area in Shape class")

class Rectangle(Shape):
    def area(self):
        print("Calculating area in Rectangle class")

class Circle(Shape):
    def area(self):
        print("Calculating area in Circle class")

# Create instances of different subclasses
rectangle = Rectangle()
circle = Circle()

# Call the overridden method
rectangle.area()  
circle.area()



##Encapsulation:
##with public members
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is", self.name, "and I am", self.age, "years old.")



person = Person("John", 25)


person.greet()           
print(person.name)       
print(person.age)        

person.age = 30
print(person.age)


##protected members

class Base:
	def __init__(self):

		
		self._a = 2


class Derived(Base):
	def __init__(self):

		
		Base.__init__(self)
		print("Calling protected member of base class: ",
			self._a)

		
		self._a = 3
		print("Calling modified protected member outside class: ",
			self._a)


obj1 = Derived()

obj2 = Base()

# Calling protected member
# Can be accessed but should not be done due to convention
print("Accessing protected member of obj1: ", obj1._a)

# Accessing the protected variable outside
print("Accessing protected member of obj2: ", obj2._a)

##private members:
class Person:
    def __init__(self, name, age):
        self.__name = name  # Private member
        self.__age = age  

    def __display_info(self):
        print("Name:", self.__name)
        print("Age:", self.__age)



person = Person("John", 25)


person._Person__display_info()






