def mainDeF():
    def calculate_average(numbers):
        total = sum(numbers)
        average = total / len(numbers)
        return average

    # Генерируем случайный список чисел
    import random
    random_list = [random.randint(1, 100) for _ in range(10)]

    # Выводим список на экран
    print("Случайный список:", random_list)

    # Вызываем функцию для вычисления среднего значения
    avg = calculate_average(random_list)
    print("Среднее значение списка:", avg)


if __name__ == "__main__":
    print('Запуск'),mainDeF()