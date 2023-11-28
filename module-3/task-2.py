def product_min_max(tree):
    n = len(tree)

    def compute(index):
        if index >= n:
            return -1

        root_value = tree[index]
        left_index = 2 * index + 1
        right_index = 2 * index + 2

        left_min_value, left_max_value = compute(left_index)
        right_min_value, right_max_value = compute(right_index)

        cur_min = min(root_value, left_min_value, right_min_value)
        cur_max = max(root_value, left_max_value, right_max_value)

        return cur_min, cur_max

    min_v, max_v = compute(0)

    return min_v * max_v


input_str = "10 4 2 6 1 3 5 8 7 9 10"
arr = list(map(int, input_str.split()[1:]))
result = product_min_max(arr)
print(result)
