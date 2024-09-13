# OO

# Nome
#Categoria
#Situação (Se ativo / inativo)

class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = ''
        self.categoria  = ''
        self.situacao = False


restaurante_sabor_de_queimado = Restaurante('Sabor de Queimado', 'Churrascaria')
restaurante_sabor_de_queimado.nome = 'Sabor de Queimado'
restaurante_sabor_de_queimado.categoria = 'Churrascaria'


churras_rest = Restaurante('Churras Rest', 'Churrascaria')
churras_rest.nome = 'Churras Rest'
churras_rest.categoria = 'Churrascaria'


restaurantes = [restaurante_sabor_de_queimado, churras_rest]

print(vars(restaurante_sabor_de_queimado))
