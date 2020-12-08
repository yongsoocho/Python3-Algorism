#Write a function that reverse a string
#The input string is given as an array of charaters char[ ]
#Do not allocate extra space for another array
#You must do this by modifying the input array in-place with O(1) extra memory
#You may assume all the charaters consist of ASCII characters

In_put = ["h", "e", "l", "l", "o"]

class Solution:
    def reverseString(self, s: In_put) -> None:
        left, right = 0, len(s)-1
        while left<right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        return s

Out_put = Solution()

print(Out_put.reverseString(In_put))
