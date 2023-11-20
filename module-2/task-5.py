def is_anagram(a, b):

    if len(a) != len(b):
        return False

    symbol_a = {}
    symbol_b = {}

    for char in a:
        symbol_a[char] = symbol_a.get(char, 0) + 1

    for char in b:
        symbol_b[char] = symbol_b.get(char, 0) + 1

    return symbol_a == symbol_b


str_a = input().split()
result = is_anagram(str_a[0], str_a[1])

if result:
    print(f"true")
else:
    print(f"false")
