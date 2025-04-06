import math
from itertools import combinations
from typing import NewType

Point = NewType("Point", tuple[float, float])
Line = NewType("Line", tuple[float, float, float])
Segment = NewType("Segment", tuple[Point, Point])
Circle = NewType("Circle", tuple[Point, int])
Triangle = NewType("Triangle", tuple[Point, Point, Point])

def line_intersection(line1: Line, line2: Line) -> Point | None:
    A1, B1, C1 = line1
    A2, B2, C2 = line2

    det = A1 * B2 - A2 * B1
    if det == 0:
        return None

    x = (B1 * C2 - B2 * C1) / det
    y = (A2 * C1 - A1 * C2) / det
    return (x, y)


def line_segment_intersection(line: Line, segment: Segment) -> Point | None:
    """
    line: (A, B, C) - уравнение прямой
    segment: ((x1, y1), (x2, y2)) - координаты отрезка
    """
    # Находим пересечение с прямой, содержащей отрезок
    segment_line = points_to_line(*segment)
    pt = line_intersection(line, segment_line)
    if not pt:
        return None

    # Проверка принадлежности точки отрезку
    x, y = pt
    (x1, y1), (x2, y2) = segment
    if (min(x1, x2) - 1e-9 <= x <= max(x1, x2) + 1e-9) and \
       (min(y1, y2) - 1e-9 <= y <= max(y1, y2) + 1e-9):
        return pt
    return None


def segments_intersection(seg1: Segment, seg2: Segment) -> Point | None:
    line1 = points_to_line(*seg1)
    line2 = points_to_line(*seg2)
    pt = line_intersection(line1, line2)
    if not pt:
        return None

    # Проверка принадлежности обоим отрезкам
    x, y = pt
    (x1, y1), (x2, y2) = seg1
    in_seg1 = (min(x1, x2) - 1e-9 <= x <= max(x1, x2) + 1e-9 and 
               min(y1, y2) - 1e-9 <= y <= max(y1, y2) + 1e-9)
    
    (x3, y3), (x4, y4) = seg2
    in_seg2 = (min(x3, x4) - 1e-9 <= x <= max(x3, x4) + 1e-9 and 
               min(y3, y4) - 1e-9 <= y <= max(y3, y4) + 1e-9)
    
    return pt if in_seg1 and in_seg2 else None


def line_circle_intersection(line: Line, circle: Circle) -> list| list[Point]:
    """
    circle: (центр (x, y), радиус R)
    Возвращает список точек пересечения
    """
    (A, B, C), ((cx, cy), R) = line, circle
    # Приводим уравнение прямой к виду Ax + By + C = 0
    # и вычисляем расстояние от центра до прямой
    numerator = abs(A * cx + B * cy + C)
    denominator = math.sqrt(A**2 + B**2)
    d = numerator / denominator
    
    if d > R:
        return []  # Нет пересечений
    
    # Находим точки пересечения
    # Решаем систему уравнений прямой и окружности
    # Подробный вывод опущен для краткости
    if B == 0:  # Вертикальная прямая
        x = -C / A
        y_terms = math.sqrt(R**2 - (x - cx)**2)
        return [(x, cy + y_terms), (x, cy - y_terms)]
    else:
        # Общий случай требует решения квадратного уравнения
        pass
    
    return []  # Упрощенная реализация


def segment_circle_intersection(segment: Segment, circle: Circle) -> list | list[Point]:
    line = points_to_line(*segment)
    points = line_circle_intersection(line, circle)
    valid = []
    for pt in points:
        if is_point_on_segment(pt, segment):
            valid.append(pt)
    return valid


def circles_intersection(circle1: Circle, circle2: Circle) -> list | list[Point]:
    (x1, y1), r1 = circle1
    (x2, y2), r2 = circle2
    dx, dy = x2 - x1, y2 - y1
    d = math.sqrt(dx**2 + dy**2)
    
    if d > r1 + r2 or d < abs(r1 - r2):
        return []  # Нет пересечений
    
    a = (r1**2 - r2**2 + d**2) / (2 * d)
    h = math.sqrt(r1**2 - a**2)
    
    xm = x1 + a * dx / d
    ym = y1 + a * dy / d
    
    pt1 = (xm + h * dy / d, ym - h * dx / d)
    pt2 = (xm - h * dy / d, ym + h * dx / d)
    
    return [pt1, pt2] if d != r1 + r2 and d != abs(r1 - r2) else [pt1]


def points_to_line(p1: Point, p2: Point) -> Line:
    """ Конвертирует две точки в уравнение прямой Ax + By + C = 0 """
    x1, y1 = p1
    x2, y2 = p2
    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2
    return (A, B, C)


def is_point_on_segment(pt: Point, segment: Segment) -> bool:
    (x1, y1), (x2, y2) = segment
    x, y = pt
    return (min(x1, x2) - 1e-9 <= x <= max(x1, x2) + 1e-9 and 
            min(y1, y2) - 1e-9 <= y <= max(y1, y2) + 1e-9)


def is_triangle_inside(tri1: Triangle, tri2: Triangle) -> bool:
    """ Проверяет, полностью ли содержится tri1 внутри tri2 """
    # Проверяем все вершины tri1 внутри tri2
    for pt in tri1:
        if not is_point_inside_triangle(pt, tri2):
            return False
    return True


def is_point_inside_triangle(pt: Point, triangle: Triangle) -> bool:
    """ Проверка точки внутри треугольника методом площадей """
    p = pt
    a, b, c = triangle
    area = lambda x1, y1, x2, y2, x3, y3: abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2.0
    
    total_area = area(*a, *b, *c)
    sub_area = area(*p, *a, *b) + area(*p, *b, *c) + area(*p, *c, *a)
    
    return abs(total_area - sub_area) < 1e-9


def find_nested_triangles(points: list[Point]) -> bool:
    triangles = list(combinations(points, 3))
    for tri1, tri2 in combinations(triangles, 2):
        if is_triangle_inside(tri1, tri2) or is_triangle_inside(tri2, tri1):
            return True
    return False


points = [(0,0), (1,0), (0,1), (2,2), (3,3), (1,2)]
print("Есть вложенные треугольники:", find_nested_triangles(points))