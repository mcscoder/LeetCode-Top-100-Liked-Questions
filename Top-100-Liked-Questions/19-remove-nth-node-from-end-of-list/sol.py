from typing import Optional


class ListNode:
    def __init__(self, val=0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = n
        ansListNode = ListNode(0, head)
        curr = ansListNode
        prevDeleteNode = curr

        while curr:
            if count < 0 and prevDeleteNode:
                prevDeleteNode = prevDeleteNode.next

            count -= 1
            curr = curr.next

        if prevDeleteNode:
            deleteNode = prevDeleteNode.next
            if deleteNode:
                prevDeleteNode.next = deleteNode.next
            else:
                return None

        return ansListNode.next


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
        print(head.val)
        head = head.next


if __name__ == "__main__":
    sol = Solution()
    case1 = sol.removeNthFromEnd(createListNode(0, [1], []), 1)
    print(case1)
    if case1:
        printListNode(case1)
