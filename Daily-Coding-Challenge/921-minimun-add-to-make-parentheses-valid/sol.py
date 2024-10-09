class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # diff = open - close
        diff = 0
        ans = 0

        for parenthese in s:
            if parenthese == "(":
                diff += 1
            else:
                diff -= 1

            if diff < 0:
                ans += 1
                diff = 0

        ans += diff

        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.minAddToMakeValid("())"))
