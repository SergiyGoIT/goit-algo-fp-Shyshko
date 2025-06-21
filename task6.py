# Оптимізація вибору їжі з жадібним алгоритмом та динамічним програмуванням

# Дані про їжу
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(budget):
    """
    Жадібний алгоритм для максимізації калорійності в межах бюджету.
    
    Параметри:
        budget (int): Доступний бюджет.
    
    Повертає:
        tuple: Список обраних страв і загальну калорійність.
    """
    # Обчислюємо співвідношення калорій до вартості
    items_with_ratio = []
    for item, data in items.items():
        ratio = data["calories"] / data["cost"]
        items_with_ratio.append((item, ratio, data["cost"], data["calories"]))
    
    # Сортуємо за спаданням співвідношення
    items_with_ratio.sort(key=lambda x: x[1], reverse=True)
    
    selected_items = []
    total_calories = 0
    remaining_budget = budget
    
    # Обираємо страви
    for item, _, cost, calories in items_with_ratio:
        if remaining_budget >= cost:
            selected_items.append(item)
            total_calories += calories
            remaining_budget -= cost
    
    return selected_items, total_calories

def dynamic_programming(budget):
    """
    Динамічне програмування для максимізації калорійності в межах бюджету.
    
    Параметри:
        budget (int): Доступний бюджет.
    
    Повертає:
        tuple: Список обраних страв і загальну калорійність.
    """
    n = len(items)
    # Ініціалізуємо таблицю DP: dp[i][j] — максимальна калорійність для i страв і бюджету j
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    
    # Ініціалізуємо таблицю для відновлення обраних страв
    keep = [[False for _ in range(budget + 1)] for _ in range(n + 1)]
    
    # Перебираємо страви та бюджети
    item_list = list(items.items())
    for i in range(1, n + 1):
        item_name, data = item_list[i - 1]
        cost, calories = data["cost"], data["calories"]
        for w in range(budget + 1):
            if cost <= w:
                # Обираємо максимум: без поточної страви або з поточною
                without_current = dp[i - 1][w]
                with_current = dp[i - 1][w - cost] + calories
                if with_current > without_current:
                    dp[i][w] = with_current
                    keep[i][w] = True
                else:
                    dp[i][w] = without_current
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Відновлюємо обрані страви
    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if keep[i][w]:
            item_name, data = item_list[i - 1]
            selected_items.append(item_name)
            w -= data["cost"]
    
    return selected_items[::-1], dp[n][budget]

def main():
    """Приклад використання обох алгоритмів."""
    budget = 100
    print(f"Бюджет: {budget} одиниць")
    
    # Жадібний алгоритм
    greedy_items, greedy_calories = greedy_algorithm(budget)
    print(f"Жадібний алгоритм: Страви {greedy_items}, Калорійність: {greedy_calories}")
    
    # Динамічне програмування
    dp_items, dp_calories = dynamic_programming(budget)
    print(f"Динамічне програмування: Страви {dp_items}, Калорійність: {dp_calories}")

if __name__ == "__main__":
    main()