class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        
        li = {}
        
        INPUT = s.split(' ')
        
        for i in range(len(pattern)):
            if pattern[i] not in li:
                li[pattern[i]] = INPUT[i]

            if li[pattern[i]] != INPUT[i]:                
                return False
            
            if INPUT[i] == INPUT[i-1]:
                if pattern[i] != pattern[i-1]:
                    return False
            
        if len(pattern) != len(INPUT):
            return False

        return True