# Given an array 'nums' of n integers where n > 1
# Return an array output such that output[i] is equal to the product of all the element of 'nums' except nums[i]

class Solution:
    def productExceptSelf(self, nums):
        s = []
        tem = 1

        for i in range(len(nums)):
            s.append(tem)
            tem *= nums[i]

        tem = 1

        for j in range(len(nums)-1, 0 -1, -1):
            s[j] *= tem
            tem *=  nums[j]

        return s


nums = [1, 2, 3, 4]

output = Solution()

print(output.productExceptSelf(nums))
