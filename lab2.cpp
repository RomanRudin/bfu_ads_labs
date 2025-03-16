#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

struct Point {
    double x, y;
    Point(double x = 0, double y = 0) : x(x), y(y) {}
};

// Функция для нахождения точки пересечения двух прямых
bool intersectLines(const Point& p1, const Point& p2, const Point& p3, const Point& p4, Point& result) {
    double A1 = p2.y - p1.y;
    double B1 = p1.x - p2.x;
    double C1 = A1 * p1.x + B1 * p1.y;

    double A2 = p4.y - p3.y;
    double B2 = p3.x - p4.x;
    double C2 = A2 * p3.x + B2 * p3.y;

    double determinant = A1 * B2 - A2 * B1;

    if (determinant == 0) {
        return false; // Прямые параллельны или совпадают
    }

    result.x = (B2 * C1 - B1 * C2) / determinant;
    result.y = (A1 * C2 - A2 * C1) / determinant;
    return true;
}

// Функция для проверки, лежит ли точка на отрезке
bool isPointOnSegment(const Point& p, const Point& a, const Point& b) {
    double cross = (p.x - a.x) * (b.y - a.y) - (p.y - a.y) * (b.x - a.x);
    if (abs(cross) > 1e-12) return false; // Точка не на прямой

    double dot = (p.x - a.x) * (b.x - a.x) + (p.y - a.y) * (b.y - a.y);
    if (dot < 0) return false; // Точка за пределами отрезка

    double len = (b.x - a.x) * (b.x - a.x) + (b.y - a.y) * (b.y - a.y);
    if (dot > len) return false; // Точка за пределами отрезка

    return true;
}

// Функция для нахождения пересечения прямой и отрезка
bool intersectLineSegment(const Point& p1, const Point& p2, const Point& p3, const Point& p4, Point& result) {
    if (!intersectLines(p1, p2, p3, p4, result)) return false;
    return isPointOnSegment(result, p3, p4);
}

// Функция для нахождения пересечения двух отрезков
bool intersectSegments(const Point& p1, const Point& p2, const Point& p3, const Point& p4, Point& result) {
    if (!intersectLines(p1, p2, p3, p4, result)) return false;
    return isPointOnSegment(result, p1, p2) && isPointOnSegment(result, p3, p4);
}

// Функция для нахождения пересечения прямой и окружности
bool intersectLineCircle(const Point& p1, const Point& p2, const Point& center, double radius, std::vector<Point>& result) {
    double A = p2.y - p1.y;
    double B = p1.x - p2.x;
    double C = A * p1.x + B * p1.y;

    double dist = abs(A * center.x + B * center.y + C) / sqrt(A * A + B * B);
    if (dist > radius) return false; // Прямая не пересекает окружность

    double dx = p2.x - p1.x;
    double dy = p2.y - p1.y;
    double dr = sqrt(dx * dx + dy * dy);
    double D = p1.x * p2.y - p2.x * p1.y;

    double discriminant = radius * radius * dr * dr - D * D;
    if (discriminant < 0) return false;

    double x1 = (D * dy + (dy < 0 ? -1 : 1) * dx * sqrt(discriminant)) / (dr * dr);
    double y1 = (-D * dx + abs(dy) * sqrt(discriminant)) / (dr * dr);
    double x2 = (D * dy - (dy < 0 ? -1 : 1) * dx * sqrt(discriminant)) / (dr * dr);
    double y2 = (-D * dx - abs(dy) * sqrt(discriminant)) / (dr * dr);

    result.push_back(Point(x1 + center.x, y1 + center.y));
    result.push_back(Point(x2 + center.x, y2 + center.y));
    return true;
}

// Функция для нахождения пересечения отрезка и окружности
bool intersectSegmentCircle(const Point& p1, const Point& p2, const Point& center, double radius, std::vector<Point>& result) {
    std::vector<Point> intersections;
    if (!intersectLineCircle(p1, p2, center, radius, intersections)) return false;

    for (const auto& p : intersections) {
        if (isPointOnSegment(p, p1, p2)) {
            result.push_back(p);
        }
    }
    return !result.empty();
}

