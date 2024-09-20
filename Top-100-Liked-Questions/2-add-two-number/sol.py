from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional["ListNode"], l2: Optional["ListNode"]
    ) -> Optional["ListNode"]:
        head = ListNode(0)
        current = head
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return head.next


def to_list(node: Optional["ListNode"]):
    values = []
    while node:
        values.append(node.val)
        node = node.next
    return values


def create_list(nums: list[int]) -> Optional["ListNode"]:
    dummy_head = ListNode(0)
    current = dummy_head
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy_head.next


if __name__ == "__main__":
    l1 = create_list([2, 4, 3])
    l2 = create_list([5, 6, 4])

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)

    print(to_list(result))
