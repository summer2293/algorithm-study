# https://programmers.co.kr/learn/courses/30/lessons/42840


def solution(answers):
    num_correct = [0, 0, 0]
    pattern_one = [1, 2, 3, 4, 5]
    pattern_three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    pattern_two = [2, 1, 2, 3, 2, 4, 2, 5]
    q_idx = 0
    for question in answers:
        if question == pattern_one[q_idx % len(pattern_one)]:
            num_correct[0] += 1
        if question == pattern_two[q_idx % len(pattern_two)]:
            num_correct[1] += 1
        if question == pattern_three[q_idx % len(pattern_three)]:
            num_correct[2] += 1
        q_idx += 1
    maximum = max(num_correct)
    answer = [i for i in range(1, 4) if num_correct[i-1] == maximum]
    return answer

print(solution([1, 3, 2, 4, 2]))
# Time complexity: linear
# Space complexity: sum (number of elements in each repeating pattern) + number of people
