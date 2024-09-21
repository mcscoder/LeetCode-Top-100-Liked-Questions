class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev = s[::-1]
        expanded = s + "#" + rev
        length = len(expanded)
        lps = [0] * length
        j = 0

        # Using KMP algorithm
        for i in range(1, length):
            while j > 0 and expanded[j] != expanded[i]:
                j = lps[j - 1]

            if expanded[j] == expanded[i]:
                j += 1
                lps[i] = j

        return rev[: len(s) - j] + s


if __name__ == "__main__":
    sol = Solution()
    print(sol.shortestPalindrome("aacecaaa"))
    print(sol.shortestPalindrome("ecbceaa"))
    print(sol.shortestPalindrome("a"))
