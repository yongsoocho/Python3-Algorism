# Given a singly linked list, determine if it is a palindrome

import collections

class Solution:
    def isPalindrome(self, head):
        
        q = []

        node = head

        while node:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False

        return True

Example : List = 1->2->2->1

output = Solution()

print(output.isPalindrome(Example))
