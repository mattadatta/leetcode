def n_sum(arr, target, n, offset):
    if not arr:
        return []
    if n <= 1:
        try:
            return [offset + arr.index(target)]
        except ValueError:
            return []
    
    for i, value in enumerate(arr):
        start = i + 1
        result = n_sum(arr[start:], target - value, n - 1, offset + start)
        if len(result) == n - 1:
            return [offset + i] + result
    
    return []

def two_sum(arr, target):
    return n_sum(arr, target, 2, 0)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return two_sum(nums, target)

sol = Solution()
nums = [3, 2, 4]
target = 6
result = sol.twoSum(nums, target)
print(result)
