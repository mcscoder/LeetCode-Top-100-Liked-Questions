class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        arrSet = sorted(set(arr))
        rank = {}

        for i in range(len(arrSet)):
            rank[arrSet[i]] = i + 1

        return [rank[i] for i in arr]


if __name__ == "__main__":
    sol = Solution()
    print(sol.arrayRankTransform([40, 10, 20, 30]))
    print(sol.arrayRankTransform([100, 100, 100]))
    print(sol.arrayRankTransform([37, 12, 28, 9, 100, 56, 80, 5, 12]))
