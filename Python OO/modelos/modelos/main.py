# OO

# Nome
#Categoria
#Situação (Se ativo / inativo)

class Restaurante:
    restaurantes = [] 

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self.categoria  = categoria
        self._situacao = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self.categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do Restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Status"}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.situacao}')

    @property
    def situacao (self):
        return 'Ativo✅' if self._situacao else 'Inativo❎'
    
    def alternar_estado(self):
        self._situacao = not self._situacao


# Criando o restaurante corretamente com dois argumentos
restaurante1 = Restaurante('Japones do Franco', 'Comida Japonesa')
restaurante1.alternar_estado()

# Chamada correta do método de classe para listar restaurantes
Restaurante.listar_restaurantes()
