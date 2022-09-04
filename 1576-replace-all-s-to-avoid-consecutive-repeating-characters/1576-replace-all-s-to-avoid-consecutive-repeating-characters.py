class Solution:
    def modifyString(self, s: str) -> str:
        import random
        letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

        new_s = s.replace('?', random.choice(letters))
        new_s = list(new_s)
        s = list(s)

        for i in range(len(s)-1):
            while s[i] == '?' and (new_s[i] == new_s[i+1] or new_s[i] == new_s[i-1]):
                new_s[i] = random.choice(letters)
        
        
        return ''.join(new_s)
