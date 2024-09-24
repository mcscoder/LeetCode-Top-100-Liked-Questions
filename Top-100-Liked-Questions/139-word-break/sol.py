class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        length = len(s)
        dp = [False] * (length + 1)
        dp[0] = True

        for i in range(1, length + 1):
            for word in wordDict:
                start = i - len(word)
                if start >= 0 and dp[start] and s[start:i] == word:
                    dp[i] = True

        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
    print(sol.wordBreak("leetcode", ["leet", "code"]))
