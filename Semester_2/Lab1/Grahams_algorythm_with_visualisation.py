import matplotlib.pyplot as plt
from matplotlib.patches import PathPatch
from matplotlib.path import Path
from typing import NewType
import math

Point = NewType("Point", tuple[float, float])


def polar_angle(p0: Point, p1: Point) -> float:
    return math.atan2(p1[1] - p0[1], p1[0] - p0[0])

def cross_product(o: Point, a: Point, b: Point) -> float:
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def graham_scan(points: list[Point]) -> list[Point]:
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
    # N = int(input("Please, enter the number of points: "))
    # assert N >= 3
    points = []
    # for i in range(N):
        # x, y = map(float, input(f"Please, enter the coordinates of {i + 1}th point (x y): ").split())
        # points.append((x, y))


    with open("Semester_2/Labs/Lab1/points.txt", 'r', encoding='utf-8') as file:
        # N = int(file.readline().strip())
        for line in file.read().splitlines():
            points.append(tuple(map(float, line.strip().split())))
        assert len(points) >= 3

    convex_hull = graham_scan(points)

    fig, plot = plt.subplots(1, 1)
    plot.scatter([point[0] for point in points], [point[1] for point in points], color="blue")
    
    if convex_hull:
        print("Convex hull consists of points: ")
        for point in convex_hull:
            print(point)
        path = Path(convex_hull)
        convex_hull_patch = PathPatch(path, color="green", alpha=0.2)
        plot.add_patch(convex_hull_patch)
    else:
        print("Convex hull does not exist for this set of points.")

    plt.show()