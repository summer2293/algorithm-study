# 921. Minimum Add to Make Parentheses Valid
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        # decrease counter for ')' and increase for '('
        count = 0
        idx = 0
        answer = 0
        while idx < len(S):
            if S[idx] == ")":
                count -= 1
            elif count>= 0 and S[idx] == "(":
                count += 1
            elif count < 0 and S[idx] == "(":
                answer += abs(count)
                count = 1
            idx += 1
        return answer + abs(count)


                     

answer = Solution()

print(answer.minAddToMakeValid("((("))


# Runtime: 28 ms, faster than 98.99% of Python3 online submissions for Minimum Add to Make Parentheses Valid.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Minimum Add to Make Parentheses Valid.