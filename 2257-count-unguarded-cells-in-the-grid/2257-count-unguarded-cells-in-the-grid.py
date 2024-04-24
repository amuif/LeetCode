class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        matrix = []
        for i in range(m):
            matrix += [[0 for i in range(n)]]

        out = 0
        # put the walls in the grid
        for x,y in walls:
            matrix[x][y] = "W"
        
        for y, x in guards:
            matrix[y][x] = "G"
        
        for y, x in guards:
            # go to up 
            for i in range(y - 1, -1, -1):
                if matrix[i][x] == 'W':
                    break
                if matrix[i][x] == 'G':
                    break
                if matrix[i][x] == 0:
                    matrix[i][x] = 'M'
                    out += 1

            # go to the left
            # add 1 to y
            for i in range(x + 1, n):
                if matrix[y][i] == 'W':
                    break
                if matrix[y][i] == 'G':
                    break
                if matrix[y][i] == 0:
                    matrix[y][i] = 'M'
                    out += 1

            # go to the right
            # subtract 1 from the y
            for i in range(x - 1, -1, -1):
                if matrix[y][i] == 'W':
                    break
                if matrix[y][i] == 'G':
                    break
                if matrix[y][i] == 0:
                    matrix[y][i] = 'M'
                    out += 1
        
            # go down
            for i in range(y + 1, m):
                if matrix[i][x] == 'W':
                    break
                if matrix[i][x] == 'G':
                    break
                if matrix[i][x] == 0:
                    matrix[i][x] = 'M'
                    out += 1
        # out = 0
        # for i in range(n):
        #     for j in range(m):
        #         if matrix[j][i] == 0:
        #             out += 1
        # return out
        return n*m - out - len(walls) - len(guards)