class Pessoa:
    def __init__(self, nome, ano_nascimento, dado):
        self.nome = nome
        self._ano_nascimento = ano_nascimento
        self._dado = dado

    #(@property) assinatura que indica que não ira usar como metodo. apenas para mostrar o valor
    @property
    def idade(self):
        _ano_atual = 2023
        return _ano_atual - self._ano_nascimento

    @property
    def valor(self):
        return self._dado

    #(@.setter) assinatura indica que você esta setando o valor da variavel que é privada
    @valor.setter
    def valor(self, value):
        self._dado = value




pessoa = Pessoa('Murilo', 1996, 100)
print(f"Nome: {pessoa.nome} \n"
      f"Idade: {pessoa.idade} \n"
      f"Dado: {pessoa.valor}")
pessoa.valor = 200

print(f"Dado: {pessoa.valor}")