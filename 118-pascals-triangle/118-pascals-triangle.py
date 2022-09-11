class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1: return [[1]]
        res = [[1], [1,1]]
        if numRows == 2: return res
        for i in range(2, numRows):
            curr_row = []
            for j in range(i+1):
                if j==0 or j==i: 
                    curr_row.append(1)
                else: 
                    curr_row.append(res[i-1][j]+ res[i-1][j-1])
            res.append(curr_row)
        return res