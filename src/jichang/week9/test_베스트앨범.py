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


"""
old solution

def solution(genres, plays):
    genres_sum = dict()
    for i in zip(genres, plays, range(0, len(genres))):
        genres_sum[(i[0])] = genres_sum.get(i[0], 0) + i[1]
    genres_sum = sorted(genres_sum.items(), key=lambda x: x[1], reverse=True)
    answers = list()
    for genre in genres_sum:
        temp = gather_specific_genre(zip(genres, plays, range(0, len(genres))), list(), genre)
        add_max_two(temp, answers)
    return answers


def gather_specific_genre(zipped, temp, genre):
    for genre_plays in zipped:
        temp = check_value_then_append(genre_plays, genre, temp)
    temp = sorted(temp, key=lambda x: x[1], reverse=True)
    return temp


def check_value_then_append(origin, target, result):
    if origin[0] == target[0]:
        result.append(origin)
    return result


def add_max_two(temp, results):
    results.append(temp[0][2])
    temp.pop(0)
    if temp:
        results.append(temp[0][2])
    return results
"""
