import random
import matplotlib.pyplot as plt
import numpy as np
from colorama import Fore

def f(x):
    return x**2

def is_inside(x, y):
    """Перевіряє, чи знаходиться точка (x, y) нижче параболи."""
    return y <= f(x)

def monte_carlo_simulation(a, b, num_experiments):
    """Виконує серію експериментів методом Монте-Карло."""
    average_area = 0
    width = b-a
    height = max(f(a), f(b))

    for _ in range(num_experiments):
        # Генерація випадкових точок
        points = [(random.uniform(a, a+width), random.uniform(0, height)) for _ in range(15000)]
        # Відбір точок, що знаходяться нижче параболи
        inside_points = [point for point in points if is_inside(point[0], point[1])]

        # Розрахунок площі за методом Монте-Карло
        M = len(inside_points)
        N = len(points)
        area = (M / N) * (width * height)

        # Додавання до середньої площі
        average_area += area

    # Обчислення середньої площі
    average_area /= num_experiments
    return average_area


if __name__ == "__main__":

    print("Привіт! Сьогодні розраховуємо інтеграл для квадратичної функції за допомогою метода Монте-Карло")
    print()
    a = int(input("Звідки будемо інтегрувати: "))
    b = int(input("До куди будемо інтегрувати: "))
    print()
    print(Fore.RED + "Почекайте, йде розрахунок..." + Fore.RESET)
    print()

    S = b**3/3 - a**3/3  # Теоретична площа

    # Кількість експериментів
    max_num_experiments = 10000

    # Виконання симуляції
    print(f"Теоретична площа під функцією: {S}")
    print()

    average_area = monte_carlo_simulation(a, b, 1000)
        
    print(f"Середня площа під функцією за {1000} експериментів: {average_area}")
    print("Відхилення від теоретичної площі", abs(S-average_area))
    print()

    # for num_experiments in range(1, 2):

    #     average_area = monte_carlo_simulation(a, b, num_experiments)
        
    #     print(f"Середня площа під функцією за {num_experiments} експериментів: {average_area}")
    #     print("Відхилення від теоретичної площі", abs(S-average_area))
    #     print()
    


    # МАЛЮЄМО ГРАФІК

    # Створення діапазону значень для x
    x = np.linspace(a-0.5, b+0.5, 400)
    y = f(x)

    # Створення графіка
    fig, ax = plt.subplots()

    # Малювання функції
    ax.plot(x, y, 'r', linewidth=2)

    # Заповнення області під кривою
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
    plt.grid()
    plt.show()
