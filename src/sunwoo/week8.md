## 멀쩡한 사각형

##### Solution

```python
def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def solution(w, h):
    return w * h - w - h + gcd(w, h)
```

##### 다른사람 풀이 참고

```python
def gcd(a, b):
    return b if a == 0 else gcd((b % a), a)

def solution(w, h):
    return w * h - w - h + gcd(w, h)
```



## 괄호변환

```python
def solution(p):
    if len(p) == 0: return ''
    left, right = p[0], ''
    count = 1 if left == '(' else -1

    for c in p[1:]:
        if count == 0:
            right += c
        else:
            count += 1 if c == '(' else -1
            left += c

    if valid(left):
        return left + solution(right)
    else:
        answer = '(' + solution(right) + ')'
        for c in left[1:-1]:
            answer += '(' if c == ')' else ')'
        return answer

def valid(p):
    list = []
    try:
        for c in p: list.append(c) if c == '(' else list.pop()
        return True
    except:
        return False
```