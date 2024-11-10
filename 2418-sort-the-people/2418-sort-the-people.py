class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        zipped  = list(zip_longest(names,heights))
        zipped.sort(key= lambda X : X[1])
        return [x[0] for x in zipped][::-1]
        
