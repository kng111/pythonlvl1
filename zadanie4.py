# Этап 4: Определение структуры узла
class TreeNode:
    def __init__(self, val):
        self.val = val  # Устанавливаем значение узла
        self.left = None  # Устанавливаем левого потомка
        self.right = None  # Устанавливаем правого потомка

# Этап 5: Добавление элементов в дерево
def insert(root, val):
    if root is None:  # Если дерево пустое
        return TreeNode(val)  # Создаем новый узел с заданным значением
    else:
        if root.val < val:  # Если значение нового элемента больше значения текущего узла
            root.right = insert(root.right, val)  # Рекурсивно добавляем элемент в правое поддерево
        else:
            root.left = insert(root.left, val)  # Иначе добавляем элемент в левое поддерево
    return root  # Возвращаем измененное дерево

# Этап 6: Поиск элемента в дереве
def search(root, val):
    if root is None or root.val == val:  # Если дерево пустое или текущий узел содержит искомое значение
        return root is not None  # Возвращаем True, если узел найден

    if root.val < val:  # Если значение искомого элемента больше значения текущего узла
        return search(root.right, val)  # Рекурсивно ищем в правом поддереве
    else:
        return search(root.left, val)  # Иначе ищем в левом поддереве

# Создаем корень дерева
root = None

# Добавляем элементы
elements = [10, 5, 15, 2, 7, 12, 20]
for element in elements:
    root = insert(root, element)  # Добавляем элемент в дерево

# Проверка наличия элементов
print(f"Успешно добавлены элементы: {', '.join(map(str, elements))}")
print(f"Результат поиска элемента 7: {search(root, 7)}")
print(f"Результат поиска элемента 9: {search(root, 9)}")
