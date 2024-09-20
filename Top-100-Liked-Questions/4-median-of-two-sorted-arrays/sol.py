class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        arr = []
        j1 = 0
        j2 = 0
        while j1 < len(nums1) and j2 < len(nums2):
            if nums1[j1] < nums2[j2]:
                arr.append(nums1[j1])
                j1 += 1
            else:
                arr.append(nums2[j2])
                j2 += 1

        if j1 < len(nums1):
            for i in nums1[j1:]:
                arr.append(i)
        else:
            for i in nums2[j2:]:
                arr.append(i)

        length = len(arr)
        res = 0
        if length % 2 == 0:
            res = (arr[length // 2 - 1] + arr[length // 2]) / 2
        else:
            res = float(arr[length // 2])

        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMedianSortedArrays([1, 3], [2]))
    print(sol.findMedianSortedArrays([1, 2], [3, 4]))
