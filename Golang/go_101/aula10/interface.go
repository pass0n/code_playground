package main

import "fmt"

type Document interface {
	Doc() string
}

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

func (pf PessoaFisica) Doc() string {
	return fmt.Sprintf("Meu cpf é %s", pf.cpf)
}

type PessoaJuridica struct {
	Pessoa
	RazaoSocial string
	cnpj        string
}

func (pj PessoaJuridica) Doc() string {
	return fmt.Sprintf("Meu cnpj é %s", pj.cnpj)
}

func show(d Document) {
	fmt.Println(d)
	fmt.Println(d.Doc())
}

func main() {
	pf := PessoaFisica{
		Pessoa{
			Nome:   "Bob",
			Idade:  105,
			Status: true,
		},
		"Esponja",
		"025.666.157.899"}

	show(pf)
	fmt.Println()

	pj := PessoaJuridica{
		Pessoa{
			Nome:   "Bobinho",
			Idade:  5,
			Status: true,
		},
		"Esponja Jobs INC.",
		"00.154.457/899-45"}

	show(pj)
}
