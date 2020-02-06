def solution(genres, plays):
    answer = []
    set_dict = {}
    list_1 = []
    for i,(x, y) in  enumerate(zip(genres, plays)):
        list_1.append((i,x, y))
        if x in set_dict:
            set_dict[x] += y
        else:
            set_dict[x] = y
    
    sdict= sorted(set_dict.items(), reverse=True) # 합의 최대값 순으로 정렬
    list_1 = sorted(list_1, key = lambda x: (x[1], -x[2]))

    check = 0
    for x, y in sdict:
        for x1,y1,z1 in list_1:
            print(x1, y1, z1)
            if x == y1:
                answer.append(x1)
                check += 1
            
            if check == 2 or (check == 1 and y1 != x):
                check = 0
                break
                
    return answer