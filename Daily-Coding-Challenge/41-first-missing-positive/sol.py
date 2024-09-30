class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        dic: dict[int, bool] = {}

        smallest = 1

        for i in nums:
            if i < 1:
                continue

            dic[i] = True
            while smallest in dic:
                smallest += 1

        return smallest


if __name__ == "__main__":
    sol = Solution()
    print(sol.firstMissingPositive([1, 2, 0]))
    print(sol.firstMissingPositive([3, 4, -1, 1]))
    print(sol.firstMissingPositive([7, 8, 9, 11, 12]))