// Функция для нахождения пересечения двух окружностей
bool intersectCircles(const Point& center1, double radius1, const Point& center2, double radius2, std::vector<Point>& result) {
    double d = sqrt((center2.x - center1.x) * (center2.x - center1.x) + (center2.y - center1.y) * (center2.y - center1.y));
    if (d > radius1 + radius2 || d < abs(radius1 - radius2)) return false; // Окружности не пересекаются

    double a = (radius1 * radius1 - radius2 * radius2 + d * d) / (2 * d);
    double h = sqrt(radius1 * radius1 - a * a);

    Point p0(center1.x + a * (center2.x - center1.x) / d, center1.y + a * (center2.y - center1.y) / d);

    result.push_back(Point(p0.x + h * (center2.y - center1.y) / d, p0.y - h * (center2.x - center1.x) / d));
    result.push_back(Point(p0.x - h * (center2.y - center1.y) / d, p0.y + h * (center2.x - center1.x) / d));
    return true;
}
// Функция для проверки, лежит ли точка внутри треугольника
bool isPointInTriangle(const Point& p, const Point& a, const Point& b, const Point& c) {
    double cross1 = (b.x - a.x) * (p.y - a.y) - (b.y - a.y) * (p.x - a.x);
    double cross2 = (c.x - b.x) * (p.y - b.y) - (c.y - b.y) * (p.x - b.x);
    double cross3 = (a.x - c.x) * (p.y - c.y) - (a.y - c.y) * (p.x - c.x);

    bool has_neg = (cross1 < -1e-9) || (cross2 < -1e-9) || (cross3 < -1e-9);
    bool has_pos = (cross1 > 1e-9) || (cross2 > 1e-9) || (cross3 > 1e-9);

    return !(has_neg && has_pos); // Точка внутри, если все cross одного знака (с допуском на погрешность)
}



// Функция для проверки наличия вложенных треугольников
bool hasNestedTriangles(const std::vector<Point>& points, std::vector<std::pair<std::vector<Point>, std::vector<Point>>>& nestedTriangles) {
    size_t n = points.size();
    for (size_t i = 0; i < n; ++i) {
        for (size_t j = i + 1; j < n; ++j) {
            for (size_t k = j + 1; k < n; ++k) {
                Point A = points[i], B = points[j], C = points[k];

                // Список внутренних точек
                std::vector<Point> insidePoints;
                for (size_t l = 0; l < n; ++l) {
                    if (l == i || l == j || l == k) continue;
                    if (isPointInTriangle(points[l], A, B, C)) {
                        insidePoints.push_back(points[l]);
                    }
                }

                // Если есть 3 внутренних точки, формируем вложенный треугольник
                if (insidePoints.size() >= 3) {
                    for (size_t m = 0; m < insidePoints.size(); ++m) {
                        for (size_t n = m + 1; n < insidePoints.size(); ++n) {
                            for (size_t o = n + 1; o < insidePoints.size(); ++o) {
                                nestedTriangles.push_back({ {A, B, C}, {insidePoints[m], insidePoints[n], insidePoints[o]} });
                            }
                        }
                    }
                }
            }
        }
    }
    return !nestedTriangles.empty();
}
// Тестирование функций
void testIntersectLines() {
    Point p1(0, 0), p2(2, 2), p3(0, 2), p4(2, 0);
    Point result;
    if (intersectLines(p1, p2, p3, p4, result)) {
        std::cout << "intersectLines:  The intersection point: (" << result.x << ", " << result.y << ")\n";
    }
    else {
        std::cout << "intersectLines: Straight lines don't intersect\n";
    }
}

void testIsPointOnSegment() {
    Point p(1, 1), a(0, 0), b(2, 2);
    if (isPointOnSegment(p, a, b)) {
        std::cout << "isPointOnSegment: The point lies on the segment\n";
    }
    else {
        std::cout << "isPointOnSegment: The point does not lie on the segment\n";
    }
}

