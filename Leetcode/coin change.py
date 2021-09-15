class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        test = [10000 for _ in range(amount + 1)]
        test[0] = 0
        answer = []
        
        for i in coins:            
            for j in range(i, amount + 1):  
                test[j] = min(test[j], test[j - i] + 1)     
        answer = test[amount]
        
        return answer if test[-1] != 10000 else -1