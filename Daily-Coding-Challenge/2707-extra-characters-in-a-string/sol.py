# Original solution
# https://leetcode.com/problems/extra-characters-in-a-string/solutions/5822172/efficient-easy-to-understand-beginner-friendly-dp/?envType=daily-question&envId=2024-09-23

# Clearly explanation video
# https://www.youtube.com/watch?v=ONstwO1cD7c


class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        words = set(dictionary)
        length = len(s)
        dp = [0] * (length + 1)

        for r in range(1, length + 1):
            # Assume the current character is unused
            dp[r] = dp[r - 1] + 1

            for l in range(r - 1, -1, -1):
                subStr = s[l:r]
                if subStr in words:
                    dp[r] = min(dp[l], dp[r])

        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    print(
        sol.minExtraChar(
            "kevlplxozaizdhxoimmraiakbak",
            [
                "yv",
                "bmab",
                "hv",
                "bnsll",
                "mra",
                "jjqf",
                "g",
                "aiyzi",
                "ip",
                "pfctr",
                "flr",
                "ybbcl",
                "biu",
                "ke",
                "lpl",
                "iak",
                "pirua",
                "ilhqd",
                "zdhx",
                "fux",
                "xaw",
                "pdfvt",
                "xf",
                "t",
                "wq",
                "r",
                "cgmud",
                "aokas",
                "xv",
                "jf",
                "cyys",
                "wcaz",
                "rvegf",
                "ysg",
                "xo",
                "uwb",
                "lw",
                "okgk",
                "vbmi",
                "v",
                "mvo",
                "fxyx",
                "ad",
                "e",
            ],
        )
    )
