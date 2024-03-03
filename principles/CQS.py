# Command-Query Separation (CQS):
'''
Proposed by Bertrand Meyer, this principle states that every method should either be a command that 
performs an action, or a query that returns data to the caller, but not both.
'''

'''
Command-Query Separation (CQS) is a principle in computer science, proposed by Bertrand Meyer, 
that asserts that every method should either be a command that performs an action, or a query 
that returns data to the caller, but not both. This principle helps in making the behavior of software 
more predictable and understandable. Here are some examples to illustrate the application of CQS:
'''

# 1. **Bank Account Management**:
    # Command**: `void deposit(amount)` 
        # - Increases the account balance by the specified amount but returns nothing.
    # Query**: `decimal getBalance()` 
        # - Returns the current account balance without changing the state of the account.

# 2. **Shopping Cart in an E-commerce Application**:
    # Command**: `void addItem(Item item)` 
        # - Adds an item to the shopping cart but does not return any value.
    # Query**: `List<Item> getItems()` 
        # - Returns a list of items in the shopping cart without modifying the cart.

# 3. **User Management System**:
    # Command**: `void changeEmailAddress(UserID userId, Email newEmail)` 
        # - Updates the email address for a user but returns no value.
    # Query**: `Email getEmailAddress(UserID userId)` 
        # - Retrieves the email address for a user without changing any user data.

# 4. **Document Editing Software**:
    # Command**: `void deletePage(int pageNumber)`
        # - Deletes a specific page from a document without returning any information.
    # Query**: `DocumentPage getPage(int pageNumber)`
        # - Retrieves a specific page from the document without altering the document.

# 5. **Online Voting System**:
    # Command**: `void castVote(Voter voter, Candidate candidate)`
        # - Records a vote for a candidate from a voter but does not return any information.
    # Query**: `int getVoteCount(Candidate candidate)`
        # - Returns the total number of votes for a candidate without affecting any votes.

# 6. **Game Score Management**:
    # Command**: `void updateScore(Player player, int points)`
        # - Adds points to a player's score without returning any information.
    # Query**: `int getScore(Player player)`
        # - Retrieves the current score for a player without modifying the score.

# 7. **Inventory System**:
    # Command**: `void restockProduct(Product product, int quantity)`
        # - Increases the stock level for a product but does not return any value.
    # Query**: `int getStockLevel(Product product)`
        # - Returns the current stock level for a product without changing the inventory.

# 8. **Configuration Settings**:
    # Command**: `void setPreference(String key, String value)` 
        # - Changes a configuration setting without returning any value.
    # Query**: `String getPreference(String key)`
        # - Retrieves the value of a configuration setting without altering any settings.

# 9. **Social Media Application**:
    # Command**: `void followUser(User follower, User followee)` 
        # - Makes one user follow another but does not return any value.
    # Query**: `List<User> getFollowers(User user)` 
        # - Retrieves the list of followers for a user without modifying any user relationships.

# 10. **Booking System**:
    # Command**: `void cancelBooking(Booking booking)` 
        # - Cancels a specific booking without returning any information.
    # Query**: `BookingStatus getBookingStatus(Booking booking)` 
        # - Checks the status of a booking without changing the booking's state.

'''
In each of these examples, the separation between commands (actions that modify state) 
and queries (actions that return data) is clear, adhering to the CQS principle. 
This approach simplifies the understanding of how an application changes its state and reduces side effects, 
making the system more robust and predictable.
'''