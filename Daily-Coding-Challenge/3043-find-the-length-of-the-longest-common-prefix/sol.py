class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        dct: dict[int, bool] = {}

        for num in arr2:
            while num > 0:
                dct[num] = True
                num //= 10

        numMax = 0
        for num in arr1:
            while num > 0:
                if num in dct:
                    numMax = max(num, numMax)
                num //= 10

        if numMax == 0:
            return 0

        return len(str(numMax))
