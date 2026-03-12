from sistema import Sistema
from view import View
import time


def start_processos(sys: Sistema):
    sys.processa_alunos_from_file()


def start_listagem_alunos(sys: Sistema, view: View):
    alunos_ativos = sys.lista_alunos_ativos()
    
    for cont, aluno in enumerate(alunos_ativos.values(), 1):
        dados = aluno.retorna_dados()
        view.print_alunos_ativos(cont, dados)


def start_menu(sys:  Sistema, view: View):
    matri = view.input_matricula()

    while not matri:
        matri = view.input_matricula()

    aluno_buscado = sys.busca_aluno_ativo(matri)

    if not aluno_buscado:
        view.print_aluno_nao_encontrado()
        return False

    aluno_dict = sys.aluno_to_dict(aluno_buscado)
    uffmails = sys.processa_opcoes_uffmails(aluno_dict)

    #   Adicionando item novo tipo list de valor contendo as opções de uffmails
    aluno_dict["uffmails"] = uffmails

    #   Menu em ação
    op = view.input_menu_email(aluno_dict)
    
    while op not in range(1, len(uffmails) + 1):
        view.input_falha_opcao()
        op = view.input_menu_email(aluno_dict)

    if op:
        uffmail_escolhido = sys.uffmail_resultante(aluno_dict, op)

        #   Deletando atributo temporario anterior 
        del aluno_dict["uffmails"]
        aluno_dict["uffmail"] = uffmail_escolhido

        #   Por fim, cria temp_aluno para atualizar dados antigos de aluno no sistema
        aluno = sys.cria_temp_aluno(aluno_dict)
        atualizou_sistema = sys.atualiza_aluno_cadastrado(aluno)
        atualizou_csv = sys.atualiza_alunos_from_file(aluno)

        if aluno and atualizou_sistema and atualizou_csv:
            view.print_sucesso_uffmail(aluno_dict)
            view.print_atualiza_csv(aluno_dict)

            time.sleep(1.6)

        else:
            view.print_erro()



def main():
    sys = Sistema()
    view = View()

    start_processos(sys)
    start_listagem_alunos(sys, view)
    op = start_menu(sys, view)

    match op:
        case True:
            return 

        case False:
            op = start_menu(sys, view)


if __name__ == "__main__":
    main()