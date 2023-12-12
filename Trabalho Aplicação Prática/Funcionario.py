from Pessoa import Pessoa


class Funcionario(Pessoa):
    def __init__(self, nome, cpf, email, cargo):
        super().__init__(nome, cpf, email)
        self.cargo = cargo