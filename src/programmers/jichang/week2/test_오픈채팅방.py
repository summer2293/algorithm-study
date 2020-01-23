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
