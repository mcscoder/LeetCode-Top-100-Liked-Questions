class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:

        nums = [i for i in nums if i > 0]

        length = len(nums)
        for n in nums:
            index = abs(n) - 1

            if index < length and nums[index] > 0:
                nums[index] *= -1

        for i in range(length):
            if nums[i] > 0:
                return i + 1

        return length + 1


if __name__ == "__main__":
    sol = Solution()
    print(sol.firstMissingPositive([1, 2, 0]))
    print(sol.firstMissingPositive([3, 4, -1, 1]))
    print(sol.firstMissingPositive([7, 8, 9, 11, 12]))
