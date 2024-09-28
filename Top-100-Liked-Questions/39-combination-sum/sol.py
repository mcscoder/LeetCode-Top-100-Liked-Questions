class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()

        ans = []

        def backtracking(index: int, comb: list[int], total: int):
            if total == target:
                ans.append(comb[:])
                return

            for i in range(index, len(candidates)):
                newTotal = total + candidates[i]

                if newTotal > target:
                    return

                comb.append(candidates[i])
                backtracking(i, comb, newTotal)
                comb.pop()

        backtracking(0, [], 0)
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum([2, 3, 6, 7], 7))
