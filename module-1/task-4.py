def merge_sort(array):
    if len(array) <= 1:
        return array

    middle = len(array) // 2
    return merge(merge_sort(array[:middle]), merge_sort(array[middle:]))


def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]: # чтобы сортировка была восходящей - изменить знак 
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1

    print(f"Слияние: {left} и {right} -> {result}")
    return result


# arr = [38, 27, 43, 27, 43, 3, 9, 82, 10, -43, 34]
size = int(input())
arr = [int(x) for x in input().split()]
print(f"Сортируем массив: {arr}")
sorted_arr = merge_sort(arr)
print(" ".join([str(item) for item in sorted_arr]))

# print(f"Отсортированный массив: {sorted_arr}")
