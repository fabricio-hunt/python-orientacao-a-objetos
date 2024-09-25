# Definindo uma classe em Python. Classes são "moldes" para criar objetos.
# A classe 'Carro' será usada para criar objetos que representam carros.
class Carro:
    # O método __init__ é o construtor da classe. Ele é chamado automaticamente
    # quando criamos um novo objeto da classe. É usado para inicializar atributos do objeto.
    def __init__(self, marca, modelo, ano):
        # Os atributos 'marca', 'modelo' e 'ano' são inicializados aqui.
        # O self é uma referência ao próprio objeto da classe e é obrigatório como primeiro
        # argumento de qualquer método que pertença a uma classe.
        self.marca = marca  # atributo 'marca'
        self.modelo = modelo  # atributo 'modelo'
        self.ano = ano  # atributo 'ano'

    # Este é um método da classe 'Carro'. Ele representa um comportamento
    # que objetos do tipo 'Carro' podem ter.
    def exibir_informacoes(self):
        # Este método imprime as informações do carro formatadas.
        print(f"Carro: {self.marca} {self.modelo}, Ano: {self.ano}")

    # Outro método da classe, representando mais um comportamento.
    def ligar_motor(self):
        print(f"O motor do {self.modelo} está ligado!")

# Aqui criamos um objeto da classe 'Carro'. Ao criar um objeto,
# o método __init__ é chamado automaticamente.
carro1 = Carro("Toyota", "Corolla", 2020)

# Aqui estamos chamando métodos do objeto 'carro1'.
# Esses métodos fazem o objeto realizar certas ações.
carro1.exibir_informacoes()  # Exibe as informações do carro
carro1.ligar_motor()  # Simula ligar o motor do carro

# Herança em Python: Podemos criar uma nova classe que herda de uma classe existente.
# A classe 'CarroEletrico' herda da classe 'Carro', ou seja, terá os mesmos métodos e atributos,
# mas podemos adicionar ou modificar funcionalidades específicas.
class CarroEletrico(Carro):
    # O método __init__ da classe derivada pode ser redefinido,
    # mas ainda chamamos o __init__ da classe pai usando super().
    def __init__(self, marca, modelo, ano, autonomia_bateria):
        # Chamando o construtor da classe base (Carro) para inicializar os atributos herdados.
        super().__init__(marca, modelo, ano)
        # Atributo adicional específico para o carro elétrico.
        self.autonomia_bateria = autonomia_bateria

    # Sobrescrita de método: Podemos redefinir um método da classe pai.
    def exibir_informacoes(self):
        # Aqui chamamos o método da classe base usando super() e adicionamos mais informações.
        super().exibir_informacoes()  # Mantemos o comportamento original
        print(f"Autonomia da bateria: {self.autonomia_bateria} km")

    # Um novo método específico para a classe CarroEletrico.
    def carregar_bateria(self):
        print(f"A bateria do {self.modelo} está sendo carregada!")

# Criamos um objeto da classe derivada 'CarroEletrico'.
carro2 = CarroEletrico("Tesla", "Model S", 2022, 500)

# Chamando os métodos do objeto carro2. Alguns são herdados e outros são específicos.
carro2.exibir_informacoes()  # Exibe as informações, incluindo a autonomia da bateria
carro2.ligar_motor()  # Método herdado da classe Carro
carro2.carregar_bateria()  # Método específico da classe CarroEletrico
