class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        maximum = skill[0] + skill[-1]
        sumi = 0
        for i in range(len(skill)):
            if maximum == skill[i] + skill[-1-i]:
                sumi += skill[i] * skill[-i-1]
            else:
                return -1
        
        return int(sumi / 2)


        