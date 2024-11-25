class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda x: x[0]**2 + x[1]**2)
        output = [points[0]]
        return points[:k]
        # for i in points:
        #     if 