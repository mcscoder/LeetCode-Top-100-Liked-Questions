class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev = s[::-1]
        length = len(s)

        i = 0
        while i <= length:
            cond = True

            # Online solving
            for j in range(length - i):
                if rev[i + j] != s[j]:
                    cond = False
                    break

            if cond:
                break

            i += 1

        return rev[:i] + s


if __name__ == "__main__":
    sol = Solution()
    print(sol.shortestPalindrome("aacecaaa"))
    print(sol.shortestPalindrome("a"))
