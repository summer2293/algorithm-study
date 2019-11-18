# graph
# 997. Find the Town Judge
# 10:25 start end 10:39


from typing import List
# first implementation without using graph


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trusted_by = dict()
        # for loop to make potential judge sets
        for pair in trust:
            if pair[1] in trusted_by:
                trusted_by[pair[1]].add(pair[0])
            else:
                trusted_by[pair[1]] = set([pair[0]])

        # print(trusted_by, "trusted by")

        maximum = None
        max_len = 0
        # find the potential judge by running max for number of elements in set
        for person in trusted_by:
            if len(trusted_by[person]) > max_len:
                maximum = person
                max_len = len(trusted_by[person])

        # print(maximum, "max")
        # edge case for only one potential judge
        if len(trusted_by) == 1:
            return list(trusted_by.keys())[0]

        for person in trusted_by:
            # check if set contains something else not in "judge set"
            if len(trusted_by[person] - trusted_by[maximum]): 
                return -1
            if trusted_by[person] == trusted_by[maximum] and person != maximum:
                return -1
        if maximum == None:
            return N
        return maximum

answer = Solution()
print(answer.findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))

# after like 5 minor bug issues (1st strategy of using dicts and sets):
# Runtime: 772 ms, faster than 99.00 % of Python3 online submissions for Find the Town Judge.
# Memory Usage: 17.2 MB, less than 10.00 % of Python3 online submissions for Find the Town Judge.


