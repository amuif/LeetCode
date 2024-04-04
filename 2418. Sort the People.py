class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        sort = list(zip(names,heights))
        sortted = sorted(sort, key=lambda x: x[1])[::-1]
        output = []
        for i in sortted:
            output.append(i[0])  
        return output     
        
