class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # contain (index, value) pairs
        decreaseStack: list[int] = [nums2[0]]
        hashmapuh: dict[int, int] = {}

        for i in range(1, nums2.__len__()):
            while decreaseStack.__len__() > 0 and decreaseStack[-1] < nums2[i]:
                value = decreaseStack.pop()
                hashmapuh[value] = nums2[i]

            decreaseStack.append(nums2[i])

        ans = []
        for num in nums1:
            if num in hashmapuh:
                ans.append(hashmapuh[num])
            else:
                ans.append(-1)

        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
