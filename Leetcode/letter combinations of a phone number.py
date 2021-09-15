class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digit = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs',
                 '8': 'tuv', '9': 'wxyz'
        }
        
        result = []

        if len(digits) == 0:
            return result
        
        if len(digits) == 1:
            for i in digit[digits]:
                result.append(i)     
            return result
    
        if len(digits) == 2:
            for i in digit[digits[0]]:
                for j in digit[digits[1]]:
                    result.append(i+j)
            return result
        
        if len(digits) == 3:
            for i in digit[digits[0]]:
                for j in digit[digits[1]]:
                    for k in digit[digits[2]]:
                        result.append(i+j+k)
            return result
        
        if len(digits) == 4:
            for i in digit[digits[0]]:
                for j in digit[digits[1]]:
                    for k in digit[digits[2]]:
                        for l in digit[digits[3]]:
                            result.append(i+j+k+l)
            return result