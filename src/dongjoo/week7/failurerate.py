# https://programmers.co.kr/learn/courses/30/lessons/42889

from collections import Counter
def solution(N, stages):
    # count how many people are in each level
    levels = Counter(stages)

    # failure rate hashtable
    failure_rate = dict()
    # number of total people in and above a certain levels, works as denominator
    denom = len(stages)
    # current level
    curr_level = 1

    while curr_level <= N:
        # skip over levels where everyone that reached it has passed
        if curr_level not in levels:
            failure_rate[curr_level] = 0
            curr_level += 1
            continue
    
        # handle cases where there exists users that passed every level
        if curr_level > N:
            # try except for when divide by 0 error
            try:
                failure_rate[N] = levels[N] / (levels[N] + levels[N+1])
            except:
                failure_rate[N] = 0
            break
        
        # calculate failure rate for regular levels    
        failure_rate[curr_level] = (levels[curr_level]/denom)
        denom -= levels[curr_level]
        curr_level += 1

    answer = [(rate, level) for level, rate in failure_rate.items()]
    answer.sort(key=lambda x: (-x[0], x[1]))
    # print(answer)
    return [x[1] for x in answer]

# space complexity: linear
# time complexity: linear

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4,[4,4,4,4,4]))



# bad first solution

# def solution(N, stages):
#     success_rates = []
#     stages.sort()
#     denom = len(stages) # total number of people
#     prev_stage = stages[0]
#     for num_cleared, stage in enumerate(stages):
#         if stage > N:
#             break
#         if prev_stage != stage:
#             # for when certain stages were "skipped"
#             if len(success_rates) < stage:
#                 success_rates.append([1] * (stage - prev_stage))
#             else:
#                 pass
#         prev_stage = stage


#     return fail_rates
