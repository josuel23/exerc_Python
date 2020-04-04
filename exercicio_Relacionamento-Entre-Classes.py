class Pessoa:
    def __init__(self, nome, idade, sexo, endereco):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo     
        self.endereco = endereco.rua
        

    def exibir_dados(self):
        print('Nome:', self.nome)
        print('Idade:', self.idade)
        print('Sexo:', self.sexo)
        

class Endereco:
    def __init__(self, rua, numero, cep):
        self.rua = rua
        self.numero = numero
        self.complemento = ' '
        self.cep = cep

    def exibir_dados(self):
        print('Rua:', self.rua)
        print('Número:', self.numero)
        print('Complemento: ', self.complemento)
        print('CEP:', self.cep)

ender = Endereco('Av. Paulista', 74, 16185495)
ender.complemento = ('sala:02')

usuario = Pessoa('Paulo', 45, 'M', ender)

usuario.exibir_dados()
ender.exibir_dados()    
