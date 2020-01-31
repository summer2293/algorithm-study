# def solution(n):
#     c = 1
#     divid_num = 1
#
#     while c > n:
#
#         divid_num += c
#         c * 3
#
#     quaternary = ""
#     rest = n
#     while n > 3:
#         a, b = divmod(n, 12)
#         n -= a * 4
#         rest = b
#         c /= 3
#         quaternary += str(a)
#
#
#     return (quaternary + str(rest)).replace("3", "4")
#
#
# print(solution(1))
# print(solution(2))
# print(solution(3))
# print(solution(4))
#
# 1
# 2
# 4
#
#
#
# 11
# 12
# 14
#
# 21
# 22
# 24
#
# 41
# 42
# 44
#
# 111
# 112
# 114
# 121
# 122
# 124
# 141
# 142
# 144
#
#
#
# 자릿수는
# 3
#  =
# 3 + 9
#  = 12
# 3 + 9 + 27
#  = 40