import math



def polar_angle(p0: tuple[int, int], p1: tuple[int, int]) -> float:
    return math.atan2(p1[1] - p0[1], p1[0] - p0[0])

def cross_product(o: tuple[int, int], a: tuple[int, int], b: tuple[int, int]) -> int:
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def graham_scan(points: list[tuple[int, int]]) -> list[tuple[int, int]]:
    assert len(points) >= 3

    starting_point = min(points, key=lambda p: (p[1], p[0]))
    sorted_points = sorted(points, key=lambda p: (polar_angle(starting_point, p), p[0], p[1]))

    stack = [starting_point, sorted_points[0], sorted_points[1]]
    for point in sorted_points[2:]:
        while len(stack) >= 2 and cross_product(stack[-2], stack[-1], point) <= 0:
            stack.pop()
        stack.append(point)
    return stack



if __name__ == "__main__":
    N = int(input("Please, enter the number of points: "))
    assert N >= 3
    points = []
    for i in range(N):
        x, y = map(float, input(f"Please, enter the coordinates of {i + 1}th point (x y): ").split())
        points.append((x, y))

    convex_hull = graham_scan(points)

    if convex_hull:
        print("Convex hull consists of points: ")
        for point in convex_hull:
            print(point)
    else:
        print("Convex hull does not exist for this set of points.")