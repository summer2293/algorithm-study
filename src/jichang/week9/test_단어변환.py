# 단어 변환 https://programmers.co.kr/learn/courses/30/lessons/43163
def convert_words(begin, target, words):
    if target in words:
        visited = [begin]
        queue = [begin]
        counter = 1

        while(True):
            old_queue = queue[:]
            queue = []
            for word in old_queue:
                for candidate in words.copy():
                    if is_difference_one_character(word, candidate) and candidate not in visited:
                        if candidate == target:
                            return counter
                        queue.append(candidate)
                        visited.append(candidate)
                        words.remove(candidate)
            counter += 1
        return counter
    return 0


def is_difference_one_character(source, destination):
    expected = 1
    for char_s, char_d in zip(source, destination):
        if char_s != char_d:
            expected -= 1
    return expected == 0


def test_convert_words():
    assert convert_words(
        "hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0
    assert convert_words(
        "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 4


def test_is_difference_one_character():
    assert is_difference_one_character("hit", "hot") == True
    assert is_difference_one_character("hit", "thi") == False
    assert is_difference_one_character("hit", "aot") == False
    assert is_difference_one_character("hit", "cog") == False


if __name__ == '__main__':
    convert_words("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
