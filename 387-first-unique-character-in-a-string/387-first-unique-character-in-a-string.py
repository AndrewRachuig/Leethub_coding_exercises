class Solution:
    def firstUniqChar(self, s: str) -> int:
        for letter in s:
            if s.count(letter) == 1:
                return s.index(letter)
        return -1