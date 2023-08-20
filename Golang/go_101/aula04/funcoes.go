package main

import (
	"fmt"
	"strconv"
)

// Funções com inical maiúscula são de escopo público e com inicial minúscula escopo de package
func hello(name string) {
	fmt.Println("Hello", name)
}

func soma(a, b int) int {
	return a + b
}

func converterESomar(a int, b string) (total int, err error) {
	i, err := strconv.Atoi(b)

	if err != nil {
		return
	}

	total = a + i
	return
}

func main() {
	hello("Sir Passon")

	fmt.Println("total:", soma(10, 20))
	total, err := converterESomar(10, "23")
	fmt.Println("total:", total, err)
}
