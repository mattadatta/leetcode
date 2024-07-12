close_to_open = {
    ")": "(",
    "}": "{",
    "]": "["
}

open_parens = {"(", "{", "["}
# close_parens = {")", "}", "]"}
    
def is_valid(tokens):
    stack = []
    curr_paren, curr_total = (None, None)
    is_valid = True
    for c in tokens:
        if c in open_parens:
            if curr_paren == c:
                curr_total += 1
            else:
                if curr_paren != None:
                    stack.append((curr_paren, curr_total))
                curr_paren = c
                curr_total = 1
        else:
            open_paren = close_to_open[c]
            if curr_paren == open_paren:
                curr_total -= 1
                if curr_total == 0:
                    if len(stack) > 0:
                        curr_paren, curr_total = stack.pop()
                    else:
                        curr_paren, curr_total = (None, None)
            else:
                is_valid = False
                break

    if curr_paren != None:
        is_valid = False
                
    return is_valid

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return is_valid(s)


sol = Solution()
s = "{[]}"
result = sol.isValid(s)
print(result)
