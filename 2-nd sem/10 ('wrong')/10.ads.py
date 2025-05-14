"""
Задача о бросании яиц: Дано 100-этажное здание.
Если яйцо сбросить с высоты N-го этажа (или с большей высоты), оно разобьется.
Если его бросить с любого меньшего этажа, оно не разобьется.
У вас есть два яйца. Найдите N за минимальное количество бросков.
Уметь объяснить решение.
"""

import math


def find_optimal_step(total_floors):
    return math.ceil((math.sqrt(8 * total_floors + 1) - 1) / 2)


def is_egg_broken(floor, critical_floor):
    return floor >= critical_floor


def find_critical_floor(total_floors=100):
    import random
    critical_floor = random.randint(1, total_floors)
    print(f"Пусть критический этаж (N) = {critical_floor}")

    step = find_optimal_step(total_floors)
    current_floor = step
    eggs_left = 2
    throws = 0

    while eggs_left > 0 and current_floor <= total_floors:
        throws += 1
        print(f"Бросок {throws}: кидаем яйцо с {current_floor} этажа...", end=" ")
        if is_egg_broken(current_floor, critical_floor):
            eggs_left -= 1
            print("Разбилось :(")
            lower_floor = current_floor - step + 1 if step > 1 else 1
            print(f"Линейная проверка: этажи {lower_floor}..{current_floor - 1}")
            for floor in range(lower_floor, current_floor):
                throws += 1
                print(f"  Бросок {throws}: кидаем яйцо с {floor} этажа...", end=" ")
                if is_egg_broken(floor, critical_floor):
                    print("Разбилось :(")
                    print(f"Найдено: яйцо разбивается на этаже {floor}")
                    return floor, throws
                else:
                    print("Целое :)")
            print(f"Найдено: яйцо разбивается на этаже {current_floor}")
            return current_floor, throws
        else:
            print("Целое :)")
            step -= 1
            current_floor += step

    if current_floor > total_floors:
        throws += 1
        print(f"Бросок {throws}: кидаем яйцо с {total_floors} этажа...", end=" ")
        if is_egg_broken(total_floors, critical_floor):
            eggs_left -= 1
            print("Разбилось :(")
            lower_floor = total_floors - step + 1
            print(f"Линейная проверка: этажи {lower_floor}..{total_floors - 1}")
            for floor in range(lower_floor, total_floors):
                throws += 1
                print(f"  Бросок {throws}: кидаем яйцо с {floor} этажа...", end=" ")
                if is_egg_broken(floor, critical_floor):
                    print("Разбилось :(")
                    print(f"Найдено: яйцо разбивается на этаже {floor}")
                    return floor, throws
                else:
                    print("Целое :)")
            print(f"Найдено: яйцо разбивается на этаже {total_floors}")
            return total_floors, throws
        else:
            print("Целое :)")
            print("Яйцо не разбилось ни на одном этаже!")
            return -1, throws


critical_floor, throws = find_critical_floor()
print(f"Результат: критический этаж = {critical_floor}, бросков = {throws}")
