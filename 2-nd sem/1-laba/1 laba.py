import math


def cross(o, a, b):
    return (a[0] - o[0])*(b[1] - o[1]) - (a[1] - o[1])*(b[0] - o[0])


def convex_hull(points):
    if len(points) <= 3:
        return points

    start = min(points, key=lambda p: (p[1], p[0]))

    # сортировка по полярному углу
    sorted_points = sorted(points, key=lambda p: (math.atan2(p[1] - start[1], p[0] - start[0]), p))

    hull = []
    for p in sorted_points:
        while len(hull) >= 2 and cross(hull[-2], hull[-1], p) <= 0:
            hull.pop()
        hull.append(p)

    return hull


def input_points():
    points = []
    n = int(input("Введите количество точек: "))
    for i in range(n):
        x, y = map(float, input(f"Введите координаты точки {i+1} (x y): ").split())
        points.append((x, y))
    return points


points = input_points()
hull = convex_hull(points)

if len(hull) < 3:
    print("Выпуклая оболочка не существует (все точки коллинеарны или их меньше 3).")
else:
    print("Выпуклая оболочка состоит из следующих точек:")
    for p in hull:
        print(p)
