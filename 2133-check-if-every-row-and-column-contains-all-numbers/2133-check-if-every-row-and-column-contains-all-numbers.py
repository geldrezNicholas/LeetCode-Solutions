class Solution:
    def checkValid(self, matrix: list[list[int]]) -> bool:

        n = len(matrix)
        expected = set(range(1,n+1))

        for row in matrix:
            if set(row) != expected:
                return False
            
        for col in range(n):
            column = []
            for row in range(n):
                column.append(matrix[row][col])
            print(column)
            if set(column) != expected:
                return False

        return True
