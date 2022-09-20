class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
#      This works but is unneccessarily long. See better solution below

#         if set(s) != set(t):
#             return False
#         else:
            
#             s_dict = {letter: 1 for letter in s}
#             s_dict = {letter: s.count(letter) for letter in s}
            
#             t_dict = {letter: 1 for letter in t}
#             t_dict = {letter: t.count(letter) for letter in t}
            
#             return s_dict == t_dict

        return sorted(s) == sorted(t)