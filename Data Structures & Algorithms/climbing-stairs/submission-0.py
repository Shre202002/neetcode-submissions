class Solution:
    def climbStairs(self, n: int) -> int:
        prev1 = 1 # for n =1
        prev2 = 2 # for n= 
        if n == 1: return 1
        if n == 2 : return 2
        for _ in range(2, n):

            curr = prev1 + prev2
            prev2 = prev1
            prev1= curr
        return prev1
        