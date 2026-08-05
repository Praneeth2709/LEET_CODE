class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        length = 0
        for char in s:
            if char in seen:
                length += 2
                seen.remove(char)
            else:
                seen.add(char)
        if seen:
            length += 1
        return length 

        