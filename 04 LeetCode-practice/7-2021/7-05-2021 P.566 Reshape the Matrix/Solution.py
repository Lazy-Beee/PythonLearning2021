"""
Day 9   7/05/2021
Problem: https://leetcode.com/problems/reshape-the-matrix/

In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new
one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the row number and column
number of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same
row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped
matrix; Otherwise, output the original matrix.
 """


class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        a = len(mat)
        b = len(mat[0])
        if r * c != a * b:
            return mat

        content = []
        for row in mat:
            content += row
        print(content)
        re = []
        for i in range(r):
            re.append(content[i*c:i*c+c])
        return re


if __name__ == "__main__":
    test = Solution()
    mat = [[1,2],[3,4]]
    r = 1
    c = 4
    print(test.matrixReshape(mat, r, c))