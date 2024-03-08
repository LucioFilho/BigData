# a function to find the middle node of a linked list
import random
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> ListNode:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

# Example to create a linked list: 1 -> 2 -> 3 -> 4 -> 5
def create_random_list(n, val_range):
    head = ListNode(random.randint(1, val_range))
    current = head
    for _ in range(n - 1):
        current.next = ListNode(random.randint(1, val_range))
        current = current.next
    return head

# Create a linked list with 1000 nodes and values between 1 and 100
head = create_random_list(1000, 100)


# Instantiate the Solution class
solution = Solution()

# Find the middle node
middle = solution.middleNode(head)

# Print the value of the middle node
print(f'Middle: {middle.val}')

