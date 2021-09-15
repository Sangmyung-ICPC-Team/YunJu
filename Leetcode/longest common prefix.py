class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]
    
        for inputs in strs[0:]:
            for word in range(0, len(prefix)):
                if word >= len(inputs) or inputs[word] != prefix[word]:
                    prefix = prefix[0:word]
                    break
                    
        if not strs:
            return ""
        
        return prefix