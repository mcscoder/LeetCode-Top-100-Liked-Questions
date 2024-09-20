class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []

        def backtracking(open: int, close: int, parenthesis: str):
            # print(parenthesis, open, close)
            # input()

            if close == n:
                ans.append(parenthesis)
                return

            if open < n:
                backtracking(open + 1, close, parenthesis + "(")

            if close < open:
                backtracking(open, close + 1, parenthesis + ")")

        backtracking(0, 0, "")

        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.generateParenthesis(3))
    print(sol.generateParenthesis(1))