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
