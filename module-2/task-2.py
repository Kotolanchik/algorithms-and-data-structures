def remove_repeat_symbol(str):
    stack = []

    for char in str:
        if not stack or char != stack[-1]:
            stack.append(char)
        else:
            stack.pop()

    return ''.join(stack)


s = input()
result = remove_repeat_symbol(s)
print(result)
