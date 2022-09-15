class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target > matrix[-1][-1]:
            return False
        for i in matrix:
            if max(i)< target:
                pass
            else:
                if target in i:
                    return True
                else:
                    return False
                