package main

import "fmt"

// строим детерминированный конечный автомат для поиска подстроки
func buildDFA(pattern string) [][]int {
	m := len(pattern)
	if m == 0 {
		return nil
	}

	// таблица переходов [состояние][символ] -> следующее состояние
	dfa := make([][]int, m+1)
	for i := range dfa {
		dfa[i] = make([]int, 256) // заполняем ASCII символами
	}

	// начальное состояние: по первому символу переходим в состояние 1
	dfa[0][pattern[0]] = 1

	// состояние отката
	x := 0

	// заполняем таблицу переходов
	for i := 1; i < m; i++ {
		// копируем переходы из состояния отката
		for c := range 256 {
			dfa[i][c] = dfa[x][c]
		}
		// устанавливаем переход по текущему символу
		dfa[i][pattern[i]] = i + 1
		// обновляем состояние отката
		x = dfa[x][pattern[i]]
	}

	// последнее состояние (полное совпадение)
	for c := range 256 {
		dfa[m][c] = dfa[x][c]
	}

	return dfa
}

// searchSubstring ищет подстроку в тексте с использованием DFA
func finiteAutomatonSearch(text, pattern string) []int {
	if len(pattern) == 0 {
		return nil
	}

	dfa := buildDFA(pattern)
	var result []int
	state := 0
	m := len(pattern)

	for i := range len(text) {
		state = dfa[state][text[i]] // переход по символу
		if state == m {
			// найдено совпадение
			result = append(result, i-m+1)
		}
	}

	return result
}

func main() {
	testCases := []struct {
		text    string
		pattern string
	}{
		{"abaaba", "aba"},
		{"ababcabc", "abc"},
		{"aaa", "b"},
		{"abababab", "aba"},
		{"", "a"},
		{"abc", ""},
	}

	for _, tc := range testCases {
		fmt.Printf("text: %q, pattern: %q\n", tc.text, tc.pattern)
		fmt.Println("positions:", finiteAutomatonSearch(tc.text, tc.pattern))
	}
}
