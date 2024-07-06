def pass_the_pillow(n, time):
    loop_size = (n - 1) * 2
    mod_t = time % loop_size
    return (mod_t if mod_t < n else (loop_size - mod_t)) + 1

class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        return pass_the_pillow(n, time)


sol = Solution()
n = 4
time = 5
# n = 3
# time = 2
result = sol.passThePillow(n, time)
print(result)
