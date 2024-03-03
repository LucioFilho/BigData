# deque for Efficient Queues and Stacks
'''deque can be used to implement efficient queues and stacks for algorithms that require 
frequent additions and removals from both ends.'''

from collections import deque

# Using deque as a stack
stack = deque()
stack.append('a')  # Push
stack.append('b')  # Push
print(stack.pop())  # Pop -> 'b'

# Using deque as a queue
queue = deque()
queue.appendleft('a')  # Enqueue
queue.appendleft('b')  # Enqueue
print(queue.pop())  # Dequeue -> 'a'
