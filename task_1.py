import heapq

def min_cost_to_connect_cables(lengths):
    # Створюємо мін-купу з довжин кабелів
    heapq.heapify(lengths)

    total_cost = 0

    # Об'єднуємо кабелі по два за раз
    while len(lengths) > 1:
        # Дістаємо два найкоротші кабелі
        first = heapq.heappop(lengths)
        second = heapq.heappop(lengths)

        # Витрати на об'єднання
        cost = first + second
        total_cost += cost

        # Додаємо новий кабель назад у купу
        heapq.heappush(lengths, cost)

    return total_cost

# Приклад використання:
cable_lengths = [8, 4, 6, 12]
result = min_cost_to_connect_cables(cable_lengths)
print(result)  # Виведе: 58
# Висновок: Реалізація мінімізує загальні витрати на об'єднання кабелів,
# забезпечуючи ефективне вирішення задачі за допомогою структури даних "купа" та алгоритмів з модуля heapq.
