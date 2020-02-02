# programmers lv2 다리를 지나는 트럭
# https://programmers.co.kr/learn/courses/30/lessons/42583
def solution(bridge_length, max_weight, truck_weights):
    bridge = deque([0]*bridge_length, maxlen=bridge_length)
    bridge_current_weight = 0
    time = 0
    truck_weights.reverse()
    while truck_weights:
        time += 1
        next_truck = bridge.popleft()
        bridge_current_weight -= next_truck
        if bridge_current_weight + truck_weights[-1] > max_weight:
            bridge.append(0)            
        else:
            truck = truck_weights.pop()
            bridge.append(truck)
            bridge_current_weight += truck
    while bridge_current_weight > 0:
        time += 1
        next_truck = bridge.popleft()
        bridge_current_weight -= next_truck
    return time