class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict = {}
        c = 0
        for i in numbers:
            c+=1
            if i not in dict:
                dict[i] = c
            if  target - i in dict.keys() and c != dict[target - i]:
                return [dict[target - i],c]