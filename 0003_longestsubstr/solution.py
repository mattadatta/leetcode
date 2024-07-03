def longest_substr_len(s):
    current_start_index = 0
    longest_len = 0
    seen = set()

    i = 0
    for c in s:
        if c in seen:
            seen.clear()
            longest_len = max(longest_len, i - current_start_index)
            current_start_index += (s[current_start_index:].index(c) + 1)
            seen.update(s[current_start_index:i])
        
        seen.add(c)
        i += 1

    longest_len = max(longest_len, i - current_start_index)
    
    return longest_len

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        return longest_substr_len(s)


sol = Solution()
s = "bbbbb"
result = sol.lengthOfLongestSubstring(s)
print(result)
