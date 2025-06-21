# Реалізація фрактала "Дерево Піфагора" з використанням Pillow і збереженням у PNG із рівнем рекурсії в імені файлу

from PIL import Image, ImageDraw
import math

def draw_branch(draw, x1, y1, length, angle, level, max_level, color=(0, 128, 0)):
    """
    Рекурсивно малює гілку фрактала "Дерево Піфагора".
    
    Параметри:
        draw (ImageDraw.Draw): Об'єкт для малювання.
        x1, y1 (float): Початкові координати гілки.
        length (float): Довжина гілки.
        angle (float): Кут нахилу гілки (у градусах).
        level (int): Поточний рівень рекурсії.
        max_level (int): Максимальний рівень рекурсії.
        color (tuple): Колір гілки у форматі RGB.
    """
    if level == 0:
        return
    
    # Обчислюємо кінцеві координати гілки
    x2 = x1 + length * math.cos(math.radians(angle))
    y2 = y1 - length * math.sin(math.radians(angle))  # Y іде вниз у Pillow
    
    # Малюємо гілку
    draw.line([(x1, y1), (x2, y2)], fill=color, width=max(1, level))
    
    # Змінюємо колір для наступного рівня (трохи світліший)
    new_color = tuple(min(255, c + 20 * (max_level - level)) for c in color)
    
    # Рекурсивно малюємо ліву та праву гілки
    new_length = length * (math.sqrt(2) / 2)
    draw_branch(draw, x2, y2, new_length, angle + 45, level - 1, max_level, new_color)
    draw_branch(draw, x2, y2, new_length, angle - 45, level - 1, max_level, new_color)

def main(recursion_level):
    """
    Створює та зберігає фрактал "Дерево Піфагора" у PNG із рівнем рекурсії в імені файлу.
    
    Параметри:
        recursion_level (int): Рівень рекурсії.
    """
    # Налаштування зображення
    width, height = 800, 600
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    
    # Початкові параметри: гілка починається знизу центру
    start_x = width // 2
    start_y = height - 50
    initial_length = 100
    initial_angle = 90  # Вгору
    
    # Малюємо фрактал
    draw_branch(draw, start_x, start_y, initial_length, initial_angle, recursion_level, recursion_level)
    
    # Формуємо ім'я файлу з рівнем рекурсії
    output_file = f"pythagoras_tree_level_{recursion_level}.png"
    
    # Зберігаємо зображення
    image.save(output_file, "PNG")
    print(f"Фрактал збережено у файл: {output_file}")

if __name__ == "__main__":
    # Отримання рівня рекурсії від користувача
    try:
        level = int(input("Введіть рівень рекурсії (рекомендується 1-10): "))
        if level < 0:
            print("Рівень рекурсії не може бути від'ємним. Встановлено 5.")
            level = 5
        elif level > 12:
            print("Занадто великий рівень може бути повільним. Встановлено 10.")
            level = 10
    except ValueError:
        print("Некоректне введення. Встановлено рівень 5.")
        level = 5
    
    main(level)