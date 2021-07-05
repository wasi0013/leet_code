class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        t = iter(chain(*mat))
        n = len(mat)
        m = len(mat[0])
        new_mat = [[0]*c for i in range(r)]
        # print(new_mat)
        if m*n != r*c:
            return mat
        for i in range(r):
            for j in range(c):
                new_mat[i][j] = next(t)
        return new_mat

