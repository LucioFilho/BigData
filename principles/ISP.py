# Interface Segregation Principle (ISP):
'''
Another principle from Robert C. Martin which states that no client should be forced to depend on methods 
it does not use. This principle leads to the development of narrowly tailored interfaces that "segregate" 
methods more granularly.
'''

'''
The Interface Segregation Principle (ISP), one of the SOLID principles introduced by Robert C. Martin, 
states that no client should be forced to depend on methods it does not use. 
This principle promotes the design of smaller, more focused interfaces rather than large, monolithic ones. 
Here are examples illustrating the application of the ISP:
'''

# Multi-Function Printer Scenario:
'''
Violation: A single interface for a multi-function printer that not all printers may support (e.g., fax, scan).
'''
class IMultiFunctionPrinter:
    def print(self, document):
        pass

    def scan(self, document):
        pass

    def fax(self, document):
        pass

class SimplePrinter(IMultiFunctionPrinter):
    def print(self, document):
        # Implementation
        pass

    def scan(self, document):
        raise NotImplementedError("Scan function is not supported.")

    def fax(self, document):
        raise NotImplementedError("Fax function is not supported.")

# ISP Application: Segregate the interface into smaller, specific interfaces.
class IPrinter:
    def print(self, document):
        pass

class IScanner:
    def scan(self, document):
        pass

class IFax:
    def fax(self, document):
        pass

class SimplePrinter(IPrinter):
    def print(self, document):
        # Implementation
        pass

class MultiFunctionPrinter(IPrinter, IScanner, IFax):
    def print(self, document):
        # Implementation
        pass

    def scan(self, document):
        # Implementation
        pass

    def fax(self, document):
        # Implementation
        pass

# Online Content Publishing:
'''
Violation: A single interface for managing online content, including videos, articles, and podcasts, 
where not all methods are relevant for each content type.
'''
class IContentManager:
    def publish_video(self, video):
        pass

    def publish_article(self, article):
        pass

    def record_podcast(self, podcast):
        pass

class ArticlePublisher(IContentManager):
    def publish_article(self, article):
        # Implementation
        pass

    # Forced to implement or leave empty
    def publish_video(self, video):
        pass

    def record_podcast(self, podcast):
        pass

# ISP Application: Create focused interfaces for each type of content.
class IVideoPublisher:
    def publish_video(self, video):
        pass

class IArticlePublisher:
    def publish_article(self, article):
        pass

class IPodcastRecorder:
    def record_podcast(self, podcast):
        pass

class ArticlePublisher(IArticlePublisher):
    def publish_article(self, article):
        # Implementation
        pass

# User Management System:
'''
Violation: A bulky interface for user operations that includes admin-specific operations 
like banning users, which regular users do not need.
'''
class IUserOperations:
    def create_post(self, post):
        pass

    def edit_profile(self, profile):
        pass

    def ban_user(self, user):
        pass

class RegularUser(IUserOperations):
    def create_post(self, post):
        # Implementation
        pass

    def edit_profile(self, profile):
        # Implementation
        pass

    def ban_user(self, user):
        raise PermissionError("Not allowed to ban users.")

# ISP Application: Separate user operations from admin operations.
class IUser:
    def create_post(self, post):
        pass

    def edit_profile(self, profile):
        pass

class IAdmin:
    def ban_user(self, user):
        pass

class RegularUser(IUser):
    def create_post(self, post):
        # Implementation
        pass

    def edit_profile(self, profile):
        # Implementation
        pass

class Admin(IUser, IAdmin):
    def create_post(self, post):
        # Implementation
        pass

    def edit_profile(self, profile):
        # Implementation
        pass

    def ban_user(self, user):
        # Implementation
        pass

'''
These examples demonstrate how adhering to the Interface Segregation Principle can lead to a cleaner, 
more maintainable, and more scalable codebase by ensuring that classes only implement the interfaces 
that are relevant to their functionality, thus avoiding the pitfalls of "fat" interfaces.
'''
