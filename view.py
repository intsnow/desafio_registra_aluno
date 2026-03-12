import time

class View:

    def __init__(self):
        pass

    def input_matricula(self):
        try:
            return input("\n\nOlá! Por favor, digite sua matrícula:\t")
     
        except ValueError:
            print("\nERRO! A matrícula deve possuir apenas números...\n")
            return None


    def print_aluno_nao_encontrado(self):
        return print("\nFalha... Matrícula digitada é inexistente ou aluno NÃO está ativo no sistema!")
    

    def print_alunos_ativos(self, cont: int, dados: str):
        return print( f"\n\tDados_Alunos [ {cont}° ]" +
                      f"\n{dados}" + "\n" + "---"*15 )
                
                
    def input_menu_email(self, dados: dict):
        nome_split = dados.get("nome").strip().split(" ")

        try:
            if len(nome_split) > 2:
                return int(input(f"\n{dados.get("nome")}, por favor escolha uma das opções abaixo ao seu UFFMail" +
                            f"\n1 - {dados.get("uffmails")[0]}\n2 - {dados.get("uffmails")[1]}" +
                            f"\n3 - {dados.get("uffmails")[2]}\n4 - {dados.get("uffmails")[3]}" +
                            f"\n5 - {dados.get("uffmails")[4]}\n\n\t"))
            
            else:
                return int(input(f"\n{dados.get("nome")}, por favor escolha uma das opções abaixo ao seu UFFMail" +
                            f"\n1 - {dados.get("uffmails")[0]}\n2 - {dados.get("uffmails")[1]}" +
                            f"\n3 - {dados.get("uffmails")[2]}\n\n\t"))
        
        except ValueError:
            print("\nOpção INVÁLIDA! Digite apenas números dentro das opções disponiveis na tela...\n")


    def input_falha_opcao(self):
        return print("\nOpção INVÁLIDA! Por favor, redigite para uma das opções:\n")
    

    def print_sucesso_uffmail(self, dados: dict):
        print("\nSucesso... Começando print de uffmail e dados")
        print(f"\nA criação do e-mail de [{dados.get("nome")}] será feita nos próximos minutos..." )
        
        time.sleep(3)   # Simulando um envio real de SMS do sistema por um delay.
        return print(f"\nUm SMS foi enviado para [{dados.get("telefone")}] com a sua senha de acesso!")
        

    def print_erro(self):
        return print("\nERRO... Finalizando print de uffmail e dados")
    

    def print_atualiza_csv(self, dados: dict):
        return print(f"\nAtualizando {dados.get("nome")} e seus dados no CSV file...\n")