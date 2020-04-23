"""
A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. If such index doesn't exist,
return -1.

You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:

BinaryMatrix.get(row, col) returns the element of the matrix at index (row, col) (0-indexed).
BinaryMatrix.dimensions() returns a list of 2 elements [rows, cols], which means the matrix is rows * cols.
Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent
the judge will result in disqualification.

For custom testing purposes you're given the binary matrix mat as input in the following four examples. 
You will not have access the binary matrix directly.

Input: mat = [[0,0],[1,1]]
Output: 0

Input: mat = [[0,0],[0,1]]
Output: 1

Input: mat = [[0,0],[0,0]]
Output: -1

Input: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
Output: 1

Constraints:

rows == mat.length
cols == mat[i].length
1 <= rows, cols <= 100
mat[i][j] is either 0 or 1.
mat[i] is sorted in a non-decreasing way.
"""

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        
        row, column = map(int, binaryMatrix.dimensions()) 
        column -= 1
        pre_row = 0
        indx = -1
        
        while column >= 0:
            for j in range(pre_row, row):
                while column >= 0 and binaryMatrix.get(j, column) == 1:
                    indx = column
                    column -= 1
                    
            pre_row = j + 1  
            if pre_row == row :
                return indx
            
        if pre_column <= 0:
            return 0
