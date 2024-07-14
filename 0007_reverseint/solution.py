order_limits = [7, 4, 6, 3, 8, 4, 7, 4, 1, 2]

def reverse(num):
    result = 0
    is_negative = num < 0
    num = num * -1 if is_negative else num

    order = 1
    digits = []
    while order < 10 and num >= (10 ** order):
        magnitude = 10 ** order
        mag_value = num % magnitude
        
        digit = mag_value / (magnitude / 10)
        digits.append(digit)

        num -= mag_value
        order += 1

    order -= 1
    digits.append(num / (10 ** order))

    danger = order > 8
    for digit in digits:
        if danger:
            limit_digit = order_limits[order]
            if digit > limit_digit:
                return 0
            elif digit < limit_digit:
                danger = False

        result += digit * (10 ** order)
        order -= 1

    return int(result * -1 if is_negative else result)

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        return reverse(x)


sol = Solution()
x = 1234567
result = sol.reverse(x)
print(result)
