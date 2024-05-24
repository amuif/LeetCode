class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # Initialize counters for five and ten dollar bills
        five_dollar_count = ten_dollar_count = 0
      
        # Iterate over each bill received
        for bill in bills:
            if bill == 5:
                # If it's a $5 bill, simply increase the count of $5 bills
                five_dollar_count += 1
            elif bill == 10:
                # If it's a $10 bill, give one $5 bill as change
                ten_dollar_count += 1
                five_dollar_count -= 1
            else:
                # If it's a $20 bill, try to give one $10 and one $5 as change if possible
                # Otherwise, give three $5 bills as change
                if ten_dollar_count:
                    ten_dollar_count -= 1
                    five_dollar_count -= 1
                else:
                    five_dollar_count -= 3
          
            # If at any point the count of $5 bills drops below zero, it's impossible to give change
            if five_dollar_count < 0:
                return False
      
        # If we got to the end without running out of $5 bills, we can give change for all transactions
        return True