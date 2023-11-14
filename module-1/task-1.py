def count_and_remove_elements(array, element):
    count = 0
    i = 0
    while i < len(array):
        if array[i] == element:
            array.pop(i)
        else:
            i += 1
    count = len(array)
    return count


if __name__ == '__main__':
    size = int(input())
    array = list(map(int, input().split()))
    target = int(input())

    count = count_and_remove_elements(array, target)

    print(count)
