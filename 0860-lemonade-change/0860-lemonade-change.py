class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_count = 0
        ten_count = 0
        dollars = {5:0 , 10:0 , 20:0}
        for i in bills:
            if i == 5:
                dollars[5] +=1
            elif i == 10:
                dollars[10] +=1
                dollars[5] -=1
            else:
                if dollars[10]:
                    dollars[10] -=1
                    dollars[5] -=1
                else:
                    dollars[5] -=3

            if dollars[5] < 0:
                return False
    
        return True
                
   