def find_median(nums1, nums2):
    nums1_len = len(nums1)
    nums2_len = len(nums2)
    new_len = nums1_len + nums2_len
    
    is_even = ((new_len % 2) == 0)
    left_target_index = int((new_len - 1) / 2)
    right_target_index = left_target_index + 1 if is_even else left_target_index

    left_val = 0
    right_val = 0
    w1 = 0
    w2 = 0
    while w1 < nums1_len or w2 < nums2_len:
        index = w1 + w2
        if w2 == nums2_len or (w1 < nums1_len and nums1[w1] <= nums2[w2]):
            if index == left_target_index:
                left_val = nums1[w1]
            if index == right_target_index:
                right_val = nums1[w1]
                break
            w1 += 1
        else:
            if index == left_target_index:
                left_val = nums2[w2]
            if index == right_target_index:
                right_val = nums2[w2]
                break
            w2 += 1
    
    return (left_val + right_val) / 2.0

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        return find_median(nums1, nums2)


sol = Solution()
nums1 = [1, 2]
nums2 = [3, 4]
result = sol.findMedianSortedArrays(nums1, nums2)
print(result)
