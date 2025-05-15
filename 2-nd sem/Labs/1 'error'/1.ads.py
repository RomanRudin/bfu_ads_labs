"""
В данной задаче требуется ввести N точек своими координатами (x, y).
Затем требуется определить, существует ли выпуклая оболочка заданного множества точек.
При этом можно использовать: или алгоритм Graham, или алгоритм Jarvis, или метод «разделяй и властвуй»
Нужно найти саму оболочку и вывести точки, входящие в нее. Алгоритм на выбор – Graham, Jarvis.
"""


def read_points():
    n = int(input("Введите количество точек: "))
    points = []
    for i in range(n):
        x, y = map(float, input(f"Введите координаты точки {i + 1} (x y): ").split())
        points.append((x, y))
    return points


def cross_product(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def convex_hull_jarvis(points):
    n = len(points)
    if n < 3:
        return None

    hull = []

    # Шаг 1: Находим самую левую точку (start)
    start_point = min(points, key=lambda p: (p[0], p[1]))
    current_point = start_point
    hull.append(current_point)

    while True:
        next_point = points[0]
        if next_point == current_point:
            next_point = points[1]

        # Шаг 2: Ищем правую точку
        for candidate in points:
            if candidate == current_point:
                continue
            cross = cross_product(current_point, next_point, candidate)
            if cross > 0:
                next_point = candidate
            elif cross == 0:
                dist_next = (next_point[0] - current_point[0]) ** 2 + (next_point[1] - current_point[1]) ** 2
                dist_cand = (candidate[0] - current_point[0]) ** 2 + (candidate[1] - current_point[1]) ** 2
                if dist_cand > dist_next:
                    next_point = candidate

        # Шаг 3: Переходим к следующей точке
        current_point = next_point
        if current_point == start_point:
            break

        hull.append(current_point)

    return hull


def main():
    points = read_points()
    hull = convex_hull_jarvis(points)

    if hull is None:
        print("Выпуклая оболочка не существует (нужно минимум 3 точки)")
    else:
        print("\nВыпуклая оболочка (точки в порядке обхода по часовой стрелке):")
        for i, point in enumerate(hull, 1):
            print(f"{i}. ({point[0]}, {point[1]})")
        print(f"{len(hull) + 1}. ({hull[0][0]}, {hull[0][1]}) <- Замыкание")


if __name__ == "__main__":
    main()
