import random

def find_min_max(arr):
    min_element = arr[0]  # Предполагаем, что первый элемент - минимальный
    max_element = arr[0]  # Предполагаем, что первый элемент - максимальный

    for num in arr:
        if num < min_element:
            min_element = num
        if num > max_element:
            max_element = num

    return min_element, max_element

# Создаем массив с случайными числами
my_array = [random.randint(1, 100) for _ in range(10)]

min_value, max_value = find_min_max(my_array)
print("Наименьший элемент:", min_value)
print("Наибольший элемент:", max_value)
