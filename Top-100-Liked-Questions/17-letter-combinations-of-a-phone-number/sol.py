class Solution:

    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        dct = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ans = []
        length = len(digits)
        dct1 = []

        for digit in digits:
            dct1.append(dct[int(digit)])

        def solve(index: int, s: str):
            if index == length:
                ans.append(s)
                return

            for ch in dct1[index]:
                solve(index + 1, s + ch)

        solve(0, "")

        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.letterCombinations("234"))
    print(sol.letterCombinations(""))
    print(sol.letterCombinations("2"))
