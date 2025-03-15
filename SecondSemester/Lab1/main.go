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
	var N int
	fmt.Print("Введите количество точек: ")
	fmt.Scan(&N)

	points := []point2D{}

	for i := range N {
		var x, y int
		fmt.Printf("Введите %d-ю точку\n", i+1)
		fmt.Scan(&x, &y)
		points = append(points, point2D{x, y})
	}

	grahamScan(points, N)
}

func grahamScan(points []point2D, N int) {
	p_p := make([]int, N) //слайс номеров точек

	for i := range N {
		p_p[i] = i
	}

	minX := 0 // находим самую левую точку и делаем её стартовой
	for i := 1; i < N; i++ {
		if points[p_p[i]].x < points[p_p[minX]].x {
			minX = i
		}
	}
	p_p[0], p_p[minX] = p_p[minX], p_p[0]
	// сортируем по левивезне
	sort.Slice(p_p[1:], func(i, j int) bool {
		return Rotate(points[p_p[0]], points[p_p[i+1]], points[p_p[j+1]]) > 0
	})
	// создаём стэк с двумя начальными точками для оболочки, стоим оболочку выпуклую с помощью этого стэка
	stack := []int{p_p[0], p_p[1]}
	for i := 2; i < N; i++ {
		for len(stack) >= 2 && Rotate(points[stack[len(stack)-2]], points[stack[len(stack)-1]], points[p_p[i]]) <= 0 {
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, p_p[i])
	}
	fmt.Println("Выпуклая оболочка:")
	for _, index := range stack {
		fmt.Printf("(%d, %d)\n", points[index].x, points[index].y)
	}
}

// векторное произведения
// положительное возвращаемое значение соответствует левой стороне, отрицательное — правой (если 0 то коллинеарные но вроде это ничего не ломает)
func Rotate(A, B, C point2D) int {
	return (B.x-A.x)*(C.y-B.y) - (B.y-A.y)*(C.x-B.x)
}
