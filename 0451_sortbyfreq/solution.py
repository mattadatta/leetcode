def frequency_sort(s):
    results = {}
    for c in s:
        val = results.get(c, 0)
        results[c] = val + 1
    return "".join([c * x for c, x in sorted(results.items(), key=lambda item: item[1], reverse=True)])

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        return frequency_sort(s)


sol = Solution()
s = "a coolrisetovotesir to you too"
result = sol.frequencySort(s)
print(result)
