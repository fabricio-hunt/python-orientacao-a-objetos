# OO

# Nome
#Categoria
#Situação (Se ativo / inativo)

class Restaurante:
    restaurantes = [] 

    def __init__(self, nome, categoria):
        self.nome = ''
        self.categoria  = ''
        self._situacao = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.situacao}')

    @property
    def situacao (self):
        return 'Ativo✅' if self._situacao else 'Inativo❎'


restaurante_sabor_de_queimado = Restaurante('Sabor de Queimado', 'Churrascaria')
restaurante_sabor_de_queimado.nome = 'Sabor de Queimado'
restaurante_sabor_de_queimado.categoria = 'Churrascaria'

churras_rest = Restaurante('Churras Rest', 'Churrascaria')
churras_rest.nome = 'Churras Rest'
churras_rest.categoria = 'Churrascaria'

tomy = Restaurante('Tomy', 'Peixaria')
tomy.nome = 'Tomy'
tomy.categoria = 'Peixaria'


Restaurante.listar_restaurantes()
