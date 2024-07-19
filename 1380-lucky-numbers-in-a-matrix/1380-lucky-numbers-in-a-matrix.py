class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        """
        find the biggest number in the column
        store the coordinate of biggest number
        go through the row 
        return that number if it's the smallest else repeat
        """
        row = len(matrix)
        col = len(matrix[0])
        curr_maxi=0
        maxi = []
    
        for c in range(col):
            curr_maxi=0
            for r in range(row):
                curr_maxi = max(curr_maxi,matrix[r][c])
            maxi.append(curr_maxi)
        return [min(maxi)]