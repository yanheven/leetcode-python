class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        return int(math.sqrt(n))


if __name__ == '__main__':
    s = Solution()
    print(s.bulbSwitch(5))
