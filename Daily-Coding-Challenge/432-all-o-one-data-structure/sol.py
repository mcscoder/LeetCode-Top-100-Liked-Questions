class AllOne:

    def __init__(self):
        # Store key - rank
        self.dct: dict[str, int] = {}

        # Store key - count value
        self.values: list[list] = []

    def inc(self, key: str) -> None:
        if key not in self.dct:
            self.dct[key] = len(self.values)
            self.values.append([key, 0])

        self.values[self.dct[key]][1] += 1

        # Check if current is greater than left node
        while (
            self.dct[key] > 0
            and self.values[self.dct[key]][1] > self.values[self.dct[key] - 1][1]
        ):
            # Get left node key
            leftNodeKey = self.values[self.dct[key] - 1][0]

            # Swap two node
            self.values[self.dct[key]], self.values[self.dct[key] - 1] = (
                self.values[self.dct[key] - 1],
                self.values[self.dct[key]],
            )

            # Re-order rank index
            self.dct[leftNodeKey] += 1
            self.dct[key] -= 1

    def dec(self, key: str) -> None:
        self.values[self.dct[key]][1] -= 1
        n = len(self.values)

        # Check if current is smaller than right node
        while (
            self.dct[key] < n - 1
            and self.values[self.dct[key]][1] < self.values[self.dct[key] + 1][1]
        ):
            # Get right node key
            rightNodeKey = self.values[self.dct[key] + 1][0]

            # Swap two node
            self.values[self.dct[key]], self.values[self.dct[key] + 1] = (
                self.values[self.dct[key] + 1],
                self.values[self.dct[key]],
            )

            # Re-order rank index
            self.dct[rightNodeKey] -= 1
            self.dct[key] += 1

        # Remove out of values storage if count is zero
        if self.values[self.dct[key]][1] == 0:
            self.values.pop()
            self.dct.pop(key)

    def getMaxKey(self) -> str:
        if len(self.values) == 0:
            return ""

        return self.values[0][0]

    def getMinKey(self) -> str:
        if len(self.values) == 0:
            return ""

        return self.values[-1][0]


if __name__ == "__main__":
    sol = AllOne()
    sol.inc("abc")
    print(sol.values)
    sol.inc("abc")
    print(sol.values)
    sol.inc("xyz")
    print(sol.values)
    sol.inc("xyz")
    print(sol.values)
    print(sol.dct)
    sol.inc("xyz")
    print(sol.values)
    print(sol.dct)
