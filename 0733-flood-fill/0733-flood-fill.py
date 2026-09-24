class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        
        startColor = image[sr][sc]
        if startColor == color:
            return image
        
        ROWS, COLS = len(image), len(image[0])

        def dfs(r, c):
            if r >= ROWS or c >= COLS or min(r,c) < 0 or image[r][c] != startColor:
                return
            
            image[r][c] = color
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image