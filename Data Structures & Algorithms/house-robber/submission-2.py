class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums)
        p1 = 0 #f(0) = 0
        p2 = 0 #f(1) = 0
        for i in range(len(nums)):
           curr = max(p1 , p2 + nums[i])
           p2 = p1
           p1 = curr
        return p1
           
            