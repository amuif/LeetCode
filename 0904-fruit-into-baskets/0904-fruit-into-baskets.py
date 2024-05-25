class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_count = 0
        basket = {}
        start = 0

        for end in range(len(fruits)):
            basket[fruits[end]] = end

            # If there are more than 2 types of fruit in the basket,
            # remove the fruit that appeared first and update the start index
            if len(basket) > 2:
                min_index = min(basket.values())
                del basket[fruits[min_index]]
                start = min_index + 1

            # Update the maximum count if the current window is larger
            max_count = max(max_count, end - start + 1)

        return max_count