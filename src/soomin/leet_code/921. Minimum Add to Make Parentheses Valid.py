# 으냥캐리
# 921. Minimum Add to Make Parentheses Valid
# Runtime: 32 ms, faster than 92.22% of Python3 online submissions for Minimum Add to Make Parentheses Valid.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Minimum Add to Make Parentheses Valid.
# Next challenges:
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        while("()" in S):
            S = S.replace("()","")
        return len(S)