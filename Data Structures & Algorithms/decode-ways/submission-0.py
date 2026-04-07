class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] != '0':
            prev1 = 1
            prev2 = 1
        else: return 0
        for i in range(1,len(s)):
            curr = 0
            if s[i] != '0':
                curr += prev1
            if s[i-1] == '1' or (s[i-1] == '2' and s[i] <= '6'):
                curr += prev2
            if curr == 0:
                return 0
            prev2 = prev1
            prev1 = curr
        return prev1

