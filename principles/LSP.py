'''
The Liskov Substitution Principle (LSP) 
Is one of the five SOLID principles of object-oriented programming 
and design, introduced by Barbara Liskov in a 1987 conference keynote. The principle defines that objects 
of a superclass should be replaceable with objects of a subclass without affecting the correctness of the 
program. In other words, instances of the subclass should be able to substitute instances of the superclass 
without altering the desirable properties of the program (correctness, task performed, etc.).

A violation of the Liskov Substitution Principle occurs when a subclass does not support the same behavior 
or expectations as its superclass. When a subclass cannot be used interchangeably with its superclass, it 
can lead to unexpected behaviors and bugs in the code that uses these classes. Here are some common 
scenarios that can lead to LSP violations:

Method Signature Changes: If a subclass changes the signature of a method in a way that is not compatible 
with the superclass, it violates LSP. This can include changing the return type, input parameters, 
or throwing new exceptions.

Weakening Preconditions: If the subclass requires more stringent conditions to function compared to the 
superclass, it violates LSP. For example, if the superclass method accepts null inputs but the subclass 
method throws an exception when passed null.

Strengthening Postconditions: If the subclass guarantees less than the superclass after the method is 
executed, it violates LSP. For instance, if the superclass method guarantees that the returned value will 
not be null, but the subclass method can return null.

Changing the Invariant Behaviors: Classes often have invariants, conditions that must always hold true 
throughout the life of an object. If a subclass changes these invariants, it can lead to LSP violations.

Altering the Expected Behavior: If a subclass alters the expected behavior of a method such that it no longer 
does what the method in the superclass was intended to do, even if the signature remains the same, it can 
violate LSP.
'''

'''
The Liskov Substitution Principle encourages us to ensure that our subclassing and inheritance structures 
are designed properly so that any derived class can be used in place of their base class without any issues. 
This leads to more robust, maintainable, and reusable code.
'''

# simple example of an LSP violation:
class Bird:
    def fly(self):
        return "I can fly!"

class Ostrich(Bird):
    def fly(self):
        raise NotImplementedError("I can't fly!")

'''
In this example, the Ostrich class violates LSP because it changes the behavior of the fly method. 
Even though Ostrich is a subclass of Bird, it cannot be used interchangeably with Bird since calling fly 
on an Ostrich instance would result in a NotImplementedError, which is not expected from a Bird instance.
'''

# Method Signature Changes:
class CoffeeMachine:
    def brew_coffee(self, amount):
        return f"Brewing {amount}ml of coffee."

class AdvancedCoffeeMachine(CoffeeMachine):
    def brew_coffee(self, amount, coffee_type):
        return f"Brewing {amount}ml of {coffee_type} coffee."

'''
Violation: The AdvancedCoffeeMachine changes the method signature by adding an additional parameter, 
coffee_type, which is not present in the superclass CoffeeMachine. This means the subclass cannot be used 
as a drop-in replacement for the superclass.
'''

# Weakening Preconditions:
class PaymentProcessor:
    def process_payment(self, amount, account):
        if account is None:
            raise ValueError("Account cannot be null")
        # Process the payment

class StrictPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount, account):
        if amount <= 0 or account is None:
            raise ValueError("Amount must be positive and account cannot be null")
        # Process the payment

'''
Violation: The StrictPaymentProcessor adds an additional precondition that the amount must be positive, 
which is not required by the PaymentProcessor. This makes the preconditions for using the subclass more 
restrictive than those for the superclass.
'''

# Strengthening Postconditions:
class Rectangle:
    def set_width(self, width):
        self.width = width
    def set_height(self, height):
        self.height = height

class Square(Rectangle):
    def set_width(self, width):
        self.width = self.height = width
    def set_height(self, height):
        self.width = self.height = height

'''
Violation: By enforcing that width and height must always be the same, the Square subclass strengthens 
the postconditions of the methods set_width and set_height of the Rectangle superclass, thus violating LSP 
because a Square cannot be substituted wherever a Rectangle is expected.
'''

# Changing the Invariant Behaviors:
class ReadOnlyFile:
    def read(self):
        return "Reading data"

class WriteableFile(ReadOnlyFile):
    def write(self, data):
        if not self.is_write_permitted:
            raise PermissionError("File is not writable")
        # Write data

'''
Violation: WriteableFile introduces an invariant related to write permissions that is not present in 
ReadOnlyFile. If is_write_permitted is False, calling write will raise an error, changing the behavior 
expected from the ReadOnlyFile class.
'''

# Altering the Expected Behavior:
class Vehicle:
    def start_engine(self):
        return "Engine started"

class ElectricCar(Vehicle):
    def start_engine(self):
        return "Error: No engine to start"

'''
Violation: The ElectricCar class alters the expected behavior of the start_engine method from the Vehicle 
superclass by indicating there is no engine to start, even though the method signature is the same. 
This behavior is different from what is expected when starting an engine in a typical vehicle, 
thus violating LSP.
'''

# ADVANCED LSP VIOLATIONS

# Complex State Mutations:
'''
Suppose you have a complex object graph where state changes in one object can affect the state in another. 
A subclass that alters the way state is changed or propagated can violate LSP because the same sequence of 
operations on the subclass does not lead to the same result as with the superclass.
'''
class DataPipeline:
    def process_data(self, data):
        self.transform(data)
        return self.export(data)

    def transform(self, data):
        # perform transformations
        pass

    def export(self, data):
        # export data
        pass

