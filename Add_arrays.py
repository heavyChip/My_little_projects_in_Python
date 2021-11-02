# Simple function which returns sum of two arrays

arr_1 = [
    [1, 2, 3, 4, 5],
    [3, 4, 5, 6, 7],
    [9, 5, 7, 2, 5]
]

arr_2 = [
    [0, 9, 6, 4, 5],
    [3, 4, 5, 8, 7],
    [9, 1, 7, 2, 5]
]


def add_arrays(arr_a, arr_b):
    result = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    for i in range(len(arr_a)):
        for j in range(len(arr_a[i])):
            result[i][j] = arr_a[i][j] + arr_b[i][j]
    return result


print(add_arrays(arr_1, arr_2))
