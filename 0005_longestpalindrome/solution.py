def longest_palindrome(s):
    s_len = len(s)
    max_len = 0
    max_substr = ""
    for i in range(s_len):
        l = i
        r = i
        while l >= 0 and r < s_len:
            if s[l] != s[r]:
                break
            l -= 1
            r += 1

        l += 1
        r -= 1
        p_len = (r - l) + 1
        if p_len > max_len:
            max_len = p_len
            max_substr = s[l:r+1]

        l = i
        r = i + 1
        while l >= 0 and r < s_len:
            if s[l] != s[r]:
                break
            l -= 1
            r += 1

        l += 1
        r -= 1
        p_len = (r - l) + 1
        if p_len > max_len:
            max_len = p_len
            max_substr = s[l:r+1]
    
    return max_substr

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        return longest_palindrome(s)


sol = Solution()
s = "hello"
result = sol.longestPalindrome(s)
print(result)
