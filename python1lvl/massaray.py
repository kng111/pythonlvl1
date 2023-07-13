import random
from array import array

# Генерация случайных чисел
random_numbers = [random.randint(1, 10) for _ in range(5)]

# Создание массива из сгенерированных чисел
ar = array('i', random_numbers)

#Строка выполняет операцию сложения первого и последнего элементов массива ar и сохраняет результат в переменной res. res 2 = сумма всего случайного массива
res,res2 = ar[0] + ar[-1],sum(ar)
# Вывод результата
print(f'index1 + index2: {res}\nsum all: {res2}')
