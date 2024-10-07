class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []

        def heapPermutation(a: list[int], size: int):

            if size == 1:
                ans.append(list(a))
                return

            for i in range(size):
                heapPermutation(a, size - 1)

                if size % 2:
                    a[0], a[size - 1] = a[size - 1], a[0]
                else:
                    a[i], a[size - 1] = a[size - 1], a[i]

        heapPermutation(nums, len(nums))

        return ans
