import math

# TODO: speed optimizations
def num_squares_impl(n, depth, cache={}):
    if n in cache:
        return cache[n]
    
    sqrt_n = int(math.sqrt(n))
    closest_square = sqrt_n * sqrt_n
    if closest_square == n:
        cache[n] = 1
        return 1
    
    i = sqrt_n
    lowest_count = n
    for i in range(sqrt_n, 0, -1):
        new_depth = depth + 1
        if new_depth >= lowest_count:
            break

        i_sqrd = i * i
        lowest_count = min(lowest_count, 1 + num_squares_impl(n - i_sqrd, new_depth, cache))
    
    return lowest_count

def num_squares(n):
    cache = {}
    return num_squares_impl(n, 0, cache)

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        return num_squares(n)


sol = Solution()
n = 56
result = sol.numSquares(n)
print(result)
