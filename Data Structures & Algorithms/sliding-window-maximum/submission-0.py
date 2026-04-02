class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        ans = []
        for i in nums:
            if len(res) < k:
                res.append(i)
            if len(res) == k:
                ans.append(max(res))
                res.pop(0)
        return ans
        