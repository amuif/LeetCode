class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        test = [i[0] for i in points]
        
        test.sort(reverse=True)
        
        max_diff = 0
        for i in range(len(test)-1):
            diff = test[i] - test[i+1]
            if diff > max_diff:
                max_diff = diff
        
        return max_diff
