class Solution:
    def reverseKGroup(self, head, k: int):
        """
        Reverse nodes in groups of k in a linked list.

        Args:
            head: The head node of the linked list.
            k: The size of the groups to reverse.

        Returns:
            The head node of the modified linked list.

        Algorithm:
        This method reverses the nodes in groups of k in the linked list.
        It uses a dummy node to simplify the reversal process.
        The linked list is traversed, and when a group of k nodes is found, the `reverse` method is called to reverse the group.
        The `reverse` method reverses the nodes between the `start` and `end` pointers.

        Returns the head of the modified linked list.
        """

        if head is None or k < 2:
            return head

        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        end = head
        count = 0

        while end:
            count += 1
            if count % k == 0:
                start = self.reverse(start, end.next)
                end = start.next
            else:
                end = end.next

        return dummy.next

    def reverse(self, start, end):
        """
        Reverse a group of nodes between the `start` and `end` pointers.

        Args:
            start: The starting node of the group (before reversal).
            end: The node after the group (after reversal).

        Returns:
            The new starting node of the reversed group.

        """

        prev, curr = start, start.next
        first = curr

        while curr != end:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        start.next = prev
        first.next = curr

        return first


class ListNode:
    def __init__(self, val=0, next=None):
        """
        Initialize a ListNode.

        Args:
            val: The value of the node.
            next: The next node in the linked list.
        """

        self.val = val
        self.next = next


# Create a linked list
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)

solution = Solution()

k = 3
result = solution.reverseKGroup(head, k)

while result:
    print(result.val, end=" -> ")
    result = result.next