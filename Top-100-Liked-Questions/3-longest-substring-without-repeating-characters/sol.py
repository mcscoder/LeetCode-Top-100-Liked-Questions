class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        max_length = 0
        l = 0

        for r in range(len(s)):
            # If character is presenting in map
            if s[r] in map:
                # Update the left index to the last element index
                l = max(l, map[s[r]] + 1)

            # Update latest appeared index of the element
            map[s[r]] = r

            # Update the max substring length
            max_length = max(max_length, r - l + 1)

        return max_length


if __name__ == "__main__":
    sol = Solution()

    print(sol.lengthOfLongestSubstring("abcabcbb"))
    print(sol.lengthOfLongestSubstring("bbbbb"))
    print(sol.lengthOfLongestSubstring("pwwkew"))
