package main

import "fmt"

type Pessoa struct {
	Nome   string
	Idade  uint8
	Status bool
}

func (p Pessoa) String() string {
	return fmt.Sprintf("Olá, meu nome é %s e eu tenho %d anos.", p.Nome, p.Idade)
}

type PessoaFisica struct {
	Pessoa
	Sobrenome string
	cpf       string
}

func main() {
	p := PessoaFisica{
		Pessoa{
			Nome:   "Bob",
			Idade:  105,
			Status: true,
		},
		"Esponja",
		"025.666.157.899"}

	fmt.Println(p)
}
