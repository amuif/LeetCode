class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_count = 0
        ten_count = 0

        for i in bills:
            if i == 5:
                five_count +=1

            elif i == 10:
                ten_count +=1
                five_count -=1

            else:
                if ten_count:
                    ten_count -=1
                    five_count -=1
                    
                else:
                    five_count -=3

            if five_count < 0:
                return False
    
        return True
                
   