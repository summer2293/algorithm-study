```python
"""
숫자를 가만보니 124나라의 숫자는 마지막 자리수가 124로 반복되는 것을 알 수 있었다.
앞자리수도 같은것이 3개씩 있는 묶음으로 반복되는 것을 알 수 있었다.

이를 풀어쓴다면, 
어떤수를 3으로 나눴을 때 나머지가 0, 1, 2이면 124나라로 변환했을 때 각각 4, 1, 2이다.

그리고 어떤수 - 1을 3으로 나눴을 때 몫이 앞의 자리수에 채워진다.
"""


def make_124_number(n):
    if n <= 3:
        return '124'[n-1]
    else:
        return make_124_number((n - 1) // 3) + make_124_number(n % 3)


def test_make_124_number():
    assert make_124_number(1) == '1'
    assert make_124_number(2) == '2'
    assert make_124_number(3) == '4'
    assert make_124_number(4) == '11'
    assert make_124_number(5) == '12'
    assert make_124_number(6) == '14'
    assert make_124_number(7) == '21'
    assert make_124_number(8) == '22'
    assert make_124_number(9) == '24'
    assert make_124_number(10) == '41'


"""
다른 풀이
"""
def change124(n):
    if n <= 3:
        return '124'[n-1]
    else:
        q, r = divmod(n-1, 3)
        return change124(q) + '124'[r]


```

```python
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
    
```

```python
"""
솔루션을 봤음
"""

from math import gcd

def available_square(W, H):
    return W * H - W - H + gcd(W, H)


def test_available_square():
    assert available_square(8, 12) == 80
    assert available_square(2, 3) == 2
    assert available_square(4, 6) == 16
    assert available_square(5, 7) == 24
    assert available_square(3, 7) == 12
    assert available_square(5, 5) == 20
    assert available_square(10, 20) == 200 - 20

```

```python
def valid_skill_trees(skill, skill_trees):
    counter = 0
    for trees in skill_trees:
        pre_skill = ''
        for skill_tree in trees:
            if skill_tree in skill:
                pre_skill += skill_tree
        if skill.startswith(pre_skill):
            counter += 1
    return counter
        
    

def test_valid_skill_trees():
    assert valid_skill_trees("CBD", ["BACDE", "CBADF", "AECB", "BDA"]) == 2
```

```python
def get_open_chatting_messages(record):
    messages_with_uid = []
    uid_to_name = dict()

    for line in record:
        human_readable_message_with_id = make_human_readable_message_with_id(line.split())
        uid_to_name = make_uid_to_name(line.split(), uid_to_name)
        if human_readable_message_with_id:
            messages_with_uid.append(human_readable_message_with_id)

    messages_with_name = []
    for line in messages_with_uid:
        messages_with_name.append(
            uid_to_name[line[0]] + line[1] + ' ' + line[2])
    return messages_with_name


def make_uid_to_name(parsed_message, uid_to_name):
    do = ['Enter', 'Change']
    if parsed_message[0] in do:
        uid_to_name[parsed_message[1]] = parsed_message[2]
    return uid_to_name


def make_human_readable_message_with_id(message_token):
    do = {'Enter': '들어왔습니다.', 'Leave': "나갔습니다."}
    try:
        do[message_token[0]]
        return [message_token[1], '님이', do[message_token[0]]]
    except:
        pass


def change_uid_to_name(str_list, uid_to_name):
    if str_list is None:
        return None
    return uid_to_name[str_list[0]] + str_list[1] + ' ' + str_list[2]


def test_get_open_chatting_messages():
    assert get_open_chatting_messages(
        ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234",
         "Enter uid1234 Prodo", "Change uid4567 Ryan"]) ==\
        ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.",
         "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]


def test_make_uid_to_name():
    assert make_uid_to_name(['Enter', 'uid1234', 'Muzi'], dict()) == {
        'uid1234': 'Muzi'}
    assert make_uid_to_name(['Leave', 'uid1234'], dict()) == {}
    assert make_uid_to_name(['Change', 'uid4567', 'Ryan'], dict()) == {
        'uid4567': 'Ryan'}
    assert make_uid_to_name(['Enter', 'uid1234', 'Muzi'], {'uid4567': 'Ryan'}) == {
        'uid1234': 'Muzi', 'uid4567': 'Ryan'}
    assert make_uid_to_name(['Change', 'uid1234', 'Muzi'], {
                            'uid1234': 'Ryan'}) == {'uid1234': 'Muzi'}


def test_make_human_readable_message_with_id():
    assert make_human_readable_message_with_id(
        ['Enter', 'uid1234', 'Muzi']) == ["uid1234", "님이", "들어왔습니다."]
    assert make_human_readable_message_with_id(
        ['Leave', 'uid1234']) == ["uid1234", "님이", "나갔습니다."]
    assert make_human_readable_message_with_id(
        ['Change', 'uid4567', 'Ryan']) == None


def test_change_uid_to_name():
    assert change_uid_to_name(["uid1234", "님이", "들어왔습니다."], {
                              'uid1234': 'Muzi'}) == "Muzi님이 들어왔습니다."

```