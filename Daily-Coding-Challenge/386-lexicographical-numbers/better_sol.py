class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        ans = []

        def dfs(currentValue: int):
            if currentValue > n:
                return

            ans.append(currentValue)
            for i in range(10):
                newValue = currentValue * 10 + i
                if newValue > n:
                    return
                dfs(newValue)

        # Start DFS from each root digit (1-9)
        for i in range(1, 10):
            dfs(i)

        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.lexicalOrder(13))
