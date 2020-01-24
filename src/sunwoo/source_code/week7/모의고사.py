def solution(answers):
    persons = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    scores = [0, 0, 0]

    for i, answer in enumerate(answers):
        for person_index, person in enumerate(persons):
            if person[i % len(person)] == answer:
                scores[person_index] += 1

    max_count = max(scores)
    result = []
    for i, counter in enumerate(scores):
        if counter == max_count:
            result.append(i + 1)

    return result