void testIntersectLineSegment() {
    Point p1(0, 0), p2(2, 2), p3(0, 2), p4(2, 0);
    Point result;
    if (intersectLineSegment(p1, p2, p3, p4, result)) {
        std::cout << "intersectLineSegment: The intersection point: (" << result.x << ", " << result.y << ")\n";
    }
    else {
        std::cout << "intersectLineSegment: There is no intersection\n";
    }
}

void testIntersectSegments() {
    Point p1(0, 0), p2(2, 2), p3(0, 2), p4(2, 0);
    Point result;
    if (intersectSegments(p1, p2, p3, p4, result)) {
        std::cout << "intersectSegments: The intersection point: (" << result.x << ", " << result.y << ")\n";
    }
    else {
        std::cout << "intersectSegments: There is no intersection\n";
    }
}

void testIntersectLineCircle() {
    Point p1(0, 0), p2(2, 2), center(1, 1);
    double radius = 1;
    std::vector<Point> result;
    if (intersectLineCircle(p1, p2, center, radius, result)) {
        std::cout << "intersectLineCircle: There is  intersection:\n";
        for (const auto& p : result) {
            std::cout << "(" << p.x << ", " << p.y << ")\n";
        }
    }
    else {
        std::cout << "intersectLineCircle: There is no intersection\n";
    }
}

void testIntersectSegmentCircle() {
    Point p1(0, 0), p2(2, 2), center(1, 1);
    double radius = 1;
    std::vector<Point> result;
    if (intersectSegmentCircle(p1, p2, center, radius, result)) {
        std::cout << "intersectSegmentCircle: There is  intersection:\n";
        for (const auto& p : result) {
            std::cout << "(" << p.x << ", " << p.y << ")\n";
        }
    }
    else {
        std::cout << "intersectSegmentCircle: There is no intersection\n";
    }
}

void testIntersectCircles() {
    Point center1(0, 0), center2(2, 0);
    double radius1 = 1, radius2 = 1;
    std::vector<Point> result;
    if (intersectCircles(center1, radius1, center2, radius2, result)) {
        std::cout << "intersectCircles: There is intersection\n";
        for (const auto& p : result) {
            std::cout << "(" << p.x << ", " << p.y << ")\n";
        }
    }
    else {
        std::cout << "intersectCircles: There is no intersection\n";
    }
}

int main() {
    //std::vector<Point> points = { {0, 0}, {1, 0}, {0.5, 1}, {0.5, 0.5}, {0.25, 0.25} };
    std::vector<Point> points = {
    { 0, 0 },    // Точка A
    { 2, 0 },    // Точка B
    { 1, 2 },    // Точка C
    { 1, 1 },    // Точка D (внутри треугольника ABC)
    { 0.5, 0.5 },// Точка E (внутри треугольника ABC)
    { 1.5, 0.5 } // Точка F (внутри треугольника ABC)
    };
    std::vector<std::pair<std::vector<Point>, std::vector<Point>>> nestedTriangles;

    if (hasNestedTriangles(points, nestedTriangles)) {
        std::cout << "Nested triangles found!" << std::endl;
        for (const auto& pair : nestedTriangles) {
            std::cout << "Outer triangle: ";
            for (const auto& p : pair.first) {
                std::cout << "(" << p.x << ", " << p.y << ") ";
            }
            std::cout << "\nInner triangle: ";
            for (const auto& p : pair.second) {
                std::cout << "(" << p.x << ", " << p.y << ") ";
            }
            std::cout << "\n\n";
        }
    }
    else {
        std::cout << "No nested triangles were found" << std::endl;
    }
    std::cout << "////////////////////////////////////////////////" << std::endl;
    testIntersectLines();
    std::cout << "////////////////////////////////////////////////" << std::endl;
    testIsPointOnSegment();
    std::cout << "////////////////////////////////////////////////" << std::endl;
    testIntersectLineSegment();
    std::cout << "////////////////////////////////////////////////" << std::endl;
    testIntersectSegments();
    std::cout << "////////////////////////////////////////////////" << std::endl;
    testIntersectLineCircle();
    std::cout << "////////////////////////////////////////////////" << std::endl;
    testIntersectSegmentCircle();
    std::cout << "////////////////////////////////////////////////" << std::endl;
    testIntersectCircles();

    return 0;
}