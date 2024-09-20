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


def printListNode(listNode: ListNode):
    head = listNode
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(-1, head)

        prev = dummyHead
        curr = dummyHead.next

        hahahaha = False
        while curr:
            if hahahaha:
                temp = prev.val
                prev.val = curr.val
                curr.val = temp

            prev = curr
            curr = curr.next
            hahahaha = not hahahaha

        return dummyHead.next


if __name__ == "__main__":
    sol = Solution()
    case1 = sol.swapPairs(createListNode([1, 2, 3, 4]))
    if case1:
        printListNode(case1)

    case2 = sol.swapPairs(None)
    if case2:
        printListNode(case2)

    case3 = sol.swapPairs(createListNode([1]))
    if case3:
        printListNode(case3)
