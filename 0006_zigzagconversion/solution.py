def zigzag_convert(s, num_rows):
    if num_rows < 2:
        return s
    
    s_len = len(s)
    zigzag = list(s)
    cycle_len = (num_rows * 2) - 2
    num_cols = (s_len + cycle_len - 1) // cycle_len

    i = 0
    row = 0
    while row < num_rows:
        col = 0
        while col < num_cols:
            j = (col * cycle_len) + row
            if j < s_len:
                zigzag[i] = s[j]
                i += 1

            # Has upward zag
            if row != 0 and row != (num_rows - 1):
                jj = (col * cycle_len) + (cycle_len - row)
                if jj < s_len:
                    zigzag[i] = s[jj]
                    i += 1
            col += 1
        row += 1
    
    return "".join(zigzag)

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        return zigzag_convert(s, numRows)

sol = Solution()
s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# s = "0123456"
numRows = 3
result = sol.convert(s, numRows)
print(result)

