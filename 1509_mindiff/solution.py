def min_diff_sorted(nums, num_moves):
    if len(nums) <= num_moves + 1:
        return 0
    
    window_size = len(nums) - num_moves
    min_value = nums[-1] - nums[0]
    for i in range(num_moves + 1):
        window_min_value = nums[window_size - 1 + i] - nums[i]
        min_value = min(min_value, window_min_value)
    
    return min_value

def min_diff(nums):
    nums = sorted(nums)
    return min_diff_sorted(nums, 3)

class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return min_diff(nums)

sol = Solution()
nums = [6,6,0,1,1,4,6]
result = sol.minDifference(nums)
print(result)
