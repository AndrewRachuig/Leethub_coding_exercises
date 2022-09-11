class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        singlerow = []
        for i in mat:
            singlerow += i
        if r * c == len(singlerow):
            new_mat = []
            for i in range(r):
                new_mat.append(singlerow[(c*i):(c + (c*i))])
            return new_mat
        else:
            return mat
        
