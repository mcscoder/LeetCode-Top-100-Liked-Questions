class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        skill.sort()

        # Check if length is divisible by 2
        if skill.__len__() % 2 != 0:
            return -1

        equalSkill = skill[0] + skill[-1]

        l = 0
        r = skill.__len__() - 1
        ans = 0

        while l < r:
            if skill[l] + skill[r] != equalSkill:
                return -1

            ans += skill[l] * skill[r]
            l += 1
            r -= 1

        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.dividePlayers([3, 2, 5, 1, 3, 4]))
