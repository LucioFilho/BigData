# Open/Closed Principle (OCP):
'''
Also introduced by Bertrand Meyer and popularized by Robert C. Martin, 
this principle states that software entities (classes, modules, functions, etc.) 
should be open for extension but closed for modification.
'''

'''
The Open/Closed Principle (OCP), one of the SOLID principles introduced by Bertrand Meyer, 
states that software entities (classes, modules, functions, etc.) should be open for extension 
but closed for modification. This means that the behavior of a module can be extended without modifying 
its source code. Here are examples illustrating the application of the OCP:
'''

# Shape Rendering System:
# Violation: Adding a new shape requires modifying the existing ShapeRenderer class.
class Circle:
    def draw(self):
        print("Drawing a circle")

class Square:
    def draw(self):
        print("Drawing a square")

class ShapeRenderer:
    def render(self, shapes):
        for shape in shapes:
            if isinstance(shape, Circle):
                shape.draw()
            elif isinstance(shape, Square):
                shape.draw()
'''
To add a new shape, you would need to modify the ShapeRenderer class, violating OCP.
'''
# Adhering to OCP:
'''
Introduce an abstract Shape class with a draw method. Each shape implements this interface, 
and ShapeRenderer only depends on this abstraction.
'''
class Shape:
    def draw(self): pass

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Square(Shape):
    def draw(self):
        print("Drawing a square")

class ShapeRenderer:
    def render(self, shapes):
        for shape in shapes:
            shape.draw()
# Now, adding a new shape does not require any changes to ShapeRenderer.

# Discount Calculation System:
# Violation: A discount calculation system that needs modification each time a new discount type is added.
class Order:
    def __init__(self, total, discount_type):
        self.total = total
        self.discount_type = discount_type

    def final_total(self):
        if self.discount_type == "fixed":
            return self.total - 10  # Fixed discount
        elif self.discount_type == "percent":
            return self.total * 0.9  # 10% discount
# Adding a new discount type requires modifying the Order class, violating OCP.

# Adhering to OCP:
# Use polymorphism to extend discount types without modifying existing code.
class Discount:
    def apply(self, total): pass

class FixedDiscount(Discount):
    def apply(self, total):
        return total - 10

class PercentDiscount(Discount):
    def apply(self, total):
        return total * 0.9

class Order:
    def __init__(self, total, discount: Discount):
        self.total = total
        self.discount = discount

    def final_total(self):
        return self.discount.apply(self.total)
# With this design, adding new discount types doesn't require changing the Order class.

# Logging Framework:
'''
Violation: A logging system that needs to be modified to add support for
new logging targets (e.g., file, console, network).
'''
class Logger:
    def log(self, message, target):
        if target == "file":
            # Logic to log to a file
            pass
        elif target == "console":
            # Logic to log to the console
            pass
'''
Adding a new logging target requires modifying the Logger class, violating OCP.
'''
# Adhering to OCP:
# Define a logging interface and implement it for each logging target.
class LogTarget:
    def log(self, message): pass

class FileLogTarget(LogTarget):
    def log(self, message):
        # Logic to log to a file

class ConsoleLogTarget(LogTarget):
    def log(self, message):
        # Logic to log to the console

class Logger:
    def __init__(self, targets: list[LogTarget]):
        self.targets = targets

    def log(self, message):
        for target in self.targets:
            target.log(message)
# Now, adding a new logging target doesn't require any changes to the Logger class.

'''
These examples demonstrate how adhering to the Open/Closed Principle 
can make software systems more flexible and maintainable by reducing 
the need for modifications when extending their functionality.
'''
