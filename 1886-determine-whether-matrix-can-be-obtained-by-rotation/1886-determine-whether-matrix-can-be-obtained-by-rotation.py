class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(matrix):
            """ Rotates a square matrix 90 degrees clockwise """
            return [list(row) for row in zip(*matrix[::-1])]
        
        for _ in range(4): 
            if mat == target:
                return True
            mat = rotate(mat)

        return False
