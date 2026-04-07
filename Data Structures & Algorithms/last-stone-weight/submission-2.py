from heapq import heappop, heappush, heapify
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapify(stones)

        while len(stones) > 1:
            m1 = -heappop(stones)
            m2 = -heappop(stones)

            if m1 != m2:
                heappush(stones, -(m1 - m2))

        return -stones[0] if stones else 0