#Reverse a singly linked list

class Solution:
    def reverseList_1(self, head):
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev

    def reverseList_2(self, head):
        def reverse(node, prev):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)

        return reverse(head)

Input : 1->2->3->4->5->NULL
Output : 5->4->3->2->1->NULL
