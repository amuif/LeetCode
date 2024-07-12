class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        isEqual = False
        for i in equations:
            if i == 'a==b' or i == 'b==a':
                isEqual = True
            elif i == 'a!=b' or i =='b!=a':
                isEqual = False
        return isEqual
        