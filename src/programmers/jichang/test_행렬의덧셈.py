def sum_of_array(arr1, arr2):
    return [sum_of_rows_in_arrays(arr1[row], arr2[row]) for row in range(len(arr1))]


def sum_of_rows_in_arrays(row1, row2):
    return [row1[row] + row2[row] for row in range(len(row1))]


def test_sum_of_array():
    assert sum_of_array([[1, 2],
                         [2, 3]],
                        [[3, 4],
                         [5, 6]]) == [[4, 6],
                                      [7, 9]]
    assert sum_of_array([[1], [2]],
                        [[3], [4]]) == [[4], [6]]

def test_sum_of_rows_in_arrays():
    assert sum_of_rows_in_arrays([1, 2], [3, 4]) == [4, 6]
    assert sum_of_rows_in_arrays([1], [3]) == [4]
