class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        firstpa = 0
        secondpa = 0
        
        for INPUT in s:
            if(INPUT == '('):
                firstpa += 1
                
            elif(INPUT == ')'):
                if(firstpa > 0):
                    firstpa -= 1
                else:
                    secondpa += 1
    
        return firstpa + secondpa
            
            