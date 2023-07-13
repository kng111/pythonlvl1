import random

# Генерируем случайные списки
list1 = [random.randint(1, 10) for _ in range(5)]
list2 = [random.randint(1, 10) for _ in range(8)]
list3 = [random.randint(1, 10) for _ in range(3)]

# Выводим списки
print("Список 1:", list1)
print("Список 2:", list2)
print("Список 3:", list3)
