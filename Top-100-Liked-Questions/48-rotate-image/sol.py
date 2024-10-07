# sudo apt install python3-tabulate
# Beauty grid print
from tabulate import tabulate


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        for level in range(n // 2 + n % 2):
            minIndex = level
            maxIndex = n - 1 - level

            temp = matrix[minIndex][:-1:]

            for i in range(minIndex, maxIndex):

                # 1. Rotate top row to right column
                tempValue = matrix[i][maxIndex]
                matrix[i][maxIndex] = temp[i]
                temp[i] = tempValue

                # 2. Rotate right column to bottom row
                tempValue = matrix[maxIndex][n - 1 - i]
                matrix[maxIndex][n - 1 - i] = temp[i]
                temp[i] = tempValue

                # 3. Rotate bottom row to left column
                tempValue = matrix[n - 1 - i][minIndex]
                matrix[n - 1 - i][minIndex] = temp[i]
                temp[i] = tempValue

                # 4. Rotate left column to top row
                matrix[minIndex][i] = temp[i]


if __name__ == "__main__":
    sol = Solution()
    # matrix = [
    #     [1, 2, 3, 4, 5, 6],
    #     [7, 8, 9, 10, 11, 12],
    #     [13, 14, 15, 16, 17, 18],
    #     [19, 20, 21, 22, 23, 24],
    #     [25, 26, 27, 28, 29, 30],
    #     [31, 32, 33, 34, 35, 36],
    # ]
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    sol.rotate(matrix)
    print(tabulate(matrix))
