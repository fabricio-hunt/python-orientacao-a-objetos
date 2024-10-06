# Restaurante Python - Orientação a Objetos

Este repositório contém um exemplo de código do curso de **Python e Orientação a Objetos** da Alura, que ilustra o uso de classes, métodos e encapsulamento em Python por meio de uma simulação de cadastro e gerenciamento de restaurantes.

## Funcionalidades

- Cadastro de restaurantes com nome e categoria.
- Alternância do estado do restaurante (ativo/inativo).
- Listagem dos restaurantes cadastrados, incluindo nome, categoria e status atual.

## Estrutura do Código

### Classe `Restaurante`

A classe principal do código é `Restaurante`, que armazena os dados de todos os restaurantes cadastrados. Abaixo estão os principais métodos e propriedades da classe:

- **Atributos**:
  - `nome`: Nome do restaurante, formatado em título.
  - `categoria`: Categoria do restaurante (ex: Comida Japonesa, Comida Italiana).
  - `situacao`: Status atual do restaurante (Ativo/ Inativo).
  
- **Métodos**:
  - `__str__`: Método de representação textual do restaurante, exibindo seu nome e categoria.
  - `listar_restaurantes`: Método de classe que lista todos os restaurantes cadastrados, mostrando nome, categoria e situação.
  - `alternar_estado`: Método que altera o estado do restaurante entre ativo e inativo.
  
- **Propriedades**:
  - `situacao`: Propriedade que retorna uma string indicando se o restaurante está ativo (`Ativo ✅`) ou inativo (`Inativo ❎`).

## Exemplo de Uso

![image](https://github.com/user-attachments/assets/ec577e8f-1c5f-43d3-8b1b-e12c3761ed1a)


```python
# Criando o restaurante corretamente com dois argumentos
restaurante1 = Restaurante('Japones do Franco', 'Comida Japonesa')
restaurante1.alternar_estado()

# Listando os restaurantes cadastrados
Restaurante.listar_restaurantes() 




