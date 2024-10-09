class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        hashmapuh: dict[int, int] = {0: 1}
        total = 0
        ans = 0

        for i in nums:
            total += i

            if total not in hashmapuh:
                hashmapuh[total] = 0

            diff = total - k

            if diff in hashmapuh:
                ans += hashmapuh[diff]

            hashmapuh[total] += 1

        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.subarraySum([1, 1, 1], 2))
    print(sol.subarraySum([1, 2, 3], 3))
