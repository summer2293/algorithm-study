## week9

#### 단어변환

처음에는 counter 를 통해 갯수 1인애들 묶어서 recursive 를 돌리면 어떨까 생각했는데 
progress compress 이런 카운터들은 못잡을 것 같다고생각 (순서가 없으니까)
결국 배낌..개어렵다

```python
from collections import deque

transistable = lambda word,begin: sum((1 if word!=begin else 0) for word,begin in zip(word,begin)) == 1

def solution(begin, target, words):
    q, next_possible_words= deque(), dict()
    q.append((begin, 0))
    next_possible_words[begin] = set(filter(lambda x:transistable(x,begin), words))
    print(q, next_possible_words)
    for word in words:
        next_possible_words[word] = set(filter(lambda x:transistable(x,word), words))
       
    while q:
        cur, level  = q.popleft()
        if level > len(words):
            return 0
        for w in next_possible_words[cur]:
            if w == target:
                return level + 1
            else:
                q.append((w, level + 1))
    
    return 0
```



#### N-Queen

미쳤다.. 2시간동안 봤는데 코드 이해 불가 ㅠㅡㅠ 그래서 배낌 그리고 코드 이해 못함 ㅠ0ㅠ

```python

def promising(i,col):
    k=0
    correct=True
    while (k<i and correct): 
        if (col[i]==col[k] or abs(col[i]-col[k])==i-k):
            correct=False
            break
        k+=1
    return correct

def queens(n,i,col,count):
    if (promising(i,col)): # queue 배치할 수 있는지 체크 
        if (i==n-1):
            count.append(col)
        else:
            for j in range(n):
                col[i+1]=j
                queens(n,i+1,col,count)

def solution(n):
    col= [0] * n  
    global count
    count=[]
    queens(n,-1,col,count)
    return len(count)

# https://geonlee.tistory.com/40
```



#### 베스트 앨범

쉬운것 같으면서 은근 머리 쓸게 많아서 어려웠다. 더깔끔한 코드 를 고민해 봐야지

```python

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
```