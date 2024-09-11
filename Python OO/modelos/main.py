# OO

# Nome
#Categoria
#Situação (Se ativo / inativo)

class Restaurante:
    nome = ''
    categoria  = ''
    situacao = False


restaurante_sabor_de_queimado = Restaurante()
restaurante_sabor_de_queimado.nome = 'Sabor de Queimado'
restaurante_sabor_de_queimado.categoria = 'Churrascaria'


churras_rest = Restaurante()
churras_rest.nome = 'Churras Rest'
churras_rest.categoria = 'Churrascaria'


restaurantes = [restaurante_sabor_de_queimado, churras_rest]
