class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        final_max = 0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                max +=1
            if final_max < max:
                final_max = max
            if nums[i] ==0:
                max = 1
        return final_max
        