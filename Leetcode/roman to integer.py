class Solution:
    def romanToInt(self, s: str) -> int:
        hash = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 
        }
        
        ans = 0
        for i in range(len(s) - 1):
            if hash[s[i]] < hash[s[i+1]]:
                ans -= hash[s[i]]
            else:
                ans += hash[s[i]]
        return ans + hash[s[-1]]