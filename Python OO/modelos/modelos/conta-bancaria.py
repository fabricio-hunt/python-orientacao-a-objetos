
# ---------------------------------------

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False  # Conta inativa por padrão

    # Mensagem em string para os atributos da classe 
    def __str__(self):
        return f'Nome: {self.titular}, seu saldo da conta é R$: {self.saldo:.2f}'

    @property
    def ativo(self):
        return 'Ativo✅' if self._ativo else 'Inativo❎'

    @ativo.setter
    def ativo(self, valor):
        self._ativo = valor

    # Alterna o estado de ativo/inativo
    def alternar_estado(self):
        self.ativo = not self._ativo

# Criando uma instância da conta bancária
cliente_banco_credito1 = ContaBancaria('Davi Emanuel', 452.98)
cliente_banco_credito1.alternar_estado()

# Imprimindo a conta
print(cliente_banco_credito1)
print(f'Estado da conta: {cliente_banco_credito1.ativo}')






    

