class BinarySearch:
    def __init__(self, arr: list[int]) -> None:
        self.arr = arr

    def searchMostLeft(self, target: int) -> int:
        left = 0
        right = len(self.arr) - 1
        isFound = False

        while left <= right:
            mid = (left + right) // 2
            value = self.arr[mid]

            if value < target:
                left = mid + 1
            elif value > target:
                right = mid - 1
            else:
                isFound = True

                # Search most left
                right = mid - 1

        if isFound:
            return left

        return -1

    def searchMostRight(self, target: int) -> int:
        left = 0
        right = len(self.arr) - 1
        isFound = False

        while left <= right:
            mid = (left + right) // 2
            value = self.arr[mid]

            if value < target:
                left = mid + 1
            elif value > target:
                right = mid - 1
            else:
                isFound = True

                # Search most right
                left = mid + 1

        if isFound:
            return right

        return -1


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        bs = BinarySearch(nums)

        return [bs.searchMostLeft(target), bs.searchMostRight(target)]


if __name__ == "__main__":
    sol = Solution()
    print(sol.searchRange([5, 7, 7, 8, 8, 8, 10], 10))
