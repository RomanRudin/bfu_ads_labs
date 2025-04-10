import math
from itertools import combinations
from typing import NewType, Optional

Point = NewType("Point", tuple[float, float])
Line = NewType("Line", tuple[float, float, float])
Segment = NewType("Segment", tuple[Point, Point])
Circle = NewType("Circle", tuple[Point, int])
Triangle = NewType("Triangle", tuple[Point, Point, Point])

UNCERTAINTY = 1e-9


def points_to_line(p1: Point, p2: Point) -> Line:
    x1, y1 = p1
    x2, y2 = p2
    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2
    return (A, B, C)



def line_intersection(line1: Line, line2: Line) -> Optional[Point]:
    A1, B1, C1 = line1
    A2, B2, C2 = line2

    det = A1 * B2 - A2 * B1
    if det == 0:
        return None

    x = (B1 * C2 - B2 * C1) / det
    y = (A2 * C1 - A1 * C2) / det
    return (x, y)



def line_segment_intersection(line: Line, segment: Segment) -> Optional[Point]:
    segment_line = points_to_line(*segment)
    point = line_intersection(line, segment_line)
    if not point:
        return None

    x, y = point
    (x1, y1), (x2, y2) = segment
    if (min(x1, x2) - UNCERTAINTY <= x <= max(x1, x2) + UNCERTAINTY) and \
       (min(y1, y2) - UNCERTAINTY <= y <= max(y1, y2) + UNCERTAINTY):
        return point
    return None



def segments_intersection(seg1: Segment, seg2: Segment) -> Optional[Point]:
    line1 = points_to_line(*seg1)
    line2 = points_to_line(*seg2)
    pt = line_intersection(line1, line2)
    if not pt:
        return None

    x, y = pt
    (x1, y1), (x2, y2) = seg1
    in_seg1 = (min(x1, x2) - UNCERTAINTY <= x <= max(x1, x2) + UNCERTAINTY and 
               min(y1, y2) - UNCERTAINTY <= y <= max(y1, y2) + UNCERTAINTY)
    
    (x1, y1), (x2, y2) = seg2
    in_seg2 = (min(x1, x2) - UNCERTAINTY <= x <= max(x1, x2) + UNCERTAINTY and 
               min(y1, y2) - UNCERTAINTY <= y <= max(y1, y2) + UNCERTAINTY)
    
    return pt if (in_seg1 and in_seg2) else None



def line_circle_intersection(line: Line, circle: Circle) -> list| list[Point]:
    (A, B, C), ((cx, cy), R) = line, circle
    numerator = abs(A * cx + B * cy + C)
    denominator = math.sqrt(A**2 + B**2)
    d = numerator / denominator
    
    if d > R:
        return [] # No intersections
    
    if B == 0:
        x = -C / A
        y_terms = math.sqrt(R**2 - (x - cx)**2)
        return [(x, cy + y_terms), (x, cy - y_terms)]
    else:
        pass # TODO
    # TODO
    return []  



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



def is_point_on_segment(pt: Point, segment: Segment) -> bool:
    (x1, y1), (x2, y2) = segment
    x, y = pt
    return (min(x1, x2) - UNCERTAINTY <= x <= max(x1, x2) + UNCERTAINTY and 
            min(y1, y2) - UNCERTAINTY <= y <= max(y1, y2) + UNCERTAINTY)



def distance(pt1: Point, pt2: Point) -> float:
    x1, y1 = pt1
    x2, y2 = pt2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def triangle_exists(tri: Triangle) -> bool:
    a, b, c = tri
    area = lambda x1, y1, x2, y2, x3, y3: abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2.0
    total_area = area(*a, *b, *c)
    return total_area > 0



def is_triangle_inside(tri1: Triangle, tri2: Triangle) -> bool:
    for pt in tri1:
        if not is_point_inside_triangle(pt, tri2):
            return False
    return True



def is_point_inside_triangle(pt: Point, triangle: Triangle) -> bool:
    p = pt
    a, b, c = triangle
    area = lambda x1, y1, x2, y2, x3, y3: abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2.0
    
    total_area = area(*a, *b, *c)
    sub_area = area(*p, *a, *b) + area(*p, *b, *c) + area(*p, *c, *a)
    
    return abs(total_area - sub_area) < UNCERTAINTY



def find_nested_triangles(points: list[Point]) -> bool:
    triangles = list(combinations(points, 3))
    for tri1, tri2 in combinations(triangles, 2):
        if not triangle_exists(tri1) or not triangle_exists(tri2):
            continue
        if is_triangle_inside(tri1, tri2) or is_triangle_inside(tri2, tri1):
            print("First triangle:", tri1)
            print("Second triangle:", tri2)
            return True
    return False



if __name__ == "__main__":
    points = [(0,0), (2,2), (1,1), (4,0), (5,1)]
    print("Are triangles nested:", find_nested_triangles(points))
    points = [(0,0), (2,2), (4,0), (5,1)]
    print("Are triangles nested:", find_nested_triangles(points))