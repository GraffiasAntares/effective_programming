import time
import sys
import random



# Создание списка
# Неэффективный способ
start_time = time.time()
inefficient_list = []
for i in range(1, 1001):
    inefficient_list.append(i)
end_time = time.time()
print(f"Неэффективное время: {end_time - start_time}")
print(f"Неэффективное использование памяти: {sys.getsizeof(inefficient_list)} bytes")

# Эффективный способ
start_time = time.time()
efficient_list = list(range(1, 1001))
end_time = time.time()
print(f"Эффективное время: {end_time - start_time}")
print(f"Эффективное использование памяти: {sys.getsizeof(efficient_list)} bytes")
print("\n")

# Сортировка списка
# Неэффективный способ
inefficient_list = [random.randint(1, 1000) for _ in range(1000)]
start_time = time.time()
inefficient_sorted_list = sorted(inefficient_list)
end_time = time.time()
print(f"Неэффективная сортировка время: {end_time - start_time}")
print(f"Неэффективная сортировка использование памяти: {sys.getsizeof(inefficient_sorted_list)} bytes")

# Эффективный способ
efficient_list = [random.randint(1, 1000) for _ in range(1000)]
start_time = time.time()
efficient_list.sort()
end_time = time.time()
print(f"Эффективная сортировка время: {end_time - start_time}")
print(f"Эффективная сортировка использование памяти: {sys.getsizeof(efficient_list)} bytes")
print("\n")


# Сортировка списка (алгоритм)
# Неэффективный
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


# Создаем большой список
inefficient_list = list(range(10000))

# Измеряем время выполнения и размер занимаемой памяти
start_time = time.time()
bubble_sort(inefficient_list)
end_time = time.time()

print(f"Время выполнения алгоритма неэффективной сортировки: {end_time - start_time} секунд")
print(f"Размер занимаемой памяти: {sys.getsizeof(inefficient_list)} байт")


# Эффективный
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# Создаем большой список
efficient_list = list(range(10000))

# Измеряем время выполнения и размер занимаемой памяти
start_time = time.time()
efficient_list = quick_sort(efficient_list)
end_time = time.time()

print(f"Время выполнения алгоритма эффективной сортировки: {end_time - start_time} секунд")
print(f"Размер занимаемой памяти: {sys.getsizeof(efficient_list)} байт")
