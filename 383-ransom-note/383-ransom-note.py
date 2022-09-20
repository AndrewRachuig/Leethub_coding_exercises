class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
         
#     This works but timed out, so I wrote a more efficient version below.
#         ransom_dict = {letter: 1 for letter in set(ransomNote)}
#         ransom_dict = {letter: ransomNote.count(letter) for letter in ransomNote}
        
#         magazine_dict = {letter: 1 for letter in set(magazine)}
#         magazine_dict = {letter: magazine.count(letter) for letter in magazine}
        
#         for letter in ransomNote:
#             try:
#                 if ransom_dict[letter] <= magazine_dict[letter]:
#                     pass
#                 else:
#                     return False
#             except:
#                 return False
#         return True
    
#       This is my second solution that works better but is still slow. Better solution below.
#         note_totals = sorted(ransomNote)
#         magazine_totals = sorted(magazine)
        
#         for letter in note_totals:
#             if letter in magazine_totals:
#                 magazine_totals.remove(letter)
#                 pass
#             else:
#                 return False
        
#         return True
    
    # I love how elegant this solutions is below
        for letter in set(ransomNote):
            if magazine.count(letter) < ransomNote.count(letter):
                return False
            
        return True