class Solution:
    def minSwaps(self, s: str) -> int:
        left = 0
        right = len(s) - 1

        step = 0

        leftOpen = 0
        leftClose = 0
        rightOpen = 0
        rightClose = 0

        while left < right:

            if s[left] == "[":
                # Left open bracket
                leftOpen += 1
            else:
                # Left close bracket
                leftClose += 1

            if s[right] == "[":
                # Right open backet
                rightOpen += 1
            else:
                # Left close bracket
                rightClose += 1

            if leftOpen < leftClose and rightOpen > rightClose:
                step += 1
                left += 1
                right -= 1

                leftOpen += 1
                leftClose -= 1

                rightOpen -= 1
                rightClose += 1
            elif leftOpen < leftClose:
                right -= 1
                leftClose -= 1
            elif rightOpen > rightClose:
                left += 1
                rightOpen -= 1
            else:
                left += 1
                right -= 1

        return step


if __name__ == "__main__":
    sol = Solution()
    print(
        sol.minSwaps(
            "]][[]][][[]]]][[][]]][]]][[][][]]]][][[[[]][[[[[[[]]][[[[]][[[]][][][]"
        )
    )
