class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        n = 0
        for i in details:
            cutted = i[11:]
            print(cutted)
            if int(cutted[0:2]) > 60:
                count +=1
            
        return  count
        