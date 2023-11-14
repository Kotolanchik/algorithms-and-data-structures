def moving_back_zeros(array, size):
    count_zero = 0
    for i in range(len(array)):
        if array[i] == 0:
            count_zero += 1

    while count_zero:
        for i in range(len(array)):
            if array[i] == 0:
                sub_arr = array[i:]
                for j in range(len(sub_arr) - 1):
                    sub_arr[j], sub_arr[j + 1] = sub_arr[j + 1], sub_arr[j]
                array[i:i + len(sub_arr)] = sub_arr
                break
        count_zero -= 1


if __name__ == '__main__':
    size = int(input())
    array = [int(x) for x in input().split()]
    moving_back_zeros(array, size)
    print(" ".join([str(item) for item in array]))
