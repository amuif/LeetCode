class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mono = []
        output = [0] * (len(temperatures))

        for i in range(len(temperatures)):

            while mono and temperatures[i] > temperatures[mono[-1]]:
                index = mono.pop()
                output[index] = i - index
                
            mono.append(i)

        return output
