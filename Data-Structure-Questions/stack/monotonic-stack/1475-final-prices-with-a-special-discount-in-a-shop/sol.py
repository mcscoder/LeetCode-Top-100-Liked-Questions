class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        # contain pairs of (index, value)
        increaseStack: list[tuple[int, int]] = [(0, prices[0])]

        for i in range(1, prices.__len__()):
            while increaseStack.__len__() > 0 and increaseStack[-1][1] >= prices[i]:
                index, value = increaseStack.pop()
                prices[index] = value - prices[i]

            increaseStack.append((i, prices[i]))

        return prices


if __name__ == "__main__":
    sol = Solution()
    print(sol.finalPrices([8, 4, 6, 2, 3]))
    print(sol.finalPrices([1, 2, 3, 4, 5]))
    print(sol.finalPrices([10, 1, 1, 6]))