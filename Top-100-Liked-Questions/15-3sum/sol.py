class Solution:
    # x + y + z = 0
    # x + y = 0 - z
    # left: x + y
    # right: 0 - z
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        length = len(nums)

        ans: set[tuple] = set()
        dct: dict[int, dict[int, bool]] = {}

        for i in range(length):
            x = nums[i]
            right = 0 - x

            if right not in dct:
                dct[right] = {}

            dct[right][i] = True

        if 0 in dct and len(dct[0]) >= 3:
            ans.add((0, 0, 0))

        for i in range(length - 1):
            x = nums[i]
            for j in range(i + 1, length):
                y = nums[j]
                left = x + y

                if not (left in dct):
                    continue

                if i in dct[left] or j in dct[left]:
                    continue

                temp = [x, y, -left]
                temp.sort()

                ans.add(tuple(temp))

        return list(map(list, ans))


if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
    print(sol.threeSum([-2, -2, 4, 4, -2]))
    print(sol.threeSum([0, 1, 1]))
    print(sol.threeSum([0, 0, 0]))
