package main

import "fmt"

func rabinKarpSearch(text, pattern string) []int {
	const (
		d = 256 // размер алфавита
		q = 101 // простое число для модуля
	)

	n := len(text)
	m := len(pattern)
	if n < m || m == 0 {
		return nil
	}

	// Вычисляем h = d^(m-1) % q
	h := 1
	for i := 0; i < m-1; i++ {
		h = (h * d) % q
	}

	var patternHash, windowHash int

	// Вычисляем хеш образца и первого окна текста
	for i := range m {
		patternHash = (d*patternHash + int(pattern[i])) % q
		windowHash = (d*windowHash + int(text[i])) % q
	}

	var result []int

	// Проходим по тексту
	for i := 0; i <= n-m; i++ {
		// Проверяем совпадение хешей
		if patternHash == windowHash {
			// Если хеши совпали, проверяем посимвольно
			match := true
			for j := 0; j < m; j++ {
				if text[i+j] != pattern[j] {
					match = false
					break
				}
			}
			if match {
				result = append(result, i)
			}
		}

		// Пересчитываем хеш для следующего окна
		if i < n-m {
			windowHash = (d*(windowHash-int(text[i])*h) + int(text[i+m])) % q
			// Обеспечиваем положительное значение хеша
			if windowHash < 0 {
				windowHash += q
			}
		}
	}

	return result
}

func main() {
	text := "i like to watch basketball and play volleyball!~"
	pattern := "ball"
	positions := rabinKarpSearch(text, pattern)

	if len(positions) == 0 {
		fmt.Println("Образец не найден")
	} else {
		fmt.Printf("Образец найден на позициях: %v\n", positions)
	}
}
