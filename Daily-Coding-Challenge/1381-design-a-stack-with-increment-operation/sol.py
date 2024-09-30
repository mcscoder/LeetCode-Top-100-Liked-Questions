from typing import Optional


class DoublyListNode:
    def __init__(
        self,
        val: int,
        prev: Optional["DoublyListNode"] = None,
        next: Optional["DoublyListNode"] = None,
    ) -> None:
        self.val = val
        self.prev = prev
        self.next = next


class CustomStack:

    def __init__(self, maxSize: int):
        self.head: Optional[DoublyListNode] = None
        self.tail: Optional[DoublyListNode] = None
        self.maxLength = maxSize
        self.length = 0

    def push(self, x: int) -> None:
        if self.length == self.maxLength:
            return

        if self.head:
            self.head.prev = DoublyListNode(x, next=self.head)
            self.head = self.head.prev
        else:
            self.head = DoublyListNode(x)
            self.tail = self.head

        self.length += 1

    def pop(self) -> int:
        if not self.head:
            return -1

        val = self.head.val

        self.head = self.head.next

        if self.head:
            self.head.prev = None

        self.length -= 1

        return val

    def increment(self, k: int, val: int) -> None:
        currentNode = self.tail
        for _ in range(min(self.length, k)):
            currentNode.val += val
            currentNode = currentNode.prev


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
