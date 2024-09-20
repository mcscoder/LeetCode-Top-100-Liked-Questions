from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        class CellType:
            EMPTY = 0
            FRESH = 1
            ROTTEN = 2

        rows = len(grid)
        cols = len(grid[0])
        rottenOrangeIndexes: deque[tuple[int, int]] = deque()
        freshOranges = 0

        for rowIndex in range(rows):
            for colIndex in range(cols):
                cell = grid[rowIndex][colIndex]

                if cell == CellType.FRESH:
                    # Count initial fresh oranges
                    freshOranges += 1
                elif cell == CellType.ROTTEN:
                    # Note rotten orange indexes for BFS algorithm
                    rottenOrangeIndexes.append((rowIndex, colIndex))

        if freshOranges == 0:
            # Instantly return if there is no fresh orange
            return 0

        # Top - Bottom - Left - Right
        directions: list[tuple[int, int]] = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        minutesPassed = 0

        # Start BFS
        while rottenOrangeIndexes and freshOranges > 0:
            minutesPassed += 1

            for _ in range(len(rottenOrangeIndexes)):
                rottenOrangeRowIndex, rottenOrangeColIndex = (
                    rottenOrangeIndexes.popleft()
                )

                for directionRowIndex, directionColIndex in directions:
                    nearRowIndex = rottenOrangeRowIndex + directionRowIndex
                    nearColIndex = rottenOrangeColIndex + directionColIndex

                    if not ((0 <= nearRowIndex < rows) and (0 <= nearColIndex < cols)):
                        continue

                    if grid[nearRowIndex][nearColIndex] == CellType.FRESH:
                        grid[nearRowIndex][nearColIndex] = CellType.ROTTEN
                        rottenOrangeIndexes.append((nearRowIndex, nearColIndex))
                        freshOranges -= 1

        if freshOranges > 0:
            return -1

        return minutesPassed


def printGrid(grid: list[list[int]]):
    for row in grid:
        print(row)
    print()


if __name__ == "__main__":
    sol = Solution()
    print(sol.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
    print(sol.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
    print(sol.orangesRotting([[0, 2]]))
