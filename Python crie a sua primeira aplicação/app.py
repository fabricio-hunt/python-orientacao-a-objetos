import os

restaurantes = ['Pizza Dont','Sushi Jalin','Sabor da Mesa', 'Delicia Restaurante']
print('')

def exibir_nome_do_programa():

     print("""
      
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
     print('1. Cadastrar restaurante')
     print('2. Listar restaurante')
     print('3. Ativar restaurante')
     print('4. Sair\n')

def finalizar__app():
     os.system('cls')
     print('Sistema Encerrado!!!\n')

def voltar_ao_menu_principal():
      input('Digite qualquer tecla para voltar ao Menu Principal: \n')
      main()

def opcao_invalida():
     print('Opção Inválida\n')
     voltar_ao_menu_principal()

def listar_restaurantes():
     os.system('cls')
     print('\nLISTA DE RESTAURANTES\n')
     print('-------------------------------')

     for restaurante in restaurantes:
          print(f'. {restaurante}')
     print('-------------------------------')
     voltar_ao_menu_principal()
     print('')
     main()

def cadastrar_novo_restaurante():
     os.system('cls')
     print('Cadastros de Novos Restaurantes:\n')
     nome_do_restaurante =  input('Digite o nome do restaurante: ')
     restaurantes.append(nome_do_restaurante)
     print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    
def escolher_opcoes():
     try:
          opcao_escolhida = int(input('Escolha uma opção: ')) 
          print(f'Você escolheu a opção {opcao_escolhida}')

          if opcao_escolhida == 1:
               cadastrar_novo_restaurante()
          elif opcao_escolhida == 2:
               listar_restaurantes()
          elif opcao_escolhida == 3:
               print('tivar restaurante')
          elif opcao_escolhida == 4:
               finalizar__app()
          else:
               opcao_invalida()
     except:
          opcao_invalida()
          
def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()
    
if __name__ == "__main__":
    main()




