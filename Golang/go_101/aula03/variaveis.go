package main;

import "fmt";

var ( //Váriavel de nível de packages
	name string;
	num1 int;
	num2 int32;
)

func main() {
	// := inicia uma váriavel já com um valor
	message := "Aula 03 - Curso GO 101";
	fmt.Println(message);

	var boolean, float, string = true, 2.65, "Olá";
	fmt.Println(boolean, float, string);

	name := "Sir Passon";
	fmt.Println("Hello,", name, "!");

	var total int;
	total++;
	fmt.Println("int: inicia com 0, boolean com false e string vazia:", "\nTotal:", total);

	var x, y = 10, 20; // troca de valores
	fmt.Println(x, y)
	y , x = x , y
	fmt.Println(x, y)
}