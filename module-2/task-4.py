def count_max_repeat_symbol(str):
    if str == "":
        return False

    symbols = {}

    for char in str:
        symbols[char] = symbols.get(char, 0) + 1

    return max(symbols.values())


if __name__ == '__main__':
    print(count_max_repeat_symbol(input()))
