# Пример словаря
person = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

# Доступ к значению по ключу
print(person['name'])  # Выведет: John

# Добавление новой пары ключ-значение
person['occupation'] = 'Engineer'
# print(person['occupation'])

# Проверка наличия ключа в словаре
if 'age' in person:
    print("Возраст:", person['age'])
else:
    print("Возраст не указан")


# Пример кортежа
coordinates = (10, 20)

# Доступ к элементам кортежа по индексу
print("X:", coordinates[0])  # Выведет: 10
print("Y:", coordinates[1])  # Выведет: 20

# Кортежи неизменяемы, нельзя изменить элементы
# coordinates[0] = 5  # Это вызовет ошибку TypeError
