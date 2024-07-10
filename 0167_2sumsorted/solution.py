def two_sum(numbers, target):
    left_index = 0
    right_index = len(numbers) - 1
    
    while left_index < right_index:
        value = numbers[left_index] + numbers[right_index]
        if value == target:
            return [left_index + 1, right_index + 1]
        elif value < target:
            left_index += 1
        else:
            right_index -= 1

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        return two_sum(numbers, target)


sol = Solution()
nums = [2, 3, 4]
target = 6
result = sol.twoSum(nums, target)
print(result)
