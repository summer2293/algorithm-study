"""
장르, 재생횟수를 순회하며 가장 많이 재생된 노래의 장르를 구하자.
장르내에서 많이 재생된 노래를 구하자.

"""
import operator

def best_album(genres, plays):
    best_genre = best_genres(genres, plays)
    best_album_songs = best_songs(best_genre, genres, plays)
    return best_album_songs

def best_genres(genres, plays):
    songs = dict()
    for genre, play in zip(genres, plays):
        try:
            songs[genre] += play
        except:
            songs[genre] = play
    
    sorted_songs = sorted(songs.items(), key=operator.itemgetter(1), reverse=True)
    sorted_songs = [i[0] for i in sorted_songs]
    return sorted_songs
    

def best_songs(best_genre, genres, plays):
    best_song_index = []
    for b_genre in best_genre:
        songs_for_best_genre = []
        for index, (genre, play) in enumerate(zip(genres, plays)):
            if b_genre == genre:
                if songs_for_best_genre:
                    if play > songs_for_best_genre[-1][1]:
                        if len(songs_for_best_genre) == 1:
                            songs_for_best_genre.insert(0, (index, play))
                        else:
                            if len(songs_for_best_genre) == 2:
                                if songs_for_best_genre[0][1] < play:
                                    songs_for_best_genre.insert(0, (index, play))
                                    songs_for_best_genre.pop()
                                else:
                                    songs_for_best_genre.pop()
                                    songs_for_best_genre.append((index, play))
                else:
                    songs_for_best_genre.append((index, play))
        for song in songs_for_best_genre:
            best_song_index.append(song[0])
    return best_song_index


def test_best_album():
    assert best_album(["classic", "pop", "classic", "classic", "pop"],
                      [500, 600, 150, 800, 2500]) == [4, 1, 3, 0]

def test_best_genres():
    assert best_genres(["classic", "pop", "classic", "classic", "pop"],
                      [500, 600, 150, 800, 2500]) == ['pop', 'classic']
    assert best_genres(["classic", "pop", "classic", "classic", "pop"],
                       [500, 600, 150, 800, 500]) == ['classic', 'pop']

def test_best_songs():
    assert best_songs(["pop", "classic"], ["classic", "pop", "classic", "classic", "pop"],
                      [500, 600, 150, 800, 2500]) == [4, 1, 3, 0]

if __name__ == '__main__':
    best_songs(['pop', 'classic'], ["classic", "pop", "classic", "classic", "pop"],
                      [500, 600, 150, 800, 2500]) #== [4, 1, 3, 0]


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