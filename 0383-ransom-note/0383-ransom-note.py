from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        t = Counter(magazine)
        for char in ransomNote:
            if t[char] > 0:
                t[char] -= 1
            else:
                return False
        return True

        