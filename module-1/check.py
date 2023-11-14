import random
import time


def func(arr, el):
    for i in arr[::-1]:
        if i == el:
            arr.remove(el)
    return len(arr)


def remove_reverse(arr, el):
    for i in reversed(arr):
        if i == el:
            arr.remove(el)
    return len(arr)


def del_by_index_reverse(arr, el):
    for i in reversed(range(len(arr))):
        if arr[i] == el:
            del arr[i]
    return len(arr)

def del_by_index_pop(arr, el):
    for i in reversed(range(len(arr))):
        if arr[i] == el:
             arr.pop(i)
    return len(arr)

def del_by_index_while(arr, el):
    i = 0
    while i < len(arr):
        if arr[i] == el:
            # Удаляем значение по индексу и не сдвигаем указатель i
            del arr[i]
        else:
            i += 1
    return len(arr)


# Создаем массив из 100000 случайных цифр от 0 до 9 и сделаем по копии для каждой функции
arr1 = [random.randint(0, 9) for num in range(100_000)]
arr2 = arr1[:]
arr3 = arr1[:]
arr4 = arr1[:]
arr5 = arr1[:]

el = 5

start = time.perf_counter()
print(func(arr1, el))
print(time.perf_counter() - start)

start = time.perf_counter()
print(remove_reverse(arr2, el))
print(time.perf_counter() - start)

start = time.perf_counter()
print(del_by_index_reverse(arr3, el))
print(time.perf_counter() - start)

start = time.perf_counter()
print(del_by_index_pop(arr5, el))
print(time.perf_counter() - start)

start = time.perf_counter()
print(del_by_index_while(arr4, el))
print(time.perf_counter() - start)