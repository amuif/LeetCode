class Solution:
    def fib(self, n: int) -> int:
        output = 0
        def fibonacci(n: int) -> int:
            
            if n <= 1:
                return n
            else:
                return fibonacci(n-1) + fibonacci(n-2)

        # Test the function
        for i in range(10):
            output =fibonacci(n)
            
        return output
            