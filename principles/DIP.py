# Dependency Inversion Principle (DIP):
'''
This principle, part of the SOLID acronym alongside LSP, SRP, OCP, and ISP, states that high-level modules 
should not depend on low-level modules but both should depend on abstractions. 
Furthermore, abstractions should not depend on details; details should depend on abstractions.
'''

'''
The Dependency Inversion Principle (DIP) is a fundamental concept in object-oriented design that suggests 
high-level modules should not depend on low-level modules, but both should depend on abstractions. 
Additionally, abstractions should not depend upon details; details should depend upon abstractions. 
This principle aims to decouple software modules, making systems easier to manage, extend, and test. 
Here are examples illustrating the application of DIP:
'''

# Data Access Layer:
'''
Imagine a system where you have a high-level module ReportGenerator that needs to access data stored 
in a database. Instead of directly depending on a concrete MySQLDatabase class (a low-level module), 
you define an abstraction IDataAccess that ReportGenerator will depend on. 
Different database implementations can then implement this interface.
'''
class IDataAccess:
    def fetch_data(self): pass

class MySQLDatabase(IDataAccess):
    def fetch_data(self):
        # MySQL specific data fetching
        return "Data from MySQL"

class MongoDBDatabase(IDataAccess):
    def fetch_data(self):
        # MongoDB specific data fetching
        return "Data from MongoDB"

class ReportGenerator:
    def __init__(self, data_access: IDataAccess):
        self.data_access = data_access

    def generate_report(self):
        data = self.data_access.fetch_data()
        # Generate report using the data

# Notification System
'''
In a system where notifications can be sent through various channels (e.g., email, SMS), 
instead of coding directly against concrete notification implementations, 
you code against an abstraction (INotification). 
This allows for easy addition of new notification methods without modifying the consumer code.
'''
class INotification:
    def send(self, message): pass

class EmailNotification(INotification):
    def send(self, message):
        # Send email logic
        print(f"Email sent: {message}")

class SMSNotification(INotification):
    def send(self, message):
        # Send SMS logic
        print(f"SMS sent: {message}")

class NotificationService:
    def __init__(self, notifier: INotification):
        self.notifier = notifier

    def notify_user(self, message):
        self.notifier.send(message)

# Payment Processing:
'''
For an e-commerce application that supports multiple payment methods, 
define a payment interface (IPaymentProcessor) rather than coding against specific payment processors. 
This allows adding new payment methods without changing the code that processes payments.
'''
class IPaymentProcessor:
    def process_payment(self, amount): pass

class PayPalProcessor(IPaymentProcessor):
    def process_payment(self, amount):
        # PayPal processing logic
        print(f"Processing ${amount} via PayPal")

class StripeProcessor(IPaymentProcessor):
    def process_payment(self, amount):
        # Stripe processing logic
        print(f"Processing ${amount} via Stripe")

class PaymentService:
    def __init__(self, processor: IPaymentProcessor):
        self.processor = processor

    def make_payment(self, amount):
        self.processor.process_payment(amount)

# Logging Framework:
'''
In an application where logging is essential, instead of directly using a specific logging library, 
you can depend on a logging abstraction (ILogger). This makes it easy to switch between logging frameworks 
without impacting the application code.
'''
class ILogger:
    def log(self, message): pass

class FileLogger(ILogger):
    def log(self, message):
        # Log message to a file
        print(f"Log to file: {message}")

class ConsoleLogger(ILogger):
    def log(self, message):
        # Log message to console
        print(f"Log to console: {message}")

class Application:
    def __init__(self, logger: ILogger):
        self.logger = logger

    def do_something(self):
        # Application logic...
        self.logger.log("Operation performed")

'''
These examples demonstrate how DIP encourages the design of systems that are highly modular, 
with components that are easily interchangeable and extensible. 
By depending on abstractions rather than concrete implementations, 
software becomes more adaptable to change and easier to test.
'''
