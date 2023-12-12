from Pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome, cpf, email, endereco):
        super().__init__(nome, cpf, email)
        self.endereco = endereco