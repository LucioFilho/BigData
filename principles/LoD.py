# Law of Demeter (LoD) or Principle of Least Knowledge:
'''
This design guideline for developing software, particularly object-oriented programs, 
states that a given object should assume as little as possible about the structure or properties 
of anything else (including its subcomponents).
'''

'''
The Law of Demeter (LoD), also known as the Principle of Least Knowledge, 
is a design guideline for developing software, particularly object-oriented programs. 
It suggests that a unit should only communicate with its immediate friends and not talk to strangers. 
This law is intended to promote loose coupling and increase modularity in the system. 
Here are examples illustrating both adherence to and violation of the LoD:
'''
# Employee-Manager Relationship:
# Violation: Accessing a method of an object that is not directly accessible.
class Employee:
    def get_manager(self):
        # Returns manager object
        pass

class Project:
    def __init__(self, employee):
        self.employee = employee

    def get_manager_name(self):
        return self.employee.get_manager().get_name()
'''
In this example, Project class is violating the Law of Demeter by reaching through the 
Employee object to get the Manager object and then calling get_name on it.
'''
# Adhering to LoD:
class Employee:
    def get_manager_name(self):
        return self.get_manager().get_name()

class Project:
    def __init__(self, employee):
        self.employee = employee

    def get_manager_name(self):
        return self.employee.get_manager_name()
'''
Here, Project only interacts with Employee, adhering to the Law of Demeter 
by not reaching through objects to call methods on a returned object.
'''

# Object Navigation in a Car-Engine Relationship:
# Violation: Directly accessing methods of a deeply nested structure.
class Car:
    def get_engine(self):
        # Returns engine object
        pass

class Driver:
    def start_car(self, car):
        car.get_engine().start()
'''
This violates the LoD because Driver directly calls a method on the object returned by Car.get_engine().
'''
# Adhering to LoD:
class Car:
    def start_engine(self):
        self.get_engine().start()

class Driver:
    def start_car(self, car):
        car.start_engine()
'''
Now, Driver only calls methods on Car, and Car is responsible for its internals, 
including starting the engine, thus adhering to the Law of Demeter.
'''

# User and Address Verification:
# Violation: Asking for an object to get to another object.
class User:
    def get_address(self):
        # Returns address object
        pass

class AddressVerificationSystem:
    def verify_user_address(self, user):
        if user.get_address().is_valid():
            # Verify the address
            pass
'''
This is a violation because AddressVerificationSystem is directly calling is_valid 
on the object returned by user.get_address().
'''
# Adhering to LoD:
class User:
    def is_address_valid(self):
        return self.get_address().is_valid()

class AddressVerificationSystem:
    def verify_user_address(self, user):
        if user.is_address_valid():
            # Verify the address
            pass
'''
In this approach, AddressVerificationSystem only interacts with User, 
and User takes care of delegating the call to its address, adhering to the Law of Demeter.
'''

# General Principle
'''
The general principle behind LoD is to reduce dependencies between components, 
which simplifies the system architecture and makes the software easier to maintain and modify. 
By ensuring that objects don't reveal their internal structures and depend only on their direct relationships, 
software designs can be more modular and robust.
'''