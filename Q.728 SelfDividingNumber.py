class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        output = []

        for num in range(left, right + 1):
            current_num = num
            is_self_dividing = True

            while current_num > 0:
                digit = current_num % 10
                if digit == 0 or num % digit != 0:
                    is_self_dividing = False
                    break
                current_num //= 10

            if is_self_dividing:
                output.append(num)

        return output
      
