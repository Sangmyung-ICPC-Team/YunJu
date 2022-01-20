class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        one = 0
        zero = 0
        for i in position:
            if(i % 2 != 0):
                one+=1
            else:
                zero+=1
                
        return min(one, zero)