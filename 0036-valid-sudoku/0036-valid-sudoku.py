class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check row wise
        for i in range(9):
            row = board[i]
            does = set()
            for j in row:
                if j != '.':
                    if j in does:
                        return False
                    does.add(j)

        # check col wise
        for i in zip(*board):
            row = i
            does = set()
            for j in row:
                if j != '.':
                    if j in does:
                        return False
                    does.add(j)
                
        # check every 3*3 box
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                does = set()
                for num in box:
                    if num != '.':
                        if num in does:
                            return False
                        does.add(num)
        
        return True