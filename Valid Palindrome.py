#Given a string, determine if it is a palindrome
#Considering only alphanumeric characters and ignoring cases

import re
import collections

in_put = "A man, a plan, a canal: Panama"
in_put_2 = "race a car"

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]','',s)
        b = s[::-1]
        if s == b:
            return True
        else:
            return False

Out_put = Solution()

print(Out_put.isPalindrome(in_put))
print(Out_put.isPalindrome(in_put_2))


class Solution_2:
    def isPalindrome_2(self, s: str) -> bool:
        strs = collections.deque()

        for i in s:
            if i.isalnum():
                strs.append(i.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True #Becareful about indent!

Out_put_2 = Solution_2()

print(Out_put_2.isPalindrome_2(in_put)) 
print(Out_put_2.isPalindrome_2(in_put_2))
      
