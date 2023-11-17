def pop_first_even(array):
    stack = []

    for el in array:
        if el % 2 == 0:
            stack.append(el)

    if not stack:
        return -1

    return stack[-1]


if __name__ == '__main__':
    size = int(input())

    array = [int(x) for x in input().split()]

    print(pop_first_even(array))
