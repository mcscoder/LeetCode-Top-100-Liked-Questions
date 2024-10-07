class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for i in range(len(s)):
            ch = s[i]

            if len(stack) == 0:
                stack.append(ch)
            elif ch == "B" and stack[-1] == "A":
                stack.pop()
            elif ch == "D" and stack[-1] == "C":
                stack.pop()
            else:
                stack.append(ch)

        return len(stack)


if __name__ == "__main__":
    sol = Solution()
    print(sol.minLength("ABFCACDB"))
    print(sol.minLength("ACBBD"))
    print(sol.minLength("D"))