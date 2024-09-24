class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length < 2:
            return
        r = length - 1

        m = r
        l = r - 1

        while l > 0 and nums[l] >= nums[m]:
            m -= 1
            l -= 1

        while r > l and nums[l] >= nums[r]:
            r -= 1

        if l == r:
            nums.sort()
            print(nums)
            return

        nums[l], nums[r] = nums[r], nums[l]

        i = m

        for _ in range(m, length - 1):
            for i in range(m, length - 1):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]

        print(nums)


if __name__ == "__main__":
    sol = Solution()
    sol.nextPermutation([1, 2, 5, 4, 3])
    sol.nextPermutation([2, 3, 1])
    sol.nextPermutation([1, 1])
    sol.nextPermutation([5, 1, 1])
    sol.nextPermutation([2, 2, 7, 5, 4, 3, 2, 2, 1])
    sol.nextPermutation([3, 2, 1])
