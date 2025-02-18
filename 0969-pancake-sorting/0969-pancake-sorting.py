class Solution:

    def flipper(self, end):
        left, right = 0, end
        while left < right:
            self.arr[left], self.arr[right] = self.arr[right], self.arr[left]
            left += 1
            right -= 1

    def maxIndexFinder(self, end):
        max_index = 0
        for i in range(end):
            if self.arr[i] > self.arr[max_index]:
                max_index = i
        return max_index

    def pancakeSort(self, arr: List[int]) -> List[int]:
        solution = []
        self.arr = arr
        self.n = len(arr)

        for i in range(self.n - 1):
            max_index = self.maxIndexFinder(self.n - i)

            self.flipper(max_index)
            self.flipper(self.n - i - 1)

            solution.append(max_index+1)
            solution.append(self.n - i)

        return solution
