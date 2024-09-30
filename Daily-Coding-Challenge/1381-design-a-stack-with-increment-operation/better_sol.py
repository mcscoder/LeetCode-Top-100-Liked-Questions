# Decrease increment method to O(1)
class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.incrementValues = [0] * maxSize
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) == self.maxSize:
            return

        self.stack.append(x)

    def pop(self) -> int:
        index = len(self.stack) - 1

        if index == -1:
            return -1

        if index > 0:
            self.incrementValues[index - 1] += self.incrementValues[index]

        value = self.stack.pop() + self.incrementValues[index]
        self.incrementValues[index] = 0

        return value

    def increment(self, k: int, val: int) -> None:
        index = min(k, len(self.stack)) - 1
        if index == -1:
            return
        self.incrementValues[index] += val


if __name__ == "__main__":
    stack = CustomStack(3)
    print(stack.push(1), end=" ")
    print(stack.push(2), end=" ")
    print(stack.pop(), end=" ")
    print(stack.push(2), end=" ")
    print(stack.push(3), end=" ")
    print(stack.push(4), end=" ")
    print(stack.increment(5, 100), end=" ")
    print(stack.increment(2, 100), end=" ")
    print(stack.pop(), end=" ")
    print(stack.pop(), end=" ")
    print(stack.pop(), end=" ")
    print(stack.pop(), end=" ")
