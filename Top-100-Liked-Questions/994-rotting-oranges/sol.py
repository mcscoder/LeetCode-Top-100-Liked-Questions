from copy import deepcopy


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        done = False
        minute = 0

        isFreshOrangePresenting = False
        height = len(grid)
        width = len(grid[0])

        while not done:
            done = True
            isFreshOrangePresenting = False

            newGrid = deepcopy(grid)

            for i in range(height):
                for j in range(width):
                    if grid[i][j] == 1:
                        isFreshOrangePresenting = True

                        # Top - Bottom - Left - Right
                        if 2 in [
                            grid[max(i - 1, 0)][j],
                            grid[min(i + 1, height - 1)][j],
                            grid[i][max(j - 1, 0)],
                            grid[i][min(j + 1, width - 1)],
                        ]:
                            newGrid[i][j] = 2
                            done = False

            grid = newGrid

            if not done:
                minute += 1

        if isFreshOrangePresenting:
            return -1

        return minute


def printGrid(grid: list[list[int]]):
    for row in grid:
        print(row)
    print()


if __name__ == "__main__":
    sol = Solution()
    print(sol.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
    print(sol.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
    print(sol.orangesRotting([[0, 2]]))
