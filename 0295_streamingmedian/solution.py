import bisect

class MedianFinder(object):

    def __init__(self):
        self.buf = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        bisect.insort_left(self.buf, num)

    def findMedian(self):
        """
        :rtype: float
        """
        buf_len = len(self.buf)
        is_even = (buf_len % 2) == 0
        return ((self.buf[buf_len // 2 - 1] + self.buf[buf_len // 2]) / 2.0) if is_even else self.buf[buf_len // 2]


finder = MedianFinder()
finder.addNum(1)
finder.addNum(1)
finder.addNum(8)
finder.addNum(9)
finder.addNum(5)
print(finder.findMedian())
# finder.addNum(3)
# print(finder.findMedian())
