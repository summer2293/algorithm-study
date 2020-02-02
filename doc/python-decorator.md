## python decorator

파이썬에서 사용하는 데코레이터 패턴에 대해 알아보자.  

#### python first-class citizen

파이썬에서는 함수를 first-class citizen 으로 취급을 한다. 다른 엔티티가 일반적으로 사용할 수 있는 모든 작업들을 지원하는 것이다. 그러면 함수를

- 변수 할당
- params 로 전달 
- return 

을 할 수 있다는 특징을 가진다.

```python
# 변수 할당 
>>> def sum(a,b):
...     return a+b
>>> a = sum(a,b)
>>> a = 1
>>> b = 2
>>> v = sum(a,b)
>>> v
3

# params 전달 
>>> def test(a,b):
...     return a + b
>>> test(5,sum(a,b))
8

# return 값 전달 
>>> def test(a,b):
...     return sum(a,b)
... 
>>> test(10,20)
30

```

sample

```python
def square(x):
    return x * x

print square(5)

f = square

print square
print f

$ python first_class_function.py 
25
<function square at 0x1018dfe60> # f == square 같은 주소를 가진다.
<function square at 0x1018dfe60>
```

sample 2 - params 로 전달

```python
def square(x):
    return x * x

num_list = [1, 2, 3, 4, 5]

def simple_square(arg_list):
    result = []
    for i in arg_list:
        result.append(i * i)
    return result

simple_squares = simple_square(num_list)

# 너무 간단한 예시여서 의미를 모르겠다면 2
def square(x):
    return x * x

def cube(x):
    return x * x * x

def quad(x):
    return x * x * x * x

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i)) # square 함수 호출, func == square
    return result

num_list = [1, 2, 3, 4, 5]

squares = my_map(square, num_list)
cubes = my_map(cube, num_list)
quads = my_map(quad, num_list)
```

sample 3 - return 으로 전달

```python
# 리턴으로 받는 
def logger(msg):
    def log_message(): #1
        print 'Log: ', msg
    return log_message

log_hi = logger('Hi')
print log_hi # log_message 오브젝트가 출력됩니다.
log_hi() # "Log: Hi"가 출력됩니다.
```

내부 함수를 호출할 수 있다. msg는 지역변수이기 때문에 참조할 수 없으나, logger 가 호출되었을때 참조가 된다.  이걸 클로저라고한다. 많이 어려우니 다음에 제대로 살펴보자! 



## 데코레이터 패턴

기존의 코드에 여러가지 기능을 추가하는 python 문법

example

```python
def decorator_function(original_function):  #1
    def wrapper_function():  #5
        return original_function()  #7
    return wrapper_function  #6


def display():  #2
    print 'display 함수가 실행됐습니다.'  #8

decorated_display = decorator_function(display)  #3

decorated_display()  #4
```

외부에서 함수를 정의 후 params 로 넘겨 실행할 수 있다.

##### 쉽게 이해할 수 있는 예제

```python
def main_function_1():
     print datetime.datetime.now()
     print "MAIN FUNCTION 1 START"
     print datetime.datetime.now()


def main_function_2():
     print datetime.datetime.now()
     print "MAIN FUNCTION 2 START"
     print datetime.datetime.now()


def main_function_3():
     print datetime.datetime.now()
     print "MAIN FUNCTION 3 START"
     print datetime.datetime.now()

```

이런 기능이 있다고 하자. 비슷하나, 안의 내용이 달라 , 여러 메서드를 사용해야 되는 경우 

```python
def datetime_decorator(func):
        def decorated():
                print datetime.datetime.now()
                func()
                print datetime.datetime.now()
        return decorated

@datetime_decorator
def main_function_1():
        print "MAIN FUNCTION 1 START"

@datetime_decorator
def main_function_2():
        print "MAIN FUNCTION 2 START"

@datetime_decorator
def main_function_3():
        print "MAIN FUNCTION 3 START"
```

데코레이터를 사용하여 코드의 중복성을 제거할 수 있다.



이걸 해보려고했는데 안되는듯 ㅠㅡㅠ

```python
# 개선 코드 (다른사람 풀이 보고 )
def solution(record):
    user = dict()
    answer = []
    tokens = []
    messages = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}
    
    # user setting O(N)
    for timeline in record: 
        token = timeline.split(" ")
        try: user[token[1]] = token[2]
        except: pass
        tokens.append(token)

    # print message  O(N) 
    for token in tokens:
        action, name = token[0], token[1]
        message = ""
        try: message += user[name]+messages[action]
        except: continue
        answer.append(message)
    return answer
```

