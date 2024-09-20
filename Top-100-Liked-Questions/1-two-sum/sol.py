from collections import defaultdict as dict


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map = dict(lambda: -1)

        for i in range(len(nums)):
            diff = target - nums[i]
            if map[diff] != -1:
                return [map[diff], i]
            map[nums[i]] = i
        return []


if __name__ == "__main__":
    solution = Solution()

    nums = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum(nums, target)
    print(result)

    nums = [3, 2, 4]
    target = 6
    result = solution.twoSum(nums, target)
    print(result)

    nums = [3, 3]
    target = 6
    result = solution.twoSum(nums, target)
    print(result)
