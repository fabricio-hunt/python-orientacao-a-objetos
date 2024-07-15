import os

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


def escolher_opcoes():
     opcao_escolhida = int(input('Escolha uma opção: ')) 
     print(f'Você escolheu a opção {opcao_escolhida}')

     if opcao_escolhida == 1:
          print('Cadastar Restaurante')
     elif opcao_escolhida == 2:
          print('Listar restaurante')
     elif opcao_escolhida == 3:
          print('tivar restaurante')
     else:
          finalizar__app()


def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()
    
if __name__ == "__main__":
    main()




