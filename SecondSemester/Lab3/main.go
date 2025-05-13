package main

import (
	"fmt"
	"math"
)

func largest_subarray(arr []int) ([]int, int) {
	max_sum := math.MinInt64
	sum := 0
	s, e := 0, 0

	for i, v := range arr {
		sum += v
		if sum > max_sum {
			max_sum, e = sum, i
		}
		if sum < 0 {
			sum, s = 0, i+1
		}
	}
	if max_sum > 0 {
		return arr[s : e+1], max_sum
	} else {
		return []int{max_sum}, max_sum
	}

}

func main() {
	arr := []int{-2, 1, -3, 4, -1, 2, 1, -5, 4}
	fmt.Println(largest_subarray(arr))
}
