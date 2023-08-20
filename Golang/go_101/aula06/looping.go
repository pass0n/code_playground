package main

import "fmt"

func printX(num int) {
	fmt.Printf("==============================\nLaço for opção %d.\n\n", num)
}

func main() {
	nomes := []string{"Tupiniquim", "Seu Zé", "Marta Matadora", "Paulin do Cão", "Lucas das Galinhas"}
	
	printX(1)
	for i := 0; i < len(nomes); i++ {
		fmt.Println(nomes[i])
	}

	printX(2)
	var i int
	for i < len(nomes) {
		fmt.Println(nomes[i])
		i++
	}
	
	printX(3)
	for key, names := range nomes {
		fmt.Println(key, names)
	}
}
