class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        coin = [0] * (amount + 1)
        coin[0] = 1
        
        for i in coins:
            for j in range(i, amount + 1):
                coin[j] = coin[j - i] + coin[j]
                
        return coin[amount]