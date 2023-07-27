# # Открываем файл для записи в режиме добавления
# file = open('output.txt', 'a')

# # Добавляем данные в файл
# file.write('\nThis is a new line.')

# # Закрываем файл
# file.close()


# # Чтение данных из файла
# with open('example.txt', 'r') as file:
#     content = file.read()
#     print(content)

# # Запись данных в файл
# with open('output.txt', 'w') as file:
#     file.write('Hello, world!')




import random

def generate_expression():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    expression = f"{num1} {operator} {num2}"
    return expression, eval(expression)

def save_result(expression, user_answer, correct_answer):
    with open("results.txt", "a", encoding= "utf-8") as file:
        file.write(f"Выражение: {expression}, Ваш ответ: {user_answer}, Правильный ответ: {correct_answer}\n")

def main():
    print("Добро пожаловать в игру! Решите следующее выражение:")
    expression, correct_answer = generate_expression()
    print(expression)

    try:
        user_answer = float(input("Введите ваш ответ: "))
    except ValueError:
        print("Ошибка! Пожалуйста, введите число.")
        return

    if user_answer == correct_answer:
        print("Поздравляем! Вы правильно решили выражение.")
    else:
        print("К сожалению, ваш ответ неверный. Попробуйте ещё раз.")

    save_result(expression, user_answer, correct_answer)

if __name__ == "__main__":
    main()
