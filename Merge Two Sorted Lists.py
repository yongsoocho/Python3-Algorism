# Merge two sorted linked lists and return it as a new sorted list
# The new list should be made by splicing together the nodes of the first two lists

class Solution:
    def mergeTwoLists(self, l1, l2):
        if (not n1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1

        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)

        return l1

Input: l1 = [1, 2, 4], l2 = [1, 3, 4]

Output: [1, 1, 2, 3, 4, 4]
