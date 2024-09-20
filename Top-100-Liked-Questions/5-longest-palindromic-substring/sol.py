class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestPalindrome = ""

        def expandAroundCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            left += 1
            palindrome = s[left:right]

            return palindrome

        for i in range(len(s)):
            # Odd palindrome length case
            oddPalindrome = expandAroundCenter(i, i)

            # Even palindrome length case
            evenPalindrome = expandAroundCenter(i, i + 1)

            # Update the longest palindrome
            longestPalindrome = max(
                longestPalindrome, oddPalindrome, evenPalindrome, key=len
            )

        return longestPalindrome


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome("bacabab"))
    print(sol.longestPalindrome("babad"))
