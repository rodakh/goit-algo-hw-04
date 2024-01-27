import timeit
import random


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


sizes = [100, 1000, 10000]
arrays = [[random.randint(0, 1000) for _ in range(size)] for size in sizes]

# Тестування часу виконання для кожного алгоритму та кожного масиву
for size, arr in zip(sizes, arrays):
    print(f"\nРозмір масиву: {size}")

    # Тестування сортування злиттям
    t = timeit.timeit(lambda: merge_sort(arr.copy()), number=1)
    print(f"Час сортування злиттям: {t:.6f} секунд")

    # Тестування сортування вставками
    t = timeit.timeit(lambda: insertion_sort(arr.copy()), number=1)
    print(f"Час сортування вставками: {t:.6f} секунд")

    # Тестування Timsort
    t = timeit.timeit(lambda: sorted(arr), number=1)
    print(f"Час Timsort: {t:.6f} секунд")
