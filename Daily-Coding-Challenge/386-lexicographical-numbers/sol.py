class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        ans = [str(i) for i in range(1, n + 1)]
        ans.sort()

        return list(map(int, ans))


if __name__ == "__main__":
    sol = Solution()
    print(sol.lexicalOrder(101))
