class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        
        if m == 1 or n == 1:
            return 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        return dp[n-1]
        