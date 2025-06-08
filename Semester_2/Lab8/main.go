package main

import (
	"fmt"
)

func count(coins []int, sum int) int {
	arr := make([]int, sum+1) //здесь храним кол-во решений для i-го
	//Нам нужна сумма+1 строк, так как слайс строится снизу вверх с использованием базового случая (сумма = 0)

	arr[0] = 1 //он нам нужен для таких случаев, что например данная величина будет 0

	for i := range len(coins) { // внешний цикл итерируется по номиналам, внутренний -- по целевой сумме
		for j := coins[i]; j <= sum; j++ {
			arr[j] += arr[j-coins[i]]
		}
	}
	return arr[sum]
}

func main() {
	coins := []int{2, 4}

	sum := 7

	fmt.Println(count(coins, sum))
}
