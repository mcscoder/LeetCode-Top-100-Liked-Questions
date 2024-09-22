from typing import Optional


# Definition for singly-linked list.
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


def printListNode(listNode: Optional[ListNode]):
    head = listNode
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        groupPrev = dummy

        while True:
            kth = groupPrev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            nextGroup = kth.next

            prev = nextGroup
            curr = groupPrev.next

            for _ in range(k):
                temp = curr.next

                curr.next = prev
                prev = curr
                curr = temp

            temp = groupPrev.next
            groupPrev.next = prev
            groupPrev = temp


if __name__ == "__main__":
    sol = Solution()
    printListNode(
        sol.reverseKGroup(
            createListNode([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), 4
        )
    )
