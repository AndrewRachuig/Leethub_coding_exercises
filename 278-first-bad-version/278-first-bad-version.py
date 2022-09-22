# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        high = n
        low = 0
        while high - low != 1:
            if isBadVersion((high+low)//2) == False:
                low = (high+low)//2
                
            
            elif isBadVersion((high+low)//2) == True:
                high = (high+low)//2
        
        return high