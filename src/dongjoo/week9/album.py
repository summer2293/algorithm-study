# https://programmers.co.kr/learn/courses/30/lessons/42579
from collections import defaultdict
class Song:
    def __init__(self, genre_order, num_plays, pk):
        self.genre_order = genre_order
        self.num_plays = num_plays
        self.pk = pk

    def __repr__(self):
        return str(self.pk)


    def __gt__(self, b):
        if b.genre_order > self.genre_order:
            return False
        elif self.genre_order > b.genre_order:
            return True
        if b.num_plays > self.num_plays:
            return False
        elif self.num_plays > b.num_plays:
            return True
        return self.pk < b.pk



def find_genre_plays(genres, plays):
    # find genre order
    plays_by_genre = defaultdict(int)
    for genre, play in zip(genres, plays):
        plays_by_genre[genre] += play
    return plays_by_genre


def solution(genres, plays):
    # find genre order
    plays_by_genre = find_genre_plays(genres, plays)

    # add songs to answer
    answer = []
    item = None
    pk = 0
    for genre, play in zip(genres, plays):
        item = Song(plays_by_genre[genre], play, pk)
        pk += 1
        answer.append(item)

    answer.sort(reverse=True)
    # only return two per genre
    count = 0
    cleaned_answer = []
    seen_genres = set()
    for song in answer:
        if song.genre_order not in seen_genres:
            count = 0
        if count < 2:
            cleaned_answer.append(song.pk)
            count += 1
            seen_genres.add(song.genre_order)
        else:
            continue

    return cleaned_answer


print(solution(['classic', 'pop', 'classic', 'classic', 'pop']
               ,[500, 600, 150, 800, 2500]))
