####sample example
##class Person:
##  def __init__(self, name, age):
##    self.name = name
##    self.age = age
##
##p1 = Person("jhon",23)
##
##print(p1.name,p1.age)
##
##
####using function
##class MyClass:
##    def __init__(self, name):
##        self.name = name
##    
##    def greet(self):
##        return f"Hello, {self.name}!"
##
##obj = MyClass("John")
##print(obj.greet())


##Default parameter:
##class Default():
##    
##    #defining default constructor
##    def __init__(self):
##        self.var1 = 56
##        self.var2 = 27
##        
##    #class function for addition
##    def add(self):
##        print("Sum is ", self.var1 + self.var2)
##
##obj = Default()     
##obj.add()

####Parametarised construtor:
##class Default():
##    
##    #defining parameterised constructor
##    def __init__(self, n1, n2):
##        self.var1 = n1
##        self.var2 = n2
##        
##    #class function for addition
##    def add(self):
##        print("Sum is ", self.var1 + self.var2)
##
##obj = Default(121, 136)             
##obj.add()





##init method using default parameter:
##class Teacher:
##    # definition for init method or constructor with default argument
##    def __init__(self, name = "Preeti Srivastava"):
##        self.name = name
##     # Random member function
##    def show(self):
##        print(self.name, " is the name of the teacher.")
##        
##t1 = Teacher()                             #name is initialised with the default value of the argument
##t2 = Teacher('Chhavi Pathak')    #name is initialised with the passed value of the argument
##t1.show()
##t2.show()



class MyClass:
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return f"MyClass with value: {self.value}"

obj = MyClass(10)
print(obj)  # Output: MyClass with value: 10


