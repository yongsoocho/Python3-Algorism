#Given an array 'nums' of 'n' integers, are there element a, b, c in 'nums' such that a + b + c = 0
#Find all unique triplets in the array which gives the sum of zero

nums = [-1, 0, 1, 2, -1, -4]

class Solution:
    def ThreeSum(self, nums):
        results = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            
            left, right = i + 1, len(nums) - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                
                if sum < 0:
                    left += 1
                    
                elif sum > 0:
                    right -= 1
                    
                else:
                    results.append((nums[i], nums[left], nums[right]))

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                        
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return results

output_3sum = Solution()

print(output_3sum.ThreeSum(nums))
