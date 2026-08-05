from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_counter = Counter(s)
        for index, char in enumerate(s):
            if char_counter[char] == 1:
                return index
        
        return -1
        