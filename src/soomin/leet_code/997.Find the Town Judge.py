# 997. Find the Town Judge

## trash code

import operator
from collections import Counter
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1:
            return 1
        list = [[0 for i in range(N+1) ] for j in  range(N+1)]
        people = []
        counter = {}
        for i in trust:
            list[i[0]][i[1]] = i[1]
            try:     
                counter[i[1]] += 1
            except:
                counter[i[1]] = 1
        
        p = max(counter, key=lambda key: counter[key])
        
        sum = 0 
        for i in list[p]:
            sum+=i
            if sum >= 1:
                return -1
        
        value = sorted(counter.values())
        
        if(len(value) > 1 and value[-1] == value[-2]):
            return -1

        return p