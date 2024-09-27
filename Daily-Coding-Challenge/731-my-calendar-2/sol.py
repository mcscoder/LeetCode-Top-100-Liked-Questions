class MyCalendarTwo:

    def __init__(self):
        self.nonOverlap: list[tuple[int, int]] = []
        self.overlap: list[tuple[int, int]] = []

    def book(self, start: int, end: int) -> bool:
        for left, right in self.overlap:
            if left < end and right > start:
                return False

        for left, right in self.nonOverlap:
            if left < end and right > start:
                self.overlap.append((max(start, left), min(end, right)))

        self.nonOverlap.append((start, end))

        return True


if __name__ == "__main__":
    sol = MyCalendarTwo()
    for start, end in [[10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]:
        print(sol.book(start, end), end=" ")
