# Principle of Least Surprise (or Astonishment):
'''
The principle that a component of a system should behave in a way that users expect it to behave, 
meaning that the outcome of an operation should be obvious and predictable and align with 
the expectations of those who use it.
'''

''' The Principle of Least Surprise (or Astonishment) suggests that software should behave in such a way that 
users are not surprised by its actions; the outcomes should be obvious and expected. 
This principle can apply to user interface design, API design, and generally any part of a system that 
interacts with users or other systems. Here are a few examples where violating this principle can lead to 
confusion or errors:
'''

# 1. **Inconsistent Naming Conventions**:
'''
If a class has methods like `delete_user` and `removeAccount`, 
the inconsistency in naming (`delete` vs `remove` and `user` vs `Account`) 
can surprise developers who expect consistent naming conventions.
'''

# 2. **Non-Standard Return Values**:
'''
A method named `get_user_by_id` that returns `None` or `False` instead of raising an exception 
when a user isn't found could be surprising. Most would expect an exception for such a lookup failure.
'''

# 3. **Unexpected Side Effects**:
'''
A function that performs an action beyond what its name suggests, 
like `calculate_total` that not only calculates but also updates the database, 
could lead to astonishment because the side effect is not communicated by the function name.
'''

# 4. **UI Elements Acting Differently**:
'''
In a UI, if a button labeled "Download" leads to another form instead of starting a download, 
it would violate the principle as the user expects an immediate download to start.
'''

# 5. **APIs That Don't Follow Conventions**:
'''
An API endpoint that uses HTTP GET to create resources instead of the standard POST or PUT 
would be surprising to developers, as it goes against the widely accepted RESTful practices.
'''

# 6. **Language Constructs Behaving Unusually**:
'''
A programming language where the `+` operator concatenates strings in some contexts 
and adds numbers in others without clear rules can be surprising.
'''

# 7. **Configuration Ignoring Changes**:
'''
A software application that requires a restart to apply configuration changes but doesn't prompt the user 
for a restart, leading them to believe changes should take effect immediately.
'''

# 8. **Command-Line Tools With Non-Standard Flags**:
'''
Most command-line tools use `-h` or `--help` to display help information. 
A tool that uses `-h` to mean "hide" would be counterintuitive and potentially frustrating.
'''

# 9. **Software Updates Changing User Preferences**:
'''
When a software update changes user preferences or defaults without clear communication, 
users can be surprised and may think there is a bug or their settings are lost.
'''

# 10. **Unexpected Focus Behavior in Forms**:
'''
A web form that moves focus to a field automatically in a non-intuitive way, 
such as skipping fields or jumping to the bottom of the page, can disorient and frustrate users.
'''
# 11. **Changing Standard Shortcuts**:
'''
If a new version of a text editor changes the shortcut for "save" from `Ctrl+S` to `Ctrl+P`, 
it would surprise and confuse users accustomed to the standard shortcut.
'''

'''
The key to adhering to the Principle of Least Surprise is to follow established conventions and patterns 
and to ensure that any component of the system acts in a way that is predictable and consistent 
with the user's expectations.
'''
