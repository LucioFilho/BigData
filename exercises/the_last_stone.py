'''The problem typically states that we have a list of stones, 
each with a positive integer weight. Each turn, we select the two 
heaviest stones and smash them together. If they are of equal weight, 
both stones are destroyed; if they are not, the stone with the lesser 
weight is destroyed, and the remaining stone loses the weight equal to the 
lighter stone. This process continues until there is zero or one stone left. 
The task is to return the weight of the remaining stone (or 0 if none are left).'''

from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Negate the weights to use Python's min heap as a max heap
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            stone_1 = -heapq.heappop(stones)
            stone_2 = -heapq.heappop(stones)
            
            if stone_1 != stone_2:
                heapq.heappush(stones, -(stone_1 - stone_2))

        return -stones[0] if stones else 0

# Example usage:
solution = Solution()
stones = [2, 66, 44, 1, 8, 1]
remaining_stone_weight = solution.lastStoneWeight(stones)
print(f"The weight of the remaining stone is: {remaining_stone_weight}")


'''In this solution, we use a min heap to simulate a max heap by negating the weights. 
Python's heapq module provides a binary min heap implementation, so we negate the 
weights when we put them into the heap and negate them again when taking them out. 
This allows us to always pop the two heaviest stones. After we calculate the difference 
(if there is any), we push the result back onto the heap as a new stone. This process 
repeats until there is one or no stones left.'''