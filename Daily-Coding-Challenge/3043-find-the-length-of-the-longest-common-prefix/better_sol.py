class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        dct = set()

        for i in arr2:
            while i:
                dct.add(i)
                i //= 10

        longest = 0
        for i in arr1:
            while i:
                if i in dct:
                    longest = max(longest, len(str(i)))
                    break
                i //= 10

        return longest


if __name__ == "__main__":
    sol = Solution()
print(sol.longestCommonPrefix([1, 10, 100], [1000]))
