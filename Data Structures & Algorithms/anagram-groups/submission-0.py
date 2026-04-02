class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for i in strs:
            freq = [0]*26

            for char in i:
                index = ord(char) - ord('a')
                freq[index] +=1
            key = tuple(freq)
            if key not in dict:
                dict[key] = []
            dict[key].append(i)

        return list(dict.values())