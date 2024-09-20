class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        threeSumSets: list[list[int]] = []
        length = len(nums)

        for left in range(length):
            if left > 0 and nums[left] == nums[left - 1]:
                # Skip duplicates
                continue

            middle = left + 1
            right = length - 1
            while middle < right:
                total = nums[left] + nums[middle] + nums[right]

                if total > 0:
                    right -= 1

                elif total < 0:
                    middle += 1

                else:
                    threeSumSets.append([nums[left], nums[middle], nums[right]])

                    right -= 1
                    while right > middle and nums[right] == nums[right + 1]:
                        right -= 1

                    middle += 1
                    while middle < right and nums[middle] == nums[middle - 1]:
                        middle += 1

        return threeSumSets


if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
    print(sol.threeSum([-2, -2, 4, 4, -2]))
    print(sol.threeSum([0, 1, 1]))
    print(sol.threeSum([0, 0, 0]))
