class Solution:
    def trap(self, height: list[int]) -> int:
        leftMax = height[0]
        rightMax = height[-1]

        left = 0
        right = height.__len__() - 1
        waterBlocks = 0

        while left < right:
            if leftMax < rightMax:
                minWallHeight = leftMax
                left += 1
                currentWallHeight = height[left]
                leftMax = max(leftMax, currentWallHeight)

            else:
                minWallHeight = rightMax
                right -= 1
                currentWallHeight = height[right]
                rightMax = max(rightMax, currentWallHeight)

            waterBlocks += max(0, minWallHeight - currentWallHeight)

        return waterBlocks


if __name__ == "__main__":
    sol = Solution()
    print(sol.trap([4, 2, 0, 3, 2, 5]))
