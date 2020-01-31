```python
# 다트게임 https://programmers.co.kr/learn/courses/30/lessons/17682
import re
exponents = {'S': 1, 'D': 2, 'T': 3}


def dart_game(dart):
    """다트게임의 문자열이 주어지면 총점수를 반환하라.

    
    """
    return mathematical_expression_to_score(
        make_mathematical_expression(game_to_token(split_dart_game(dart))))


def mathematical_expression_to_score(mathematical_expressions):

    total = 0
    for mathematical_expression in mathematical_expressions:
        total += mathematical_expression[0] ** mathematical_expression[1] * \
            mathematical_expression[2]
    return total


def make_mathematical_expression(game_token):
    result = []
    for token in game_token:
        coefficient = 1
        if token[2]:
            if token[2] == '*':
                coefficient = 2
                if result:
                    old = result.pop()
                    new = (old[0], old[1], old[2]*coefficient)
                    result.append(new)
            else:
                coefficient = -1
        mathematical_expression = (
            int(token[0]), exponents[token[1]], coefficient)
        result.append(mathematical_expression)

    return result


def game_to_token(splited_dart_game):
    result = []

    for game in splited_dart_game:
        base = re.findall(r"\d{1,2}", game)[0]
        exponent = re.findall(r"[A-Z]", game)[0]
        coefficient = re.findall(
            r"[#*]", game)[0] if re.findall(r"[#*]", game) else ''
        game_tuple = (base, exponent, coefficient)
        result.append(game_tuple)

    return result


def split_dart_game(dart):
    m = re.findall(r"\d{1,2}\w[#*]*", dart)
    return m


def test_dart_game():
    assert dart_game('1S2D*3T') == 37
    assert dart_game('1D#2S*3S') == 5


def test_mathematical_expression_to_score():
    assert mathematical_expression_to_score([(1, 1, 2),
                                             (2, 2, 2),
                                             (3, 3, 1)]) == 37
    assert mathematical_expression_to_score([(1, 2, -2),
                                             (2, 1, 2),
                                             (3, 1, 1)]) == 5


def test_make_mathematical_expression():
    assert make_mathematical_expression(
        [('1', 'S', ''),
         ('2', 'D', '*'),
         ('3', 'T', '')]) == [(1, 1, 2),
                              (2, 2, 2),
                              (3, 3, 1)]
    assert make_mathematical_expression(
        [('1', 'D', '#'),
         ('2', 'S', '*'),
         ('3', 'S', '')]) == [(1, 2, -2),
                              (2, 1, 2),
                              (3, 1, 1)]


def test_game_to_token():
    assert game_to_token(['1S', '2D*', '3T']) == [('1', 'S', ''),
                                                  ('2', 'D', '*'),
                                                  ('3', 'T', '')]
    assert game_to_token(['1D#', '2S*', '3S']) == [('1', 'D', '#'),
                                                   ('2', 'S', '*'),
                                                   ('3', 'S', '')]


def test_split_dart_game():
    assert split_dart_game('1S2D*3T') == ['1S', '2D*', '3T']
    assert split_dart_game('1D#2S*3S') == ['1D#', '2S*', '3S']
    assert split_dart_game('1S*2T*3S') == ['1S*', '2T*', '3S']
    assert split_dart_game('10S*2T*10S#') == ['10S*', '2T*', '10S#']

```

```python
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

```

```python
# 실패율 https://programmers.co.kr/learn/courses/30/lessons/42889
from collections import Counter

def failure_rate(N, stages):
    """스테이지의 수 N과 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 주어질 때, 실패율이 높은 스테이지부터
    내림차순으로 스테이지의 번호가 담겨있는 배열을 구한다.

    시간 복잡도:
    stages의 길이를 s, 스테이지의 수를 N이라고 할 때
    O(s)

    """
    stages_dict = Counter(stages)
    denominator = len(stages)
    failure_rating = {}

    for index in range(1, N+1):
        try:
            failure_rating[index] = (stages_dict[index] / denominator)
            denominator -= stages_dict[index]
        except:
            failure_rating[index] = 0

    answer = []
    
    for key in sorted(failure_rating.items(), key=lambda failure_rating: failure_rating[1], reverse=True):
        answer.append(key[0])
    return answer


def test_failure_rate():
    assert failure_rate(5, [2, 1, 2, 6, 2, 4, 3, 3]) == [3, 4, 2, 1, 5]
    assert failure_rate(4, [4, 4, 4, 4, 4]) == [4, 1, 2, 3]
```

```python
# 예산 https://programmers.co.kr/learn/courses/30/lessons/12982
def budget(d, budget):
    """예산(budget)과 부서별 신청한 금액(d)이 주어지면 최대 몇 팀에게 지원할 수 있는지 구한다.

    시간 복잡도:
    d의 길이를 n이라고 할 때 O(nlogn)

    """
    d.sort()
    
    for index, money in enumerate(d):
        budget -= money
        if budget < 0:
            return index
    return len(d)

def test_budget():
    assert budget([1, 3, 2, 5, 4], 9) == 3
    assert budget([2, 2, 3, 3], 10) == 4

```

```python
# 완주하지 못한 선수 https://programmers.co.kr/learn/courses/30/lessons/42576
from collections import Counter

def an_incomplete_player(p, c):
    """참가자와 완주한 사람의 목록이 주어지고 완주하지 못한 선수를 구한다.

    시간 복잡도:
    p의 길이를 n이라고 할 때 O(p)
    """
    return list((Counter(p) - Counter(c)).keys())[0]


def test_an_incomplete_player():
    assert an_incomplete_player(["leo", "kiki", "eden"],
                                ["eden", "kiki"])\
        == "leo"
    assert an_incomplete_player(["marina", "josipa", "nikola", "vinko", "filipa"],
                                ["josipa", "filipa", "marina", "nikola"])\
        == "vinko"
    assert an_incomplete_player(["mislav", "stanko", "mislav", "ana"],
                                ["stanko", "ana", "mislav"])\
        == "mislav"

```

```python
# 자릿수더하기 https://programmers.co.kr/learn/courses/30/lessons/12931
def digits_plus(n):
    """정수의 자릿수를 더한다.

    시간 복잡도:
    n의 자릿수가 m일 때 O(m)

    """
    sum_of_digit = 0
    for digit in str(n):
        sum_of_digit += int(digit)
    return sum_of_digit


def test_digits_plus():
    assert digits_plus(123) == 6
    assert digits_plus(987) == 24
    assert digits_plus(10002) == 3

```

```python
def sum_of_array(arr1, arr2):
    """두 행렬의 덧셈을 구하라.

    시간 복잡도:
    arr1가 M x N 크기의 행렬이라고 할 떄 O(NM)
    """
    return [sum_of_rows_in_arrays(arr1[row], arr2[row]) for row in range(len(arr1))]


def sum_of_rows_in_arrays(row1, row2):
    return [row1[row] + row2[row] for row in range(len(row1))]


def test_sum_of_array():
    assert sum_of_array([[1, 2],
                         [2, 3]],
                        [[3, 4],
                         [5, 6]]) == [[4, 6],
                                      [7, 9]]
    assert sum_of_array([[1], [2]],
                        [[3], [4]]) == [[4], [6]]

def test_sum_of_rows_in_arrays():
    assert sum_of_rows_in_arrays([1, 2], [3, 4]) == [4, 6]
    assert sum_of_rows_in_arrays([1], [3]) == [4]

```
