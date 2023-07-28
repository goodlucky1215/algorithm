import collections


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = collections.deque([0] * bridge_length)
    truck_weights = collections.deque(truck_weights)
    total = 0
    while bridge:
        answer += 1
        total -= bridge.popleft()

        if truck_weights:
            if total + truck_weights[0] <= weight:
                total += truck_weights[0]
                bridge.append(truck_weights.popleft())
            else:
                bridge.append(0)

    return answer