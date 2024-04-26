class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        ans = []
        while i < len(firstList) and j < len(secondList) :
            s1, e1, s2, e2 = *firstList[i], *secondList[j]
            start_overlap = max(s1,s2)
            end_overlap = min(e1,e2)
            if start_overlap <= end_overlap:
                ans.append([start_overlap,end_overlap])
            if e1 < e2:
                i  += 1
            else:
                j +=1
        return ans