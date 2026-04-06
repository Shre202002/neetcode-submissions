from heapq import heappop, heappush, heapify
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) != 1:
            m1 = -heapq.heappop(stones)
            m2 = -heapq.heappop(stones)
            if m1 != m2: heapq.heappush(stones,m1-m2)
        return stones[0]


