package main

import (
	"fmt"
)

func get_BD(pattern string) map[string]int {
	badCharMap := make(map[string]int)

	for i, v := range pattern {
		badCharMap[string(v)] = i
	}

	return badCharMap
}

func bMBadCharacter(text, pattern string) []int {
	s_i := get_BD(pattern)
	res := []int{}
	shift := 0

	for shift <= (len(text) - len(pattern)) {
		j := len(pattern) - 1

		for j >= 0 && pattern[j] == text[shift+j] {
			j--
		}

		if j < 0 { //полное совпадение
			res = append(res, shift)
			shift++
		} else {
			badChar := string(text[shift+j])
			lastOccur, exists := s_i[badChar]
			shiftValue := 1
			if exists {
				shiftValue = max(1, j-lastOccur)
			}
			shift += shiftValue
		}
	}
	return res
}

func main() {
	fmt.Println("Result:", bMBadCharacter("hello my name is goga, do you wanna go bawling?", "go"))
}
