# 모의고사 https://programmers.co.kr/learn/courses/30/lessons/42840


def who_solved_the_most_problems(answers):
    """가장 많은 문제를 맞춘 사람을 구한다.
    
    시간 복잡도:
    answer의 길이가 n, 수포자의 수를 m이라고 할 때
    O(n + m)
    """
    the_answers_of_first_person = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    the_answers_of_second_person = [2, 1, 2, 3, 2, 4, 2, 5]
    the_answers_of_third_person = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    persons = [0, 0, 0]

    for index in range(len(answers)):
        if the_answers_of_first_person[index % 10] == answers[index]:
            persons[0] += 1
        if the_answers_of_second_person[index % 8] == answers[index]:
            persons[1] += 1
        if the_answers_of_third_person[index % 10] == answers[index]:
            persons[2] += 1

    top_score_person = []
    for person in range(len(persons)):
        if persons[person] == max(persons):
            top_score_person.append(person+1)

    return top_score_person


def test_who_solved_the_most_problems():
    assert who_solved_the_most_problems([1, 2, 3, 4, 5]) == [1]
    assert who_solved_the_most_problems([1, 3, 2, 4, 2]) == [1, 2, 3]
