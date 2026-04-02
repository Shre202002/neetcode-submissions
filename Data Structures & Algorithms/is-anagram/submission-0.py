class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_s = "".join(sorted(s))
        t_t = "".join(sorted(t))
        if s_s ==  t_t:
            return True
        else:
            return False
        
        