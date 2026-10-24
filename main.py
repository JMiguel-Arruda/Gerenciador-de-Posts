import operacao_api 
from operacao_api import *

def main():
    while True:
        print("DIGITE 1 PARA CONSULTAR UM POST")
        print("DIGITE 2 PARA LISTAR POSTS DE UM USUÁRIO")
        print("DIGITE 3 PARA CRIAR UM POST")
        print("DIGITE 4 PARA ATUALIZAR UM POST")
        print("DIGITE 5 PARA EXCLUIR UM POST")
        print("DIGITE 6 PARA SAIR")
        resp = pedir_inteiro("Digite aqui: ")
        if resp not in(1, 2, 3, 4, 5, 6):
            print("Digite um comando válido!")
            continue
        if resp == 1:
            consultar_post()
        elif resp == 2:
            listar_posts()
        elif resp == 3:
            criar_post()
        elif resp == 4:
            atualizar_post()
        elif resp == 5:
            excluir_post()
        elif resp == 6:
            print("Encerrando....")
            break

if __name__ == "__main__":
    main()