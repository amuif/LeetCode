class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans  = []

        # whenever there is 1 the next can be 0 or 1
        #  if it's 0 the next should always be 1

        def backtrack(subs):
            nonlocal ans
            if len(subs) == n:
                ans.append(subs)
                return

            if subs[-1] == '1':
                backtrack(subs+"1")
                backtrack(subs+"0")

            if subs[-1] == '0':
                backtrack(subs+'1')

            return ans
        backtrack("1")
        backtrack("0")
        return ans