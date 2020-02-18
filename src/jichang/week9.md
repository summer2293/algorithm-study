셔틀 버스

```python
def fromstrint(strTime):
    return int(strTime[:2])*60 + int(strTime[3:])


def fromintstr(intTime):
    return str(intTime // 60).zfill(2) + ":" + str(intTime % 60).zfill(2)

def solution(n, t, m, timetable):
    busTime = []
    for i in range(n):
        time = t*i
        busTime.append(540+time)
    inttimetable = []
    timetable.sort()
    for i in timetable:
        inttimetable.append(fromstrint(i))
    count = 0
    while len(busTime) != 1:
        if not inttimetable:
            break
        elif count == m or busTime[0] < inttimetable[0]:
            count =0
            busTime.pop(0)
        elif busTime[0] >= inttimetable[0]:
            inttimetable.pop(0)
            count += 1
            
    if len(inttimetable) < m:
        answer = fromintstr(busTime[0])
    else:
        for i in range(busTime[0], -1, -1):
            inttimetable.append(i+0.1)
            inttimetable.sort()
            if i+0.1 in inttimetable[0:m]:
                answer = fromintstr(i)
                break
            else:
                inttimetable.remove(i+0.1)
    return answer
```


베스트 앨범

```python
"""
장르, 재생횟수를 순회하며 가장 많이 재생된 노래의 장르를 구하자.
장르내에서 많이 재생된 노래를 구하자.

"""
import operator


def best_album(genres, plays):
    best_genre = best_genres(genres, plays)
    return best_songs_by_genres(best_genre, genres, plays)


def best_genres(genres, plays):
    songs = dict()
    for genre, play in zip(genres, plays):
        try:
            songs[genre] += play
        except:
            songs[genre] = play

    sorted_songs = sorted(
        songs.items(), key=operator.itemgetter(1), reverse=True)
    sorted_songs = [i[0] for i in sorted_songs]
    return sorted_songs


def best_songs_by_genres(sorted_songs, genres, plays):
    songs = dict()
    best_song_list = []
    for index, (genre, play) in enumerate(zip(genres, plays)):
        try:
            songs[genre].append((index, play))
        except:
            songs[genre] = [(index, play)]

    for best_genre in sorted_songs:
        genre_song_list = songs[best_genre]
        sorted_specific_genre_song = sorted(genre_song_list, reverse=True, key=lambda l:l[1])
        for index in range(min(2, len(sorted_specific_genre_song))):
            if sorted_specific_genre_song[index]:
                best_song_list.append(sorted_specific_genre_song[index][0])
    return best_song_list


def test_best_album():
    assert best_album(["classic", "pop", "classic", "classic", "pop"],
                      [500, 600, 150, 800, 2500]) == [4, 1, 3, 0]
    assert best_album(["classic", "pop", "classic", "classic", "pop"],
                      [500, 600, 150, 800, 500]) == [3, 0, 1, 4]
    assert best_album(["classic", "pop", "classic", "classic"],
                      [500, 600, 150, 800, 500]) == [3, 0, 1]

def test_best_genres():
    assert best_genres(["classic", "pop", "classic", "classic", "pop"],
                       [500, 600, 150, 800, 2500]) == ['pop', 'classic']
    assert best_genres(["classic", "pop", "classic", "classic", "pop"],
                       [500, 600, 150, 800, 500]) == ['classic', 'pop']


def test_best_songs_by_genres():
    assert best_songs_by_genres(['pop', 'classic'], ["classic", "pop", "classic", "classic", "pop"],
                       [500, 600, 150, 800, 2500]) == [4, 1, 3, 0]

if __name__ == '__main__':
    best_songs(['pop', 'classic'], ["classic", "pop", "classic", "classic", "pop"],
               [500, 600, 150, 800, 2500])  # == [4, 1, 3, 0]

```

단어 변환

```python
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

```