class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        li = []
        def dfs(s = '', pa1 = 0, pa2 = 0):
            if pa1 == n:
                li.append(s + ')' * (n - pa2)) 
            else:
                dfs(s + '(', pa1 + 1, pa2)
                if pa2 < pa1:
                    dfs(s + ')', pa1, pa2 + 1) 
        
        dfs()
        return li