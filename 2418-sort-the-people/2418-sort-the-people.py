class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        zipped = lambda names, heights: [
            name
            for name, height in sorted(
                zip(names, heights), key=lambda x: x[1], reverse=True
            )
        ]

      
        sorted_names = zipped(names, heights)

        return sorted_names
