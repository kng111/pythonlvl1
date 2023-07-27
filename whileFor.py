def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def find_primes(start, end):
    primes = []
    for number in range(start, end + 1):
        if is_prime(number):
            primes.append(number)
    return primes

if __name__ == "__main__":
    start_range,end_range  = map(int, input("Через пробел напиши 2 числа, Начало диапазона и конец:").split())


    result = find_primes(start_range, end_range)

    if result:
        print(f"Простые числа в диапазоне от {start_range} до {end_range}:")
        print(result)
    else:
        print(f"В диапазоне от {start_range} до {end_range} нет простых чисел.")
