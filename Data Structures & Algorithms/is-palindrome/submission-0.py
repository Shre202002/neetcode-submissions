class Solution:
    def isPalindrome(self, s: str) -> bool:
        low_str = s.lower().replace(" ","")
        low = "".join(filter(str.isalnum, low_str))
        rev = low[::-1]     
        if low == rev: return True
        else: return False                                                                                                                                                                                                                                                        