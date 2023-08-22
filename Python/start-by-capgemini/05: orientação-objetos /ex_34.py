class Pessoa:
    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento


class PessoaFisica(Pessoa):
    def __init__(self, nome, nascimento, rg, cpf):
        super().__init__(nome, nascimento)
        self.rg = rg
        self.cpf = cpf


class PessoaJuridica(Pessoa):
    def __init__(self, nome, nascimento, ie, cnpj):
        super().__init__(nome, nascimento)
        self.ie = ie
        self.cnpj = cnpj


def exibir_informacoes_pessoas(pessoas):
    for pessoa in pessoas:
        print("Nome:", pessoa.nome)
        print("Nascimento:", pessoa.nascimento)
        if isinstance(pessoa, PessoaFisica):
            print("RG:", pessoa.rg)
            print("CPF:", pessoa.cpf)
        elif isinstance(pessoa, PessoaJuridica):
            print("IE:", pessoa.ie)
            print("CNPJ:", pessoa.cnpj)
        print()


pessoa_fisica = PessoaFisica("Passon", "10/07/1500", "1.255.366", "177.255.366-55")
pessoa_juridica = PessoaJuridica("Empresa ABC", "03/03/2000", "123", "456789")

exibir_informacoes_pessoas([pessoa_fisica, pessoa_juridica])
