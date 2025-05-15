"""
Записать алгоритмы нахождения точек пересечения двух прямых, прямой и отрезка,
двух отрезков, прямой и окружности, отрезка и окружности, двух окружностей.
Данные алгоритмы используются при решении следующей задачи:
Дано N точек координатами (X, Y).
Выяснить, есть ли в этом множестве точек координаты вложенных друг в друга треугольников.
Нужно использовать какие-то идеи, чтобы уменьшить временную сложность алгоритма.
"""

import math
import random
from typing import List, Tuple, Optional
from rtree import index


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return math.isclose(self.x, other.x) and math.isclose(self.y, other.y)

    def __hash__(self):
        return hash((round(self.x, 6), round(self.y, 6)))

    def __repr__(self):
        return f"({self.x:.2f}, {self.y:.2f})"


def distance(p1: Point, p2: Point) -> float:
    return math.hypot(p2.x - p1.x, p2.y - p1.y)


def is_collinear(p1: Point, p2: Point, p3: Point) -> bool:
    area = (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)
    return math.isclose(area, 0, abs_tol=1e-9)


class Triangle:
    def __init__(self, p1: Point, p2: Point, p3: Point):
        self.points = (p1, p2, p3)
        self.area = self._compute_area()
        self.bbox = self._compute_bbox()

    def _compute_area(self) -> float:
        a = distance(self.points[0], self.points[1])
        b = distance(self.points[1], self.points[2])
        c = distance(self.points[2], self.points[0])
        s = (a + b + c) / 2
        return math.sqrt(max(0, s * (s - a) * (s - b) * (s - c)))

    def _compute_bbox(self) -> Tuple[float, float, float, float]:
        xs = [p.x for p in self.points]
        ys = [p.y for p in self.points]
        return (min(xs), min(ys), max(xs), max(ys))

    def contains_point(self, p: Point) -> bool:
        def sign(a: Point, b: Point, c: Point) -> float:
            return (a.x - c.x) * (b.y - c.y) - (b.x - c.x) * (a.y - c.y)

        d1 = sign(p, self.points[0], self.points[1])
        d2 = sign(p, self.points[1], self.points[2])
        d3 = sign(p, self.points[2], self.points[0])

        has_neg = (d1 < -1e-9) or (d2 < -1e-9) or (d3 < -1e-9)
        has_pos = (d1 > 1e-9) or (d2 > 1e-9) or (d3 > 1e-9)
        return not (has_neg and has_pos)

    def contains_triangle(self, other: 'Triangle') -> bool:
        if not (self.bbox[0] <= other.bbox[0] and
                self.bbox[1] <= other.bbox[1] and
                self.bbox[2] >= other.bbox[2] and
                self.bbox[3] >= other.bbox[3]):
            return False

        # Затем точная проверка всех точек
        return all(self.contains_point(p) for p in other.points)

    def __repr__(self):
        return f"Triangle{self.points}: area={self.area:.2f}"


def generate_triangles(points: List[Point]) -> List[Triangle]:
    triangles = []
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                p1, p2, p3 = points[i], points[j], points[k]
                if not is_collinear(p1, p2, p3):
                    triangles.append(Triangle(p1, p2, p3))
    return triangles


def build_spatial_index(triangles: List[Triangle]) -> index.Index:
    idx = index.Index()
    for i, triangle in enumerate(triangles):
        idx.insert(i, triangle.bbox)
    return idx


def find_nested_triangles(triangles: List[Triangle]) -> Optional[Tuple[Triangle, Triangle]]:
    triangles.sort(key=lambda t: -t.area)
    spatial_index = build_spatial_index(triangles)

    for i, outer_tri in enumerate(triangles):
        candidates = list(spatial_index.intersection(outer_tri.bbox))

        for j in candidates:
            if j <= i:
                continue

            inner_tri = triangles[j]
            if outer_tri.contains_triangle(inner_tri):
                return outer_tri, inner_tri

    return None


def main():
    random.seed(42)
    n_points = 50
    points = [Point(random.uniform(-10, 10), random.uniform(-10, 10))
              for _ in range(n_points)]

    print(f"Сгенерировано {len(points)} точек")
    triangles = generate_triangles(points)
    print(f"Сгенерировано {len(triangles)} треугольников")
    result = find_nested_triangles(triangles)
    if result:
        outer, inner = result
        print("\nНайдены вложенные треугольники:")
        print(f"Внешний треугольник (площадь {outer.area:.2f}): {outer.points}")
        print(f"Внутренний треугольник (площадь {inner.area:.2f}): {inner.points}")

        # Визуализация
        try:
            import matplotlib.pyplot as plt
            plt.figure(figsize=(8, 6))
            plt.scatter([p.x for p in points], [p.y for p in points], c='blue', alpha=0.5)
            outer_x = [p.x for p in outer.points] + [outer.points[0].x]
            outer_y = [p.y for p in outer.points] + [outer.points[0].y]
            plt.plot(outer_x, outer_y, 'r-', linewidth=2, label='Внешний треугольник')
            inner_x = [p.x for p in inner.points] + [inner.points[0].x]
            inner_y = [p.y for p in inner.points] + [inner.points[0].y]
            plt.plot(inner_x, inner_y, 'g-', linewidth=2, label='Внутренний треугольник')
            plt.legend()
            plt.title("Вложенные треугольники")
            plt.grid(True)
            plt.show()
        except ImportError:
            print("Для визуализации установите matplotlib: pip install matplotlib")
    else:
        print("\nВложенные треугольники не найдены.")


if __name__ == "__main__":
    main()
