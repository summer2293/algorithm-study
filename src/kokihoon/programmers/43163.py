def solution(begin, target, words):
    answer = 0
    
    if target not in set(words):
        return 0
    
    list_word = [begin]
    
    while len(words) != 0:
        for value in list_word:
            temp = []
            for word in words:
                count = 0
                for index in range(len(word)):
                    if value[index] != word[index]:
                        count+=1
                    if count == 2:
                        break
                if count == 1:
                    temp.append(word)
                    words.remove(word)
        
        answer += 1
        if target == "".join(temp):
            return answer
        else:
            list_word = temp
            
    return answer