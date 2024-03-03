# Don't Repeat Yourself (DRY):
'''
Introduced by Andy Hunt and Dave Thomas in their book "The Pragmatic Programmer", 
the DRY principle states that "Every piece of knowledge must have a single, unambiguous, 
authoritative representation within a system".
'''

'''
The Don't Repeat Yourself (DRY) principle emphasizes minimizing duplication in software development 
to achieve a more maintainable, extensible, and bug-resistant codebase. 
Here are several examples illustrating the application of the DRY principle:
'''

# Consolidating Common Logic:

# Violation: Copy-pasting the same logic in multiple functions or methods.
def calculate_area_of_square(side):
    return side * side  # Repeated logic

def calculate_perimeter_of_square(side):
    return 4 * side  # Repeated logic

# DRY Application: Extract the repeated logic into a reusable function.
def square(side):
    return side * side

def calculate_area_of_square(side):
    return square(side)

def calculate_perimeter_of_square(side):
    return 4 * side

# Using Loops Instead of Repetition:

# Violation: Manually writing out actions for each item.
print(student_grades[0])
print(student_grades[1])
print(student_grades[2])

# DRY Application: Use a loop to iterate over items.
for grade in student_grades:
    print(grade)

# Template Functions for Similar HTML Pages:

# Violation: Copying and pasting similar HTML structures with minor differences.
<!-- Page1.html -->
<div>
    <h1>Title 1</h1>
    <p>Content for page 1...</p>
</div>

<!-- Page2.html -->
<div>
    <h1>Title 2</h1>
    <p>Content for page 2...</p>
</div>

# DRY Application: Use a templating engine to dynamically generate similar pages.
# Using a Python web framework like Flask with Jinja2 templating
@app.route('/page/<int:page_id>')
def show_page(page_id):
    titles = ["Title 1", "Title 2"]
    contents = ["Content for page 1...", "Content for page 2..."]
    return render_template('page_template.html', title=titles[page_id], content=contents[page_id])

<!-- page_template.html -->
<div>
    <h1>{{ title }}</h1>
    <p>{{ content }}</p>
</div>

# Centralizing Configuration Values:

# Violation: Hardcoding configuration values like database connection strings in multiple places.
# In file1.py
db_connection = "server=localhost;user=root;password=123"

# In file2.py
db_connection = "server=localhost;user=root;password=123"

# DRY Application: Define the configuration in one location and import it elsewhere.
# config.py
db_connection = "server=localhost;user=root;password=123"

# file1.py and file2.py
from config import db_connection

# Utilizing CSS Classes for Styling:

# Violation: Repeating style attributes in multiple HTML elements.
<p style="font-size:16px;color:blue;">Paragraph 1</p>
<p style="font-size:16px;color:blue;">Paragraph 2</p>

# DRY Application: Define a CSS class and apply it to all relevant elements.
<style>
.blue-text {
    font-size: 16px;
    color: blue;
}
</style>
<p class="blue-text">Paragraph 1</p>
<p class="blue-text">Paragraph 2</p>

'''
These examples demonstrate how adhering to the DRY principle can simplify and improve 
the maintainability of code by reducing repetition and centralizing shared logic or data.
'''
