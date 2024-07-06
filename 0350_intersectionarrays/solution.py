def intersect(nums1, nums2):
    n1_buf = {}
    n2_buf = {}
    for n in nums1:
        n1_buf[n] = n1_buf.get(n, 0) + 1
    for n in nums2:
        n2_buf[n] = n2_buf.get(n, 0) + 1
    intersecting_nums = set(n1_buf.keys()) & set(n2_buf.keys())
    results = []
    for n in intersecting_nums:
        c = min(n1_buf[n], n2_buf[n])
        for _ in range(c):
            results.append(n)
    return results

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return intersect(nums1, nums2)


sol = Solution()
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
result = sol.intersect(nums1, nums2)
print(result)

