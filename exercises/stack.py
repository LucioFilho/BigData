'''In Python, a stack can be easily implemented using a list. 
A stack is a data structure with two principal operations: 
push (which adds an item to the top of the stack) and pop 
(which removes the item from the top of the stack). 
Stacks follow the Last In, First Out (LIFO) principle.'''

'''This Stack class provides the typical functionality you would expect from a stack:

push: Add an item to the top of the stack.

pop: Remove and return the top item from the stack. 
If the stack is empty, it raises an IndexError.

peek: Return the top item from the stack without removing it. 
If the stack is empty, it raises an IndexError.

is_empty: Check if the stack is empty.

size: Return the number of items in the stack.

This implementation uses Python's built-in list to store stack items, 
taking advantage of the list's efficient append and pop methods that operate 
in constant time.'''

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")

    def size(self):
        return len(self.items)

# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())  # Outputs 3
print(stack.peek())  # Outputs 2
print(stack.size())  # Outputs 2


'''In a stack, both the append (or push) and pop operations occur at the same end, 
conventionally referred to as the "top" of the stack. In Python's list implementation, 
this "top" is represented by the end of the list:

The append method adds an element to the end of the list, which acts as the top of the stack.

The pop method, without an index, removes the element from the end of the list, 
effectively removing it from the top of the stack.
So yes, both the append and pop operations are performed from the same side of 
the list to maintain the LIFO (Last In, First Out) behavior characteristic of a stack. 
Here's how it works:'''

stack_appen = []
stack_appen.append(1)  # Stack is now [1]
stack_appen.append(2)  # Stack is now [1, 2]
stack_appen.append(3)  # Stack is now [1, 2, 3]

# Pop elements from the stack
print(stack_appen.pop())  # Outputs 3, stack is now [1, 2]
print(stack_appen.pop())  # Outputs 2, stack is now [1]
print(stack_appen.pop())  # Outputs 1, stack is now []
