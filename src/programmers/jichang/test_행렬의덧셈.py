def sum_of_array(arr1, arr2):
    result = []
    for row in range(len(arr1[0])):
        rows = []
        for column in range(len(arr1)):
            rows.append(arr1[row][column] + arr2[row][column])
        result.append(rows)
    return result

    return [[arr1[0][0] + arr2[0][0], arr1[0][1] + arr2[0][1]],
            [arr1[1][0] + arr2[1][0], arr1[1][1] + arr2[1][1]]]


def test_sum_of_array():
    assert sum_of_array([[1, 2],
                         [2, 3]],
                        [[3, 4],
                         [5, 6]]) == [[4, 6],
                                      [7, 9]]