class FilteringDataPipeline(DataPipeline):
    def transform(self, data):
        # perform transformations
        data.filter_sensitive_information()  # new behavior not in superclass

'''
Violation: The FilteringDataPipeline introduces a new behavior in the transform method that filters out 
sensitive information. If the DataPipeline class's clients do not expect this filtering, it violates LSP.
'''

# Breaking Interface Segregation:
'''
When a subclass inherits from a superclass that has more functionality than the subclass needs, 
and the subclass cannot fully implement the superclass's interface without some of these methods 
doing nothing or throwing exceptions, it violates both the Interface Segregation Principle and LSP.
'''
class AllPurposePrinter:
    def print(self, document):
        # print the document
        pass

    def scan(self, document):
        # scan the document
        pass

class PrintOnlyPrinter(AllPurposePrinter):
    def scan(self, document):
        raise NotImplementedError("This printer can only print")

'''
Violation: The PrintOnlyPrinter cannot fulfill the contract of AllPurposePrinter because it cannot scan, 
so it should not inherit from it.
'''

# Temporal Coupling:
'''
When methods must be called in a certain order in the superclass, and the subclass changes that order or 
the conditions under which certain methods can be called, this can be a subtle violation of LSP.
'''
class Transaction:
    def begin(self):
        # begin the transaction
        pass

    def commit(self):
        # commit the transaction
        pass

class AutoCommitTransaction(Transaction):
    def begin(self):
        super().begin()
        super().commit()  # commits immediately

'''
Violation: AutoCommitTransaction changes the expected behavior of a transaction by committing immediately 
upon beginning, which may not be expected by users of Transaction.
'''

# Contravariant Method Parameter Types:
'''
In some languages, replacing a method parameter with a subtype in the subclass (contravariant parameter typing) 
can lead to LSP violations because the subclass method cannot accept all the same inputs 
as the superclass method.
'''
class EventListener:
    def handle_event(self, event: Event):
        # handle the event
        pass

class MouseEventListener(EventListener):
    def handle_event(self, event: MouseEvent):  # MouseEvent is a subclass of Event
        # handle only mouse events
        pass

'''
Violation: The MouseEventListener cannot handle generic Event objects even though it's a subclass of 
EventListener, which can.
'''

# Invariant Contraction:
'''
If a subclass narrows the range of allowable values for an attribute compared to its superclass, 
it can violate LSP because the subclass cannot be used wherever the superclass can be used.
'''
class UserAccount:
    def set_age(self, age: int):
        if not (0 < age < 150):
            raise ValueError("Invalid age")
        self._age = age

class TeenagerAccount(UserAccount):
    def set_age(self, age: int):
        if not (13 <= age <= 19):
            raise ValueError("Not a teenager age")
        super().set_age(age)

'''
Violation: TeenagerAccount cannot accept the full range of ages that UserAccount can, so it cannot substitute 
for UserAccount without potentially breaking the program.
'''

# COMPLEX LSP VIOLATIONS
'''
Complex LSP violations often occur in systems where behavior is emergent from interactions between components 
rather than from a single unit of code. One of the most complex and subtle LSP violations involves violations 
of behavioral semantics, which can happen in distributed systems, concurrent programming, or when implementing 
plugins or modules that must adhere to certain protocols.
'''

# Here's a conceptual example that illustrates a complex LSP violation in the context of a distributed system:

# Distributed Transactions in Microservices Architecture:
'''
Imagine a microservices architecture where each service handles its own transactions. 
There's a base TransactionService class that each microservice's transaction class extends. 
The base class defines a contract for starting, committing, and rolling back transactions.
'''
class TransactionService:
    def start_transaction(self):
        # Start a new transaction
        pass
    
    def commit(self):
        # Commit the transaction
        pass
    
    def rollback(self):
        # Roll back the transaction
        pass

'''
Each microservice implements its own version of a transaction according to its data store. 
However, a new microservice is introduced with eventual consistency requirements, 
which means that its transactions are not immediately consistent and can take time 
to propagate through the system.
'''
class EventualConsistencyTransactionService(TransactionService):
    def start_transaction(self):
        # Start a new transaction with eventual consistency
        pass
    
    def commit(self):
        # Commit the transaction with the possibility of it being eventually consistent
        pass
    
    def rollback(self):
        # Rollback cannot be guaranteed immediately due to eventual consistency
        pass

'''
Violation:

The EventualConsistencyTransactionService violates LSP because it cannot guarantee an 
immediate rollback due to the nature of eventual consistency. 

Clients using TransactionService expect that when they call rollback, 
the transaction is immediately rolled back, which is not the case with the eventual consistency model.

The EventualConsistencyTransactionService cannot be used as a drop-in replacement for TransactionService 
in contexts where immediate consistency is required.

This example is complex because it requires an understanding of distributed system design, 
consistency models, and transactional integrity. The violation is not in the method signatures or even 
in the immediate effects of method calls, but in the overall behavior and guarantees of the system. 
Replacing a TransactionService that guarantees immediate consistency with one that only provides eventual 
consistency can lead to subtle bugs and system failures that are difficult to predict and diagnose, as they 
depend on the timing and order of operations, which are not always controlled in a distributed system.
'''
