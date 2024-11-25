class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort()
        output = [points[0]]
        return points[:k]
        # for i in points:
        #     if 