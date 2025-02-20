class ProductOfNumbers:

    def __init__(self):
        self.arr = []
        self.prefix = []
        self.n = 0
        self.zero = -1

    def add(self, num: int) -> None:
        self.arr.append(num)
        
        if num == 0:
            num = 1
            self.zero = self.n
                    
        self.prefix.append(self.prefix[-1]*num if self.prefix else num)
        self.n += 1

    def getProduct(self, k: int) -> int:
        # print(self.arr)
        if self.zero >= self.n-k:
            return 0 
            
        if self.n == k:
            return self.prefix[-1]
        

        return self.prefix[-1] // self.prefix[-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
