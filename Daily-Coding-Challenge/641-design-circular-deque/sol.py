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


class MyCircularDeque:

    def __init__(self, k: int):
        self.head: Optional[DoublyListNode] = None
        self.tail: Optional[DoublyListNode] = None
        self.maxLength = k
        self.length = 0

    def insertFront(self, value: int) -> bool:
        if self.length == self.maxLength:
            return False

        if self.head:
            # Deque is not empty
            self.head.prev = DoublyListNode(value, next=self.head)
            self.head = self.head.prev
        else:
            # Deque is empty
            self.head = DoublyListNode(value)
            self.tail = self.head

        self.length += 1

        return True

    def insertLast(self, value: int) -> bool:
        if self.length == self.maxLength:
            return False

        if self.tail:
            # Deque is not empty
            self.tail.next = DoublyListNode(value, prev=self.tail)
            self.tail = self.tail.next
        else:
            # Deque is empty
            self.tail = DoublyListNode(value)
            self.head = self.tail

        self.length += 1

        return True

    def deleteFront(self) -> bool:
        if self.head:
            self.head = self.head.next

            if self.head:
                self.head.prev = None
            else:
                # Delete the final element in the deque
                self.tail = None
        else:
            return False

        self.length -= 1

        return True

    def deleteLast(self) -> bool:
        if self.tail:
            self.tail = self.tail.prev

            if self.tail:
                self.tail.next = None
            else:
                # Delete the final element in the deque
                self.head = None
        else:
            return False

        self.length -= 1

        return True

    def getFront(self) -> int:
        if self.head:
            return self.head.val
        else:
            return -1

    def getRear(self) -> int:
        if self.tail:
            return self.tail.val
        else:
            return -1

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.maxLength
