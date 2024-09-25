class Solution:
    def sumPrefixScores(self, words: list[str]) -> list[int]:
        dct = {}

        for word in words:
            for i in range(len(word) + 1):
                subStr = word[:i]

                if subStr not in dct:
                    dct[subStr] = 0

                dct[subStr] += 1

        ans = []
        for word in words:
            count = 0
            for i in range(1, len(word) + 1):
                subStr = word[:i]
                count += dct[subStr]

            ans.append(count)

        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.sumPrefixScores(["abc", "ab", "bc", "b"]))
