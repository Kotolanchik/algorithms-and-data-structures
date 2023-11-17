import re


def merge_sort_books(books):
    if len(books) <= 1:
        return books

    middle = len(books) // 2
    left_half = merge_sort_books(books[:middle])
    right_half = merge_sort_books(books[middle:])

    return merge_books(left_half, right_half)


def merge_books(left, right):
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        # Сначала сравниваем по году издания
        if left[left_index][2] < right[right_index][2]:
            result.append(left[left_index])
            left_index += 1
        elif left[left_index][2] > right[right_index][2]:
            result.append(right[right_index])
            right_index += 1
        else:
            # Если год издания одинаков, сравниваем по названию книги
            if left[left_index][1] < right[right_index][1]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1

    # Добавляем оставшиеся книги
    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1

    return result


# Ввод данных
n = int(input())

books = []

for book in range(n):
    pattern = re.compile(r'(\d{10}) "(.*?)" (\d{4})')
    matches = re.findall(pattern, input())
    isbn, title, year = matches[0]
    books.append((isbn, title, int(year)))

# Сортировка и вывод результатов
sorted_books = merge_sort_books(books)
for book in sorted_books:
    print(f'{book[0]} "{book[1]}" {book[2]}')
