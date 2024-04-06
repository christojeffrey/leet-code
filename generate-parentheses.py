
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def generate(n, currentLeft, currentRight, singleAns):

            if(currentLeft == n and currentRight == n):
                res.append(singleAns)
                return 

            if(currentLeft < n):
                generate(n, currentLeft + 1, currentRight, singleAns + "(")
            if(currentRight < currentLeft):
                generate(n, currentLeft, currentRight + 1, singleAns + ")")
                
        generate(n, 0, 0, "")
        return res
