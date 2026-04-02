class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        final_max = 0
        if len(nums) == 1 and nums[0] == 1: return 1
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1] == 1:
                if max:max +=1
                else: max+=2
            if final_max < max:
                final_max = max
            if nums[i] == 0:
                max = 0
        return final_max
        