# Программа для определения оценки по баллам



# Сноска по ошибке
error = """
Использование try и except ValueError в данном случае поможет обработать ошибку, которая может возникнуть при попытке преобразовать введенное пользователем значение в целое число.

Если пользователь введет что-то, что нельзя преобразовать в целое число (например, буквы или символы), то функция int(input("Введите количество баллов: ")) вызовет ошибку ValueError, потому что не сможет выполнить преобразование. Чтобы избежать сбоя программы из-за этой ошибки, мы используем try и except блоки.

Когда мы помещаем код, который может вызвать ошибку, внутрь блока try, программа пытается выполнить этот код. Если ошибка происходит, программа переходит в блок except, где мы можем обработать ошибку или выдать сообщение об ошибке пользователю.

В данном случае, если возникает ошибка ValueError, программа перехватывает ее и выводит сообщение "Ошибка! Введите число от 0 до 100.", вместо того чтобы завершиться аварийно. Это позволяет сделать программу более устойчивой к некорректному вводу пользователя.
"""

# Для визуального эффекта возьмём time
import time
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Ввод баллов от пользователя
try:
    score = int(input("Введите количество баллов: "))
    if score < 0 or score > 100:
        print("Некорректное количество баллов! Введите число от 0 до 100.")
        
        
    else:
        # grade = get_grade(score)
        print(f"Ваша оценка: {get_grade(score)}")
except ValueError:
    print("Ошибка! Введите число от 0 до 100."),time.sleep(3),print(error)

