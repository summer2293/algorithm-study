def get_root(idx, arr):
    while arr[idx] != idx:
        idx = arr[idx]
    return idx

def solution(n, computers):
    arr = [i for i in range(n)]
    idx = 0
    for connections in computers:
        # print(arr, 'outer', connections, 'connections', idx, 'idx')
        for connection_id in range(n):
            root = get_root(idx, arr)
            # print(arr, 'inner')
            if connections[connection_id]:
                arr[connection_id] = root
        idx += 1
    # print(arr)
    answer = len(set(arr))
    return answer


answer = solution(4, [[1, 1, 0, 0], [1, 1, 0, 1], [0, 0, 1, 0], [0, 1, 0, 1]])
print('answer is', answer)


# import pytest
# @pytest.mark.parametrize("n, computers, expected", [
#     (3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]],	2),
#     (3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]],	1),
#     (4, [[1, 1, 0, 0], [1, 1, 0, 1], [0, 0, 1, 0], [0, 1, 0, 1]], 2),
#     (4, [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], 4),
#     (4, [[1, 1, 1, 1], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], 1),
# ])

# def test_one(n, computers, expected):
#     assert solution(n, computers) == expected


