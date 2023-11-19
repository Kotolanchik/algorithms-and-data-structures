def separate_even_odd(array):
    even_arr = []
    odd_arr = []

    for element in array:
        if element % 2 == 0:
            even_arr.append(element)
        else:
            odd_arr.append(element)

    return even_arr, odd_arr


def move_even_numbers(arr):
    even_idx = 0

    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i], arr[even_idx] = arr[even_idx], arr[i]
            even_idx += 1

    return arr


def merge_sort(array):
    if len(array) <= 1:
        return array

    middle = len(array) // 2
    return merge(merge_sort(array[:middle]), merge_sort(array[middle:]))


def merge(left_arr, right_arr):
    res = []
    l_i, r_i = 0, 0

    while l_i < len(left_arr) and r_i < len(right_arr):
        if left_arr[l_i] < right_arr[r_i]:
            res.append(left_arr[l_i])
            l_i += 1
        else:
            res.append(right_arr[r_i])
            r_i += 1

    while l_i < len(left_arr):
        res.append(left_arr[l_i])
        l_i += 1

    while r_i < len(right_arr):
        res.append(right_arr[r_i])
        r_i += 1

    return res


if __name__ == '__main__':
    # arr = [int(x) for x in '3 2 1 8 11 4 9'.split()]
    s = input()
    arr = [int(x) for x in input().split()]

    even_arr, odd_arr = separate_even_odd(arr)

    #    print(" ".join([str(item) for item in merge_sort(even_arr) + merge_sort(odd_arr)]))
    # print(" ".join([str(item) for item in even_arr + odd_arr]))
    print(" ".join([str(item) for item in move_even_numbers(arr)]))
