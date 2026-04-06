class Solution:
    def climbStairs(self, n: int) -> int:
        # def ways(n):
        #     return ways(n-1) + ways(n-2)
         
        if n == 1: return 1
        if n == 2 : return 2
        p1 = 1 #for n = 1
        p2 = 2  # for n = 2
        for _ in range(3,n+1):
            curr = p1 + p2
            p2 = p1
            p1 = curr
        return p1
        