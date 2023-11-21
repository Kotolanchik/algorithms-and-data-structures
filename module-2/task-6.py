# алгоритм бойера мура
def majority_element(arr):
    if not arr:
        return -1

    current_element, count = None, 0

    arr.sort()

    for digit in arr:
        if count == 0:
            current_element = digit
            count = 1
        elif current_element == digit:
            count += 1
        else:
            count -= 1

    count = arr.count(current_element)

    if count > len(arr) // 2:
        return current_element
    else:
        return -1


size = int(input())
array = [int(x) for x in input().split()]
result = majority_element(array)
print(result)
