# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


# Create list node util
def createListNode(values: list[int]) -> Optional[ListNode]:
    head = ListNode()
    current = head

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return head.next


def printListNode(listNode: ListNode):
    head = listNode
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        listNodes: list[ListNode] = []

        while curr:
            tempList: list[ListNode] = []
            i = 0

            while i < k and curr:
                tempList.append(curr)
                curr = curr.next
                i += 1

            if i == k:
                tempList.reverse()

            for node in tempList:
                listNodes.append(node)

        listNodes[-1].next = None
        for i in range(len(listNodes) - 1):
            listNodes[i].next = listNodes[i + 1]

        return listNodes[0]


if __name__ == "__main__":
    sol = Solution()
    case1 = sol.reverseKGroup(
        createListNode([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), 4
    )
    if case1:
        printListNode(case1)
