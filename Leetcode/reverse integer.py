class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        
        if x > 0:
            while x > 0:
                result = result * 10 + x % 10
                x = x // 10
            return result if -2**31 <= result <= 2**31 - 1 else 0
        
        else:
            x *= -1
            while x > 0:
                result = result * 10 + x % 10
                x = x // 10
            result *= -1 
            return result if -2**31 <= result <= 2**31 - 1 else 0
        