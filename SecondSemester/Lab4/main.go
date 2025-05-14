package main

import (
	"fmt"
)

/*
Эта функция вычисляет массив borders (также известный как "массив префикс-функции") для строки s.
1)Мы инициализируем массив borders и текущий индекс curr_index.
2)Для каждого символа в строке (начиная со второго) обновляем curr_index:

	-Пока curr_index > 0 и символы не совпадают, отступаем назад по borders.
	-При совпадении символов увеличиваем curr_index.
	-Записываем текущее значение curr_index в borders[i].
*/
func find_borders(s string) []int {
	borders := make([]int, len(s))
	curr_index := 0

	for i := 1; i < len(s); i++ {
		for (curr_index > 0) && (s[curr_index] != s[i]) {
			curr_index = borders[curr_index-1]
		}
		if s[curr_index] == s[i] {
			curr_index += 1
		}
		borders[i] = curr_index
	}
	return borders
}

/*
-Мы сначала вычисляем borders для подстроки s.
-Затем проходим по тексту txt, поддерживая текущий индекс comp_index в подстроке s.
-При несовпадении используем borders для "перепрыгивания" уже совпавших частей.
-При полном совпадении (comp_index == len(s)) добавляем позицию в результат и корректно обновляем comp_index.
*/
func KMP(s string, txt string) []int {
	borders := find_borders(s)
	result := []int{}
	comp_index := 0

	for i := 0; i < len(txt); i++ {
		for (comp_index > 0) && (txt[i] != s[comp_index]) {
			comp_index = borders[comp_index-1]
		}
		if txt[i] == s[comp_index] {
			comp_index += 1
		}
		if comp_index == len(s) {
			result = append(result, i-comp_index+1)
			comp_index = borders[len(s)-1]
		}
	}
	return result
}

func main() {
	txt := "abacaba"
	s := "aba"
	fmt.Println("Результат:\n", KMP(s, txt))

	s = "abc"
	txt = "ababcabc"
	fmt.Println("Результат:\n", KMP(s, txt))

	s = "a"
	txt = "aaaaa"
	fmt.Println("Результат:\n", KMP(s, txt))
}
