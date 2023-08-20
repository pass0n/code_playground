package main

import (
	"fmt"
)

type Pessoa struct {
	Nome string
	Sobrenome string
	Idade uint8
	Status bool
}

func main() {

	p := Pessoa {
		Nome: "Kayllon",
		Sobrenome: "Passon",
		Idade: 22,
		Status: true,
	}
	fmt.Println(p)

	//nomes := make([]string, 10, 20) //! Inicia um slice com 10 espaços com valor 0 e 20 de capacidade.
	nomes := []string {"Maria", "Mario", "Joca", "Carl"}
	fmt.Println(nomes, len(nomes), cap(nomes))
																													//! LEN = Tamanho do Slice e CAP é a capacidade.
	nomes = append(nomes, "Michael")
	fmt.Println(nomes, len(nomes), cap(nomes))

	nomes = append(nomes, "Michelle")
	fmt.Println(nomes, len(nomes), cap(nomes))

	idades := make(map[string]uint8)
	idades["Thiago"] = 31
	idades["Fernando"] = 24
	idades["Julia"] = 16
	fmt.Println(idades)

	val, ok := idades["Flávio"]
	fmt.Println(val, ok) 
}