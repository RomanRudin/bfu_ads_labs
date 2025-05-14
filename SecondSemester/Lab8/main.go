package main

import (
	"fmt"
)

func count(coins []int, sum int) int {
	dp := make([]int, sum+1)

	dp[0] = 1

	for i := range len(coins) {
		for j := coins[i]; j <= sum; j++ {
			dp[j] += dp[j-coins[i]]
		}
	}
	return dp[sum]
}

func main() {
	coins := []int{2, 4}

	sum := 7

	fmt.Println(count(coins, sum))
}
