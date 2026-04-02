class Solution:
    def isValid(self, s: str) -> bool:
        list =[]
        dict = {
        ']': '[',
        '}': '{',
        ')': '('
        }
        for i in s:
            if i in ['[', '{', '(']:
                list.append(i)
            elif i in [')', ']', '}']:
                if not list:
                    return False
                if list[-1] != dict[i]:
                    return False
                list.pop()

        return not list
             