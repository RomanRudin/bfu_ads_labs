package main

import (
	"fmt"
)

func find_egg_break_floor(max_floor int, eggs int) (int, int) {
	// Вычисляем начальный шаг k по формуле суммы арифметической прогрессии
	k := 0
	for k*(k+1)/2 < max_floor {
		k += 1
	}

	current_floor := k
	step := k - 1
	eggs_remaining := eggs
	attempts := 0

	for eggs_remaining > 0 && current_floor <= max_floor {
		attempts += 1
		fmt.Printf("Бросаем яйцо с %v-го этажа (попытка %v)\n", current_floor, attempts)
		fmt.Println("Разбило? (y/n)")

		var broke string
		fmt.Scanln(&broke)

		if broke == "y" {
			eggs_remaining -= 1
			if eggs_remaining == 0 {
				fmt.Printf("Критический этаж: %v\n", current_floor)
				return current_floor, attempts
			} else {
				// Если осталось ещё яйцо, проверяем все этажи между предыдущим и текущим
				lower := current_floor - step
				for floor := lower; floor < current_floor; floor++ {
					attempts += 1
					fmt.Printf("Проверяем %v-й этаж (попытка %v)\n", floor, attempts)
					fmt.Println("Разбило? (y/n)")
					var broke_inner string
					fmt.Scanln(&broke_inner)
					if broke_inner == "y" {
						fmt.Printf("Критический этаж: %v\n", floor)
						return floor, attempts
					}
				}
				fmt.Printf("Критический этаж: %v\n", current_floor-1)
				return current_floor - 1, attempts
			}
		} else {
			current_floor += step
			step -= 1
			if step < 1 {
				step = 1
			}
		}
	}

	// Если дошли до последнего этажа и яйцо не разбилось
	fmt.Printf("Критический этаж: %v (последний этаж)\n", max_floor)
	return max_floor, attempts
}

func main() {
	critical_floor, attempts := find_egg_break_floor(100, 2)
	fmt.Printf("\nРезультат: критический этаж = %v, попыток = %v\n", critical_floor, attempts)
}
