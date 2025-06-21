# Симуляція кидків кубиків методом Монте-Карло та порівняння з аналітичними даними

import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_simulations):
    """
    Імітує кидки двох кубиків і обчислює частоти сум.
    
    Параметри:
        num_simulations (int): Кількість симуляцій.
    
    Повертає:
        dict: Частоти сум від 2 до 12.
    """
    frequencies = {i: 0 for i in range(2, 13)}
    
    for _ in range(num_simulations):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        frequencies[total] += 1
    
    # Обчислюємо ймовірності
    probabilities = {total: freq / num_simulations for total, freq in frequencies.items()}
    return probabilities

def analytical_probabilities():
    """
    Повертає аналітичні ймовірності для сум двох кубиків у відсотках.
    
    Повертає:
        dict: Теоретичні ймовірності від 2 до 12.
    """
    return {
        2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89,
        7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
    }

def visualize_probabilities(sim_prob, ana_prob, num_simulations):
    """
    Візуалізує ймовірності у вигляді гістограми та зберігає у файл.
    
    Параметри:
        sim_prob (dict): Ймовірності з симуляції.
        ana_prob (dict): Аналітичні ймовірності.
        num_simulations (int): Кількість симуляцій.
    """
    sums = list(range(2, 13))
    sim_values = [sim_prob[s] * 100 for s in sums]  # Переводимо в проценти
    ana_values = [ana_prob[s] for s in sums]
    
    plt.figure(figsize=(10, 6))
    plt.bar(sums, sim_values, alpha=0.7, label="Симуляція", color="blue")
    plt.plot(sums, ana_values, 'ro-', label="Теоретичні", markersize=8)
    plt.xlabel("Сума")
    plt.ylabel("Ймовірність (%)")
    plt.title(f"Ймовірності сум при {num_simulations} кидках (Монте-Карло)")
    plt.legend()
    plt.grid(True)
    plt.savefig("dice_probabilities.png", format="png", bbox_inches="tight")
    plt.close()

def main():
    """Основна функція для симуляції та аналізу."""
    num_simulations = 10000  # Кількість симуляцій
    print(f"Виконується {num_simulations} симуляцій кидків двох кубиків...")
    
    # Симуляція
    simulated_probabilities = simulate_dice_rolls(num_simulations)
    
    # Аналітичні дані
    analytical_probabilities_data = analytical_probabilities()
    
    # Виведення результатів
    print("\nЙмовірності з симуляції (%):")
    for total in range(2, 13):
        print(f"Сума {total}: {simulated_probabilities[total] * 100:.2f}%")
    
    print("\nТеоретичні ймовірності (%):")
    for total in range(2, 13):
        print(f"Сума {total}: {analytical_probabilities_data[total]:.2f}%")
    
    # Візуалізація
    visualize_probabilities(simulated_probabilities, analytical_probabilities_data, num_simulations)
    print(f"Графік збережено у файл: dice_probabilities.png")

if __name__ == "__main__":
    main()