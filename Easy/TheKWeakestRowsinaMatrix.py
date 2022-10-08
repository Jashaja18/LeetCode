class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        for i in range(len(mat)):  # for i in range of the length of mat
            for j in range(len(mat)):
                if mat[i][j] == 0:  # if mat at i and j is 0
                    mat[i] = mat[i][:j]  # mat at i is mat at i from 0 to j
                    break  # break
                elif j == len(mat) - 1:  # if j is equal to the length of mat - 1
                    mat[i] = mat[i][:j + 1]  # mat at i is mat at i from 0 to j + 1
        return [i[0] for i in sorted(enumerate(mat), key=lambda x: len(x[1]))][:k]
