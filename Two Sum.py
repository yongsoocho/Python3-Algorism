#Given an array of integars 'nums' and an integer 'target'
#return 'indices' of the two numbers such that they add up to target

import collections

class Solution:
    def TwoSum_1(self, nums, target):
        for i, n in enumerate(nums):
            complement = target - n

            if complement in nums[i+1:]:
                return [nums.index(n), nums[i+1:].index(complement) + (i+1)]

    def TwoSum_2(self, nums, target):
        nums_map = {}
        nums_map = collections.defaultdict(int)
        
        for i, num in enumerate(nums):
            nums_map[num] = i

        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [nums.index(num), nums_map[target - num]]

    def TwoSum_3(self, nums, target):
        left, right = 0, len(nums) - 1
        while not left == right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                return [left, right]

input_nums = [2, 7, 11, 15]
input_target = 9

output = Solution()

print(output.TwoSum_1(input_nums, input_target))
print(output.TwoSum_2(input_nums, input_target))
print(output.TwoSum_3(input_nums, input_target))
