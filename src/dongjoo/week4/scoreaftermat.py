# 861. Score After Flipping Matrix
from typing import List
class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        # check first column, flipping first column is always better
        # because exponentiation is always 1 bigger than summation for this case

        # take care of first column
        for rowidx in range(len(A)):
            if A[rowidx][0] == 0:
                A[rowidx] = [~elem + 2 for elem in A[rowidx]] #bit shift for two's complement
    
        # take care of rows after that with greedy approach
        colidx = 1
        rowidx = 0
        zeros = 0 # count of zeros in each col
        while colidx < len(A[0]):
            # while loop to count zero in each col
            while rowidx < len(A):
                if A[rowidx][colidx] == 0:
                    zeros += 1
                rowidx += 1

            # print("zeros counted", zeros)
            if zeros > len(A)//2: #check to see if more zeros in row, flip row if so
                tempidx = 0 # temp row idx
                # while loop to flip row
                # print("before flipping", A)
                while tempidx < len(A):
                    A[tempidx][colidx] = ~A[tempidx][colidx] + 2
                    tempidx += 1
                # print("AFTER flipping", A)

            zeros = 0 # reset zeros
            rowidx = 0 # reset rowidx
            colidx += 1 # move one column to right

        answer = 0
        expo = len(A[0])-1 # exponentiation for 2 to sum over A
        for row in A:
            for elem in row:
                answer += elem * (2 ** expo)
                expo -= 1
            expo = len(A[0])-1
        # print(A)
        return answer


answer = Solution()
print(answer.matrixScore([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]))


# Runtime: 40 ms, faster than 95.31 % of Python3 online submissions for Score After Flipping Matrix.
# Memory Usage: 12.9 MB, less than 100.00 % of Python3 online submissions for Score After Flipping Matrix.
