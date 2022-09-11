class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        singlemat = []
        for i in mat:
            singlemat += i
        if r *c == len(singlemat):
            new_mat = []
            for i in range(r):
                new_mat.append(singlemat[(c*i):(c + (c*i))])
            return new_mat
        else:
            return mat
        
