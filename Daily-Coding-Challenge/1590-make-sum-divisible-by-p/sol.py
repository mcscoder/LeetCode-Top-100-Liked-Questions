# Ms Whiteboard available
class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        total_sum = sum(nums)
        target = total_sum % p

        if target == 0:
            return 0

        # Dictionary to store the latest index where prefix sum % p == key
        prefix_mod_map = {0: -1}
        prefix_sum = 0
        min_length = len(nums)

        for i, num in enumerate(nums):
            # Update prefix sum
            prefix_sum += num
            # Get current prefix sum modulo p
            curr_mod = prefix_sum % p

            # Find the value we need to remove to make the remaining sum divisible by p
            needed_mod = (prefix_sum - target + p) % p

            if needed_mod in prefix_mod_map:
                # Update the minimum length of subarray to remove
                min_length = min(min_length, i - prefix_mod_map[needed_mod])

            # Store the current index for this mod value
            prefix_mod_map[curr_mod] = i

        return min_length if min_length != len(nums) else -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.minSubarray([3, 1, 4, 2], 6))
