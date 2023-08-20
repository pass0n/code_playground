// Métodos são funções atreladas a uma struct

package main

import "fmt"

type Pessoa struct {
	Nome      string
	Sobrenome string
	Idade     uint8
	Status    bool
	cpf       string
}

func (p Pessoa) String() string {
	return fmt.Sprintf("Olá, meu nome é %s e eu tenho %d anos.", p.Nome, p.Idade)
}

type Categoria struct {
	Nome string
	Pai  *Categoria
}

func (c Categoria) HasParent() bool {
	return c.Pai != nil
}

func (c *Categoria) SetPai(pai *Categoria) {
	c.Pai = pai
}

func main() {
	p := Pessoa{"Bob", "Esponja", 105, true, "025.666.157.899"}
	p.cpf = "1"
	fmt.Println(p)

	cat := Categoria{Nome: "Categoria 1"}

	if !cat.HasParent() {
		fmt.Println("Não tem pai")
	}

	catPai := Categoria{Nome: "Categoria 1"}
	catPai.SetPai(&Categoria{Nome: "Pai"})

	if catPai.HasParent() {
		fmt.Println("Tem pai")
	}
}
