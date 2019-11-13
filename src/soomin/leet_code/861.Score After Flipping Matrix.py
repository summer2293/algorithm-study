# 861. Score After Flipping Matrix
class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        if (len(A) == 1):
            return 1
        if (len(A[0]) == 1):
            return len(A)
        
        for i in range(len(A)):
            if(A[i][0] == 0):
                A[i] = list(map(lambda x: 1-x, A[i]))

        sum = 2 ** (len(A[0])-1) * len(A)

        for i in range(1,len(A[0])):
            count = 0
            for j in range(len(A)):
                if (A[j][i] == 1):
                    count += 1
            m =  max(count,len(A)-count)
            sum += 2 ** (len(A[0])-i-1) * m
            
        return sum

# Runtime: 40 ms, faster than 93.29% of Python3 online submissions for Score After Flipping Matrix.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Score After Flipping Matrix.
# Next challenges: