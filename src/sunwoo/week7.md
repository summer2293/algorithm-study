## 완주하지 못한 선수

https://programmers.co.kr/learn/courses/30/leassons/42576?language=python3

#####Python

```python
def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    return participant.pop()
```



## 자릿수 더하기

##### Swift

```swift
import Foundation

func solution(_ n: Int) -> Int {
    return String(n).map{ Int(String($0))! }.reduce(0, +)
}
```

##### Python

```python
def solution(n):
    answer = 0
    for s in str(n): answer += int(s)

    return answer
```



## 예산

##### Swift

```swift
import Foundation

func solution(_ d: [Int], _ budget: Int) -> Int {
    return d.sorted().reduce((0, 0)) { arg1, element in
        let (count, amount) = arg1
        guard amount + element <= budget else { return arg1 }
        return (count + 1, amount + element)
    }.0
}
```



##### Python

- Solution1

```python
def solution(d, budget):
    d.sort()
    count = 0

    for price in d:
        budget -= price
        if budget < 0: return count
        else: count += 1

    return count
```

- Solution2 - enumerate

```python

def solution2(d, budget):
    d.sort()
    for index, price in enumerate(d):
        budget -= price
        if budget < 0: return index

    return len(d)
```

## 모의고사

##### Swift

```swift
import Foundation

func solution(_ answers:[Int]) -> [Int] {
    let person1 = [1, 2, 3, 4, 5]
    let person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    let person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    let persons = [person1, person2, person3].map { person -> [Int] in
        let count = answers.count / person.count + (answers.count % person.count > 0 ? 1 : 0)
        let array = [[Int]].init(repeating: person, count: count).reduce([], +)
        return array
    }
     
    let answersCountArray = persons.map { person in
        answers.enumerated().filter { $1 == person[$0] }.count
    } 
    let sortedArray = answersCountArray.enumerated().sorted { $0.element > $1.element }
 
    guard let maxCount = sortedArray.first?.element else { return [] }
    
    let result = sortedArray
        .filter { $0.element == maxCount }
        .map { $0.offset + 1 }
        .sorted(by: <)
    
    return result
}
```



##### Python

- solution1

```python
def solution(answers):
    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    person1_len = len(person1)
    person2_len = len(person2)
    person3_len = len(person3)

    counters = [0, 0, 0]

    for i, answer in enumerate(answers):
        if person1[i % person1_len] == answer: counters[0] += 1
        if person2[i % person2_len] == answer: counters[1] += 1
        if person3[i % person3_len] == answer: counters[2] += 1

    max_count = max(counters)

    result = []
    for i, counter in enumerate(counters):
        if counter == max_count:
            result.append(i + 1)

    return result
```



- solution2

```python
def solution(answers):
    persons = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    scores = [0, 0, 0]

    for i, answer in enumerate(answers):
        for person_index, person in enumerate(persons):
            if person[i % len(person)] == answer:
                scores[person_index] += 1

    max_count = max(scores)
    result = []
    for i, counter in enumerate(scores):
        if counter == max_count:
            result.append(i + 1)

    return result
```



## 실패율

##### Python

```python
def solution(N, stages):
    counter = len(stages)
    rates = []
    
    for i in range(1, N+1):
        if N >= i and counter > 0:
            rates.append(((i,float(stages.count(i) / counter))))
            counter = counter - stages.count(i)
        else:
            rates.append((i, 0))

    sorted_stage_rates = sorted(rates, key=lambda rate: rate[1], reverse=True)
    return list(map(lambda rate: rate[0], sorted_stage_rates))[:N]


```

