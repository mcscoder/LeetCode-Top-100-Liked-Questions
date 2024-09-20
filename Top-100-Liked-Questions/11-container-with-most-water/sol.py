class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxArea = 0
        left = 0
        right = len(height) - 1

        while left < right:
            minHeight = min(height[left], height[right])
            width = right - left
            area = minHeight * width
            maxArea = max(maxArea, area)

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return maxArea


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
