class Solution:
    def fib(self, n: int) -> int:
        output = 0

        def fibonacci(n: int) -> int:

            if n <= 1:
                return n
            else:
                return fibonacci(n - 1) + fibonacci(n - 2)

        for i in range(n):
            output = fibonacci(n)

        return output
