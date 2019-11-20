# https: // programmers.co.kr/learn/courses/30/lessons/42839
# good combinations and permutations practice


from collections import Counter


def solution(numbers):
    answer = 0
    return answer


def is_prime(number):
    if number == 1:
        return False
    for i in range(2, round(number ** 0.5)+1):
        if number % i == 0:
            # print("factor is ", i)
            return False
    return True


# probably has horrible performance
def combi_dfs(counts, curr_selected, total_selected, total):
    # counts is counter, curr_selected is Counter of selected stuff
    # total_selected is list of selected sets, total is num of selections
    if sum(counts.values()) == 0:
        # print("empty potentials!!!")
        return
    if sum(curr_selected.values()) == total:
        if curr_selected not in total_selected:
            # print(total_selected)
            total_selected.append(curr_selected)
            curr_selected = Counter()
        return
    for key in counts:
        # add elements to curr_selected
        if counts[key] > 0:
            curr_selected[key] += 1
            # after adding, decrement counts
            counts[key] -= 1
            combi_dfs(counts.copy(), curr_selected, total_selected, total)
            curr_selected = Counter() # reset curr_selected


test = [1, 1, 2, 5, 7, 8, 3]

total_selected = []
curr_selected = Counter()
counts = Counter(test)
print(total_selected)
combi_dfs(counts, curr_selected, total_selected, 2)
print(total_selected)
