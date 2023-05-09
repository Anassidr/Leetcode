# by usine a queue, we visit the 0 cells, then the 1 cells, 2 cells etc in order
# this way we always get the shorted path from 0


import collections as c
class Solution:
    def updateMatrix(self, matrix):
        q = c.deque()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    q.append((i, j))
                else:
                    matrix[i][j] = -1

        while q:
            x, y = q.popleft()
            for r, c in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                newX, newY = x+r, y+c
                if 0 <= newX < len(matrix) and 0 <= newY < len(matrix[0]) and matrix[newX][newY] == -1:
                    matrix[newX][newY] = matrix[x][y] + 1
                    q.append((newX, newY))
        return matrix