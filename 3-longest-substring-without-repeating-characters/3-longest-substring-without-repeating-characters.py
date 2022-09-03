class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        longest = 0

        if len(s) == 0:
            return 0

        for i in range(len(s)):
            temp_set = set()
            while i < len(s):
                if s[i] not in temp_set:
                    temp_set.add(s[i])
                    i+=1
                else:
                    if len(temp_set) > longest:
                        longest = len(temp_set)
                        break
                    else:
                        break
            if len(temp_set) > longest:
                longest = len(temp_set)
        return longest