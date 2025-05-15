"""
В данной задаче требуется ввести N точек своими координатами (x, y).
Затем требуется определить, существует ли выпуклая оболочка заданного множества точек.
При этом можно использовать: или алгоритм Graham, или алгоритм Jarvis, или метод «разделяй и властвуй»
Нужно найти саму оболочку и вывести точки, входящие в нее. Алгоритм на выбор – Graham, Jarvis.
"""


import math
from logging import exception


class Point(object):
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + ',' + str(self.y) + ")"

    def __eq__(self,other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not (self == other)

    def __iadd__(self, other):
        ...


def is_on_line(points):
    p1 = points[0]
    p2 = points[1]

    for p in points[2:]:
        if (p.y - p1.y) * (p2.x - p1.x) != (p.x - p1.x) * (p2.y - p1.y):
            return False
    return True


def polar_angle(a: Point, b: Point):
    x = b.x - a.x
    y = b.y - a.y
    if x == 0 and y == 0:
        exception("[polar_angle]: same points")

    res = math.atan2(y, x)
    if res < 0:
        res += 2 * math.pi
    return res


def main():
    input_points = list()
    n = int(input("Введите количество точек: "))
    print("Введите координаты точек: ")
    for i in range(n):
        input_points.append(Point(float(input()),float(input())))
    points = list()
    min_point = input_points[0]
    for i in input_points:
        if i.y < min_point.y:
            min_point = i
        if not (i in points):
            points.append(i)

    # Проверка на существование оболочки
    if len(points) < 3:
        print("Оболочку невозможно построить: слишком мало точек")
    elif is_on_line(points):
        print("Оболочку невозможно построить: все точки лежат на одной прямой")
    else:
        # Алгоритм Jarvis
        MCH = list()
        MCH.append(min_point)

        while True:
            min_angle = 99
            min_point = MCH[-1]
            for p in points:
                if MCH[-1] == p:
                    pass
                elif polar_angle(MCH[-1],p) < min_angle:
                    min_angle = polar_angle(MCH[-1],p)
                    min_point = p

            if min_point == MCH[0]:
                break

            MCH.append(min_point)
            points.remove(min_point)

        print(f"-----------------")
        print("Исходные точки:")
        for i in input_points:
            print(i)
        print(f"-----------------")
        print("Оболочка:")
        for i in MCH:
            print(i)


if __name__ == "__main__":
    main()
