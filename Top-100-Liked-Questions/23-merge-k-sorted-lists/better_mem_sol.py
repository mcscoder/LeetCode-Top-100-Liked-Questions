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

        def mergeSortedList(l1: Optional[ListNode], l2: Optional[ListNode]):
            if not (l1):
                return

            previous = l1
            current = l1.next

            while current and l2:
                if current.val < l2.val:
                    # L2 is greater than current
                    # Just move to the next greater current and previous number
                    # Then it will be compare later
                    previous = current
                    current = current.next
                else:
                    # print(current.val, l2.val)
                    # Save the next value of the L2
                    l2Next = l2.next

                    # L2 is smaller than current
                    # Add it next to the previous and before the current
                    previous.next = l2
                    l2.next = current

                    # Move to the next value of L2
                    l2 = l2Next

                    # Update previous
                    previous = previous.next

            if l2:
                previous.next = l2

        ans = ListNode(0)

        for i in range(len(lists)):
            mergeSortedList(ans, lists[i])

        return ans.next


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
