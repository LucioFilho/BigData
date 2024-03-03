from collections import deque

# Create a deque
dq = deque(['a', 'b', 'c'])

# Append to the right and left
dq.append('d')  # deque(['a', 'b', 'c', 'd'])
dq.appendleft('z')  # deque(['z', 'a', 'b', 'c', 'd'])

# Pop from the right and left
dq.pop()  # 'd', deque(['z', 'a', 'b', 'c'])
dq.popleft()  # 'z', deque(['a', 'b', 'c'])

print(dq)  # deque(['a', 'b', 'c'])
