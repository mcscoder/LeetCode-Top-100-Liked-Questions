from typing import Optional

class TreeNode:
    def __init__(
        self,
        start: int,
        end: int,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.start = start
        self.end = end
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = TreeNode(-1, -1)

    def insertEvent(self, start: int, end: int):
        currNode = self.root

        while currNode:
            if start >= currNode.end:
                # Current interval <= start <= end
                # No overlap, go to the right subtree
                if currNode.right:
                    currNode = currNode.right
                else:
                    currNode.right = TreeNode(start, end)
                    return True
            elif end <= currNode.start:
                # start <= end <= current interval
                # No overlap, go to the left subtree
                if currNode.left:
                    currNode = currNode.left
                else:
                    currNode.left = TreeNode(start, end)
                    return True
            else:
                # Overlap detected
                return False

        return False


class MyCalendar:

    def __init__(self) -> None:
        self.bst = BinarySearchTree()

    def book(self, start: int, end: int) -> bool:
        return self.bst.insertEvent(start, end)


if __name__ == "__main__":
    sol = MyCalendar()
    for start, end in [[10, 20], [15, 25], [20, 30]]:
        print(sol.book(start, end))
