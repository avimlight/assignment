# q1 Class:
# Attributes/Properties: These are the characteristics or data that describe the class. For example, if you have a class representing a "Car," the attributes might include make, model, year, color, etc.

# Methods/Functions: These are the actions or behaviors that the class can perform. Continuing with the "Car" example, methods might include starting the engine, stopping the engine, accelerating, braking, etc.

# Object:
# An object is an instance of a class. It is a specific realization of the class, with values assigned to its attributes.
# Here's a simple Python example:
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.is_running = False

#     def start_engine(self):
#         self.is_running = True
#         print(f"The {self.year} {self.make} {self.model}'s engine is now running.")

#     def stop_engine(self):
#         self.is_running = False
#         print(f"The {self.year} {self.make} {self.model}'s engine is now stopped.")

# # Creating objects (instances) of the Car class
# car1 = Car("Toyota", "Camry", 2020)
# car2 = Car("Honda", "Accord", 2021)

# # Using the objects
# car1.start_engine()
# car2.stop_engine()

# q2 The four pillars of object-oriented programming (OOP) are:

# 1. **Encapsulation:** This involves bundling the data (attributes) and the methods (functions) that operate on the data into a single unit, known as a class. It helps in hiding the internal details of the object and exposing only what is necessary.

# 2. **Abstraction:** Abstraction is the process of simplifying complex systems by modeling classes based on the essential properties and behaviors they share. It involves creating abstract classes with a common set of attributes and methods that can be inherited by more specific subclasses.

# 3. **Inheritance:** Inheritance allows a class (subclass or derived class) to inherit the properties and behaviors of another class (superclass or base class). It promotes code reusability and the creation of a hierarchy of classes.

# 4. **Polymorphism:** Polymorphism means "many forms." It allows objects of different classes to be treated as objects of a common superclass. It enables a single interface to represent different types of objects and allows for more flexible and modular code.

# These pillars collectively contribute to building robust, modular, and maintainable software through the principles of OOP.


# q3The `__init__()` function in Python is a special method, also known as a constructor, used to initialize the attributes of an object when it is created. It is automatically called when an object is instantiated from a class. The primary purpose of `__init__()` is to set the initial state of the object by assigning values to its attributes.

# Let's look at an example to illustrate this:

# ```python
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.is_hungry = True

#     def bark(self):
#         print("Woof!")

#     def eat(self):
#         self.is_hungry = False
#         print(f"{self.name} is now satisfied.")

# # Creating an instance of the Dog class
# my_dog = Dog(name="Buddy", age=3)

# # Accessing attributes and calling methods
# print(f"My dog's name is {my_dog.name}.")  # Output: My dog's name is Buddy.
# print(f"{my_dog.name} is {my_dog.age} years old.")  # Output: Buddy is 3 years old.

# my_dog.bark()  # Output: Woof!

# # Checking if the dog is hungry
# print(f"Is {my_dog.name} hungry? {'Yes' if my_dog.is_hungry else 'No'}")  # Output: Is Buddy hungry? Yes

# # Feeding the dog
# my_dog.eat()  # Output: Buddy is now satisfied.

# # Checking if the dog is hungry after eating
# print(f"Is {my_dog.name} hungry now? {'Yes' if my_dog.is_hungry else 'No'}")  # Output: Is Buddy hungry now? No
# ```

# In this example, the `__init__()` method initializes the `name`, `age`, and `is_hungry` attributes of the `Dog` class. When a `Dog` object (`my_dog`) is created, it automatically calls `__init__()` with the specified values for `name` and `age`. This helps ensure that each instance of the class starts with a defined initial state.


#q4In object-oriented programming (OOP), `self` is a convention used in many programming languages, including Python, to refer to the instance of the class. It is a reference to the current object being operated upon within a method or instance variable.

# Here's why `self` is used:

# 1. **Instance Reference:**
#    - When you create an instance of a class (an object), methods of that class have access to the instance through the `self` parameter. This allows the methods to operate on the specific attributes and methods of that instance.

# 2. **Avoid Ambiguity:**
#    - In a class, you might have both instance variables (attributes) and local variables within a method. Using `self` helps distinguish between instance variables and local variables, preventing ambiguity.

# 3. **Method Invocation:**
#    - When you call a method on an object (e.g., `my_object.my_method()`), the instance (`my_object`) is automatically passed as the first argument to the method. This allows the method to interact with the specific instance's data.

# 4. **Consistency:**
#    - The use of `self` provides consistency in method definitions across different instances of a class. It's a convention that makes code more readable and helps developers understand that a particular variable or method is related to the instance.

# Here's a simple example in Python:

# ```python
# class MyClass:
#     def __init__(self, x):
#         self.x = x

#     def print_value(self):
#         print(self.x)

# # Creating an instance of MyClass
# obj = MyClass(42)

# # Calling a method on the instance
# obj.print_value()  # Output: 42
# ```

# In the `print_value` method, `self` refers to the instance `obj`, allowing access to the `x` attribute specific to that instance. Without `self`, the method wouldn't know which instance's `x` to print.

#q5Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a new class (subclass or derived class) to inherit properties and behaviors from an existing class (superclass or base class). This promotes code reuse, modularity, and the creation of a hierarchy of classes.

# There are several types of inheritance:

# 1. **Single Inheritance:**
#    - In single inheritance, a subclass inherits from only one superclass.

#    ```python
#    class Animal:
#        def speak(self):
#            print("Animal speaks")

#    class Dog(Animal):
#        def bark(self):
#            print("Dog barks")

#    # Example usage
#    my_dog = Dog()
#    my_dog.speak()  # Output: Animal speaks
#    my_dog.bark()   # Output: Dog barks
#    ```

# 2. **Multiple Inheritance:**
#    - Multiple inheritance allows a subclass to inherit from multiple superclasses.

#    ```python
#    class Flyable:
#        def fly(self):
#            print("Can fly")

#    class Swimmable:
#        def swim(self):
#            print("Can swim")

#    class FlyingFish(Flyable, Swimmable):
#        pass

#    # Example usage
#    flying_fish = FlyingFish()
#    flying_fish.fly()   # Output: Can fly
#    flying_fish.swim()  # Output: Can swim
#    ```

# 3. **Multilevel Inheritance:**
#    - In multilevel inheritance, a class is derived from another class, and then another class is derived from this intermediate class.

#    ```python
#    class Vehicle:
#        def start_engine(self):
#            print("Engine started")

#    class Car(Vehicle):
#        def drive(self):
#            print("Car is being driven")

#    class SportsCar(Car):
#        def accelerate(self):
#            print("Sports car accelerating")

#    # Example usage
#    sports_car = SportsCar()
#    sports_car.start_engine()  # Output: Engine started
#    sports_car.drive()         # Output: Car is being driven
#    sports_car.accelerate()    # Output: Sports car accelerating
#    ```

# 4. **Hierarchical Inheritance:**
#    - In hierarchical inheritance, multiple classes inherit from a single base class.

#    ```python
#    class Shape:
#        def draw(self):
#            print("Drawing shape")

#    class Circle(Shape):
#        def draw(self):
#            print("Drawing circle")

#    class Rectangle(Shape):
#        def draw(self):
#            print("Drawing rectangle")

#    # Example usage
#    circle = Circle()
#    rectangle = Rectangle()

#    circle.draw()      # Output: Drawing circle
#    rectangle.draw()   # Output: Drawing rectangle
#    ```

# In each example, the derived classes inherit attributes and methods from their respective base classes, demonstrating different types of inheritance in OOP.

