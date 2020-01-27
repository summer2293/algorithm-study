# 괄호변환 https://programmers.co.kr/learn/courses/30/lessons/60058
from collections import Counter

def make_correct_bracket_string(balanced_bracket_string):
    if is_correct_bracket(balanced_bracket_string):
        return balanced_bracket_string
    else:
        return split_u_and_v(balanced_bracket_string)


def is_correct_bracket(bracket_string):
    if not bracket_string:
        return True
    if bracket_string.replace("()", "") == bracket_string:
        return not bool(bracket_string)
    return is_correct_bracket(bracket_string.replace("()", ""))


def split_u_and_v(w):
    if w == "":
        return ""
    else:
        u, v = no_longer_separable_balanced_bracket_string(w)
        if is_correct_bracket(u):
            return u + split_u_and_v(v)
        else:
            added_string = split_u_and_v(v)
            new_u = [')' if i == '(' else '(' for i in u[1:-1]]
            
            new_bracket_string = "(" + added_string + ")" + ''.join(new_u)
            return new_bracket_string



def no_longer_separable_balanced_bracket_string(w):
    for index in range(2, len(w), 2):
        if Counter(w[:index])[')'] == Counter(w[:index])['(']:
            return (w[:index], w[index:])
    return (w, "")


def test_make_correct_bracket_string():
    assert make_correct_bracket_string("") == ""
    assert make_correct_bracket_string("()()") == "()()"
    assert make_correct_bracket_string(")(") == "()"
    assert make_correct_bracket_string("(()())()") == "(()())()"
    assert make_correct_bracket_string(")(()()()") == "(()()())"

    """
    )(
    )()()(

    ( ()()() )
    """


def test_is_correct_bracket():
    assert is_correct_bracket("(())") == True
    assert is_correct_bracket("") == True
    assert is_correct_bracket(")()(") == False
    assert is_correct_bracket("()()") == True
    assert is_correct_bracket(")(") == False
    assert is_correct_bracket("(()())()") == True
    assert is_correct_bracket("()))((()") == False


def test_split_u_and_v():
    assert split_u_and_v(")(") == "()"
    assert split_u_and_v("()))((()") == "()(())()"
    assert split_u_and_v("(()())()") == "(()())()"


def test_no_longer_separable_balanced_bracket_string():
    assert no_longer_separable_balanced_bracket_string(")(") == (")(", "")
    assert no_longer_separable_balanced_bracket_string("()))((()") == ("()", "))((()")
    assert no_longer_separable_balanced_bracket_string("))((()") == ("))((", "()")


if __name__ == '__main__':
    make_correct_bracket_string(")(")
    