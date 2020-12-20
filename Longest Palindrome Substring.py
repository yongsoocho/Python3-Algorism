#Given a string 's'
#Return the longest palindromic substring s

class Solution:
    def longestPalindrome(self, s):
        result = ''
        
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right - 1]:
                left -= 1
                right += 1

            return s[left + 1:right - 1]

        if len(s) < 2 or s[:]==s[::-1]:
            return s

        for i in range(len(s) - 1):
            result = max(result, expand(i, i+2), expand(i, i+1), key=len)

        return result

input_1 = "babad"
input_2 = "cbbbd"

output_1 = Solution()
output_2 = Solution()

print(output_1.longestPalindrome(input_1))
print(output_2.longestPalindrome(input_2))
