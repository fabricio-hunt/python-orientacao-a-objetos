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
        print(f'{'Nome do Restaurante.'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.situacao}')

    @property
    def situacao (self):
        return 'Ativo✅' if self._situacao else 'Inativo❎'
    
    def alternar_estado(self):
        self._situacao = not self._situacao


restaurante_sabor_de_queimado = Restaurante('Sabor de Queimado', 'Churrascaria')
restaurante_sabor_de_queimado._nome = 'Sabor de Queimado'
restaurante_sabor_de_queimado.categoria = 'Churrascaria'
restaurante_sabor_de_queimado.alternar_estado()

churras_rest = Restaurante('Churras Rest', 'Churrascaria')
churras_rest._nome = 'Churras Rest'
churras_rest.categoria = 'Churrascaria'

tomy = Restaurante('Tomy', 'Peixaria')
tomy._nome = 'Tomy'
tomy.categoria = 'Peixaria'


Restaurante.listar_restaurantes()
