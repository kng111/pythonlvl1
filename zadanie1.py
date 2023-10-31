# Этап 2
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Этап 3
def generate_primes(start, end):
    primes = []
    for i in range(start, end + 1):
        if is_prime(i):
            primes.append(i)
    return primes

# Этап 1
try:
    start = int(input("Введите начало диапазона: "))
    end = int(input("Введите конец диапазона: "))
    
    if start < 2:
        start = 2  # Простые числа начинаются с 2
except ValueError:
    print("Ошибка: Введите целое число.")
    exit(1)

# Этап 5
if start > end:
    print("Ошибка: Начало диапазона больше конца.")
else:
    # Этап 4
    primes = generate_primes(start, end)
    if primes:
        print(f"Простые числа в диапазоне от {start} до {end}: {', '.join(map(str, primes))}")
    else:
        print(f"В диапазоне от {start} до {end} нет простых чисел.")
