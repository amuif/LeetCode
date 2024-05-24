class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        if n<=1:
            return n
        points = sorted(points, key=lambda x:x[1])

        fp = points[0][1]
        ret = 0
        for i in range(1, n):
            if fp >= points[i][0]:
                continue
            else:
                fp = points[i][1]
                ret += 1
        return ret + 1
