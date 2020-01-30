def solution(w,h):
    if(w == h):
        return w*h-w
    else :
        a = w
        b = h
        # 최대 공약수 구하는부분 start
        if b>a:
            tmp = a
            a = b
            b = tmp
        while b>0:
            c = b
            b = a % b
            a = c
        # end
        return w*h - (w+h-a)