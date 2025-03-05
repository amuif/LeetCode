class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        burst = -1
        count = 0
        points.sort(key=lambda x:x[1])
        # print(points)
        for i in range(len(points)):
            if points[i][0] > burst:
                burst = points[i][1]
                count+=1

        return count