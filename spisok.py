import random

def mainS():
    # Создаем список чисел
    numbers = [random.randint(1, 100) for _ in range(10)]

    # Выводим список на экран
    print("Список чисел:", numbers)

    # Индексирование списка
    first_number = numbers[0]
    second_number = numbers[1]
    print("Первое число:", first_number)
    print("Второе число:", second_number)

    # Изменение элемента списка
    numbers[2] = 10
    print("Измененный список:", numbers)

    # Добавление элемента в конец списка
    numbers.append(6)
    print("Список после добавления элемента:", numbers)

    # Удаление элемента из списка
    numbers.remove(4)
    print("Список после удаления элемента:", numbers)

    # Срезы списка
    sublist = numbers[1:4]
    print("Срез списка:", sublist)

    # Длина списка
    list_length = len(numbers)
    print("Длина списка:", list_length)

if __name__ == "__main__":
    print('Запуск')
    mainS()