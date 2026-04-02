class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        for i in range(1, len(height)-1):
            left_max = max(height[0:i])
            right_max = max(height[i:len(height)])
            diff = min(left_max, right_max) - height[i] 
            water += diff if diff > 0 else 0
        return water