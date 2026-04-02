class Solution:
    def maxArea(self, heights: List[int]) -> int:
        cap = 0
        for i in range(len(heights)-1):
            for j in range(i+1,len(heights)):
                if cap < (j-i) * min(heights[i] , heights[j]):
                    cap = (j-i) * min(heights[i] , heights[j])
        return cap