from collections import OrderedDict
def solution(genres, plays):
    genres_best = {}
    answer = []

    for idx in range(len(genres)):
        for category in set(genres):
            TOTAL_TIME = 0
            if category == genres[idx]:
                try:
                    genres_best[category][TOTAL_TIME] += plays[idx]
                    add_play_list(genres_best[category][1], idx, plays)
                except:
                    genres_best[category] = [plays[idx], {idx: plays[idx]}]
    total_sorted_genres = sorted(genres_best.items(), key=lambda x: x[1], reverse=True)
    for plays in total_sorted_genres:
        sorted_best_plays = list(OrderedDict(sorted(plays[1][1].items(), key=lambda t:t[1], reverse=True)).keys())
        answer += sorted_best_plays[:2]
    
    return answer
        
def add_play_list(top_music, idx, plays):
    top_music[idx] = plays[idx]
    return top_music