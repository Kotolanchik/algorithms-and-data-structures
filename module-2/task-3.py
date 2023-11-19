def recursive_binary_search(arr, left, right, search_element):
    middle_index = (left + right) // 2
    middle = arr[middle_index]

    if left > right:
        return False

    if middle == search_element:
        return True, middle_index
    elif middle < search_element:
        return recursive_binary_search(arr, middle_index + 1, right, search_element)
    else:
        return recursive_binary_search(arr, left, middle_index - 1, search_element)


def while_binary_search(arr, search_element):
    left, right = 0, len(arr) - 1

    if right == 0 or search_element < arr[left] or search_element > arr[right]:
        return False

    while left <= right:
        middle_index = (left + right) // 2
        middle_el = arr[middle_index]

        if middle_el == search_element:
            return True

        if search_element > middle_el:
            left = middle_index + 1
        else:
            right = middle_index - 1

    return False


if __name__ == "__main__":
    size = int(input())
    array = [int(x) for x in input().split()]
    target = int(input())
    if while_binary_search(array, target):
        print("true")
    else:
        print("false")
