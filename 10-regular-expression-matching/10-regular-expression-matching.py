class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        import re
        p = '^'+p+'$'
        return type(re.search(p, s)) != type(None)
