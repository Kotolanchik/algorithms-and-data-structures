def insertion_sort(array):
    for i in range(1, len(array)):
        current_key = array[i]
        j = i - 1

        while j >= 0 and array[j] > current_key:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = current_key


if __name__ == '__main__':
    size = int(input())
    array = [int(x) for x in input().split()]
    insertion_sort(array)
    print(" ".join([str(item) for item in array]))
