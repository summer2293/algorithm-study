def solution(n, computers):
    answer = 0
    enumerated_link = enumerate(computers)

    queue = []

    current_queue = [enumerated_link.next()]
    while len(current_queue) > 0:
        queue += current_queue

    return answer

count = [
    solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]),
    solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])
]
print(count)