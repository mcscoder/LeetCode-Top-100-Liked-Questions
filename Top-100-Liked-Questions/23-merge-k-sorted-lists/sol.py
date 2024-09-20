# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


# Create list node util
def createListNode(
    index: int, values: list[int], listNodes: list[ListNode]
) -> ListNode:
    if index == len(values):
        head = listNodes[0]
        for i in range(len(listNodes) - 1):
            listNodes[i].next = listNodes[i + 1]
        return head

    listNodes.append(ListNode(values[index]))

    return createListNode(index + 1, values, listNodes)


def printListNode(listNode: ListNode):
    head = listNode
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        def createListNode(
            index: int, values: list[int], listNodes: list[ListNode]
        ) -> ListNode:
            if index == len(values):
                head = listNodes[0]
                for i in range(len(listNodes) - 1):
                    listNodes[i].next = listNodes[i + 1]
                return head

            listNodes.append(ListNode(values[index]))

            return createListNode(index + 1, values, listNodes)

        values = []

        for listNode in lists:
            head = listNode
            while head:
                values.append(head.val)
                head = head.next

        if len(values) == 0:
            return None

        values.sort()

        return createListNode(0, values, [])


if __name__ == "__main__":
    sol = Solution()
    data1: list[ListNode | None] = list(
        map(lambda x: createListNode(0, x, []), [[1, 4, 5], [1, 3, 4], [2, 6]])
    )
    case1 = sol.mergeKLists(data1)
    if case1:
        printListNode(case1)

    case2 = sol.mergeKLists([])
    if case2:
        printListNode(case2)

    case3 = sol.mergeKLists([None])
    if case3:
        printListNode(case3)
