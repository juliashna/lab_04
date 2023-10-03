mas = input("Массив для прощётов: ")
povtor = mas.split(' ')
print(povtor)
def count_duplicates(lst):
    counts = {}  # Создаем пустой словарь для подсчета повторений
    for item in lst:
        if item in counts:
            counts[item] += 1  # Увеличиваем значение для существующего элемента
        else:
            counts[item] = 1  # Добавляем новый элемент в словарь с начальным значением 1

    return counts

duplicates = count_duplicates(povtor)
for item, count in duplicates.items():
    if count > 1:
        print(f"Элемент {item} повторяется {count} раз(а).")