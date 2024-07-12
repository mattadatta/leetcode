def trap(heights):
    stack = [(heights[0], 0)]
    count = 0
    i = 1
    while i < len(heights):
        height = heights[i]
        height_diff = height - stack[-1][0]

        # Ascending
        if height_diff > 0:
            while len(stack) > 1 and stack[-1][0] < height:
                popped_height, popped_index = stack.pop()
                width = i - (stack[-1][1] + 1)
                block_height = min(height, stack[-1][0]) - popped_height
                to_add = width * block_height
                count += to_add

            if len(stack) == 1:
                if stack[0][0] < height:
                    stack[0] = (height, i)
                else:
                    stack.append((height, i))
            elif stack[-1][0] > height:
                stack.append((height, i))

            else:
                stack[-1] = (height, i)
        
        # Descending
        elif height_diff < 0:
            stack.append((height, i))

        # Equivalent
        else:
            stack[-1] = (height, i)
        
        i += 1
    
    return count

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        return trap(height)


sol = Solution()
height = [4,2,0,3,2,5]
result = sol.trap(height)
print(result)
