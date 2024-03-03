# Single Responsibility Principle (SRP):
'''
Established by Robert C. Martin, this principle states that every module or class should have 
responsibility over a single part of the functionality provided by the software, and that 
responsibility should be entirely encapsulated by the class.
'''

'''
The Single Responsibility Principle (SRP) is one of the SOLID design principles 
introduced by Robert C. Martin, which states that a class should have only one reason to change. 
This means that a class should only have one job or responsibility. 
Adhering to SRP makes software easier to understand and maintain. 
Here are examples illustrating the application of SRP:
'''

# User Management System:
'''
Violation: A class that handles both user data management and user notification responsibilities.
'''
class UserManager:
    def add_user(self, user):
        # Add user to the database
        pass
    
    def send_email(self, user, content):
        # Send an email to the user
        pass

# SRP Application: 
'''
Split the class into two: one for user management and another for handling user notifications.
'''
class UserDatabase:
    def add_user(self, user):
        # Add user to the database
        pass

class UserNotification:
    def send_email(self, user, content):
        # Send an email to the user
        pass

# Report Generation and Persistence:
'''
Violation: A class responsible for generating reports and also saving them to a file.
'''
class ReportGenerator:
    def generate_report(self, data):
        # Generate the report
        return report
    
    def save_report(self, report, filepath):
        # Save the report to a file
        pass

# SRP Application: 
'''
Separate the responsibilities into a report generation class and a report persistence class.
'''
class ReportGenerator:
    def generate_report(self, data):
        # Generate the report
        return report

class ReportSaver:
    def save_report(self, report, filepath):
        # Save the report to a file
        pass

# Employee Class Handling Multiple Responsibilities:
'''
Violation: An Employee class that calculates pay and generates employee reports.
'''
class Employee:
    def calculate_pay(self):
        # Calculate pay logic
        pass
    
    def generate_performance_report(self):
        # Generate performance report
        pass

# SRP Application: 
'''
Create separate classes for handling payroll and performance reporting.
'''
class Payroll:
    def calculate_pay(self, employee_id):
        # Calculate pay logic
        pass

class PerformanceReport:
    def generate(self, employee_id):
        # Generate performance report
        pass

# E-commerce Application:
'''
Violation: A single class handling order processing, payment, and email notifications.
'''
class OrderProcessor:
    def process_order(self, order):
        # Process the order
        pass
    
    def process_payment(self, payment_details):
        # Process payment
        pass
    
    def send_confirmation_email(self, order):
        # Send an email confirmation
        pass

#SRP Application: 
'''
Break down the class into dedicated classes for order processing, 
payment processing, and sending notifications.
'''
class OrderService:
    def process_order(self, order):
        # Process the order
        pass

class PaymentService:
    def process_payment(self, payment_details):
        # Process payment
        pass

class NotificationService:
    def send_confirmation_email(self, order):
        # Send an email confirmation
        pass

'''
Adhering to the Single Responsibility Principle helps in creating a system that is modular, 
where each class or module has a clear purpose. 
This not only makes the system easier to maintain and extend but also facilitates easier testing 
and management of dependencies.
'''
