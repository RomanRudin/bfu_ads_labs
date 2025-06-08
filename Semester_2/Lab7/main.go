package main

import (
	"fmt"
	"math/rand"
)

func randGenerator(lenght, min, max int) []int {
	slice := make([]int, lenght)
	for i := range lenght {
		slice[i] = rand.Intn(max-min+1) + min
	}
	return slice
}

func Kadane(arr []int) int {
	res, maxi := arr[0], arr[0]
	for i := 1; i < len(arr); i++ {
		maxi = max(maxi+arr[i], arr[i])
		res = max(res, maxi)
	}
	return res
}

func main() {
	array := randGenerator(10, -5, 5)
	fmt.Println(array)
	fmt.Println(Kadane(array))
}
