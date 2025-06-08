package main

import (
	"fmt"
	"sort"
)

type point2D struct {
	x int
	y int
}

func main() {
	points := []point2D{
		{0, 0},
		{1, 1},
		{2, 2},
		{0, 3},
		{0, 1},
		{3, 1},
	}
	grahamScan(points, len(points))
}

func grahamScan(points []point2D, N int) {
	p_p := make([]int, N)
	for i := range N {
		p_p[i] = i
	}

	// Находим индекс самой нижней левой точки
	minIdx := 0
	for i := 1; i < N; i++ {
		if points[p_p[i]].x < points[p_p[minIdx]].x ||
			(points[p_p[i]].x == points[p_p[minIdx]].x && points[p_p[i]].y < points[p_p[minIdx]].y) {
			minIdx = i
		}
	}
	p_p[0], p_p[minIdx] = p_p[minIdx], p_p[0]

	// Сортируем остальные точки по возрастанию полярного угла относительно точки points[p_p[0]]
	sort.Slice(p_p[1:], func(i, j int) bool {
		a := points[p_p[i+1]]
		b := points[p_p[j+1]]
		cross := Rotate(points[p_p[0]], a, b)
		if cross != 0 {
			return cross > 0 // левее — раньше
		}
		// Если коллинеарны, то ближе к точке отсчёта идёт первой
		dx1, dy1 := a.x-points[p_p[0]].x, a.y-points[p_p[0]].y
		dx2, dy2 := b.x-points[p_p[0]].x, b.y-points[p_p[0]].y
		return dx1*dx1+dy1*dy1 < dx2*dx2+dy2*dy2
	})

	// Построение выпуклой оболочки
	stack := []int{p_p[0], p_p[1]}
	for i := 2; i < N; i++ {
		curr := p_p[i]
		for len(stack) >= 2 {
			top := stack[len(stack)-1]
			prev := stack[len(stack)-2]
			if Rotate(points[prev], points[top], points[curr]) > 0 {
				break
			}
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, curr)
	}

	fmt.Println("Выпуклая оболочка:")
	for _, idx := range stack {
		fmt.Printf("(%d, %d)\n", points[idx].x, points[idx].y)
	}
}

// векторное произведения
// положительное возвращаемое значение соответствует левой стороне, отрицательное — правой (если 0 то коллинеарные но вроде это ничего не ломает)
func Rotate(A, B, C point2D) int {
	return (B.x-A.x)*(C.y-B.y) - (B.y-A.y)*(C.x-B.x)
}
