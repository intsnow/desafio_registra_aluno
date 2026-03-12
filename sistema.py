from aluno import Aluno

class Sistema:

    def __init__(self):
        self.alunos_ativos = {}

    def processa_alunos_from_file(self):
        
        with open("alunos.csv", "r", encoding="utf-8") as f:
            #   Coleta lista unica dos nomes de cada coluna, que servirá
            #   de parâmetro a criação de objetos Alunos posteriormente
            atributos_nomes = f.readline().strip().split(",")    

            for linha_aluno in f:
                
                #   Lista de cada dado/célula por linha_aluno do arquivo
                linha_aluno = linha_aluno.strip().split(",")

                dados_dict = {}
                for atrib_chave, dados in zip(atributos_nomes, linha_aluno):
                    dados_dict[atrib_chave] = dados

                aluno = self.cria_temp_aluno(dados_dict)

                if aluno.status == "Ativo":
                    self.alunos_ativos[aluno.matricula] = aluno 


    def atualiza_alunos_from_file(self, aluno: Aluno):
        conteudo_atualizado = []
        atualizou = False

        with open("alunos.csv", "r", encoding="utf-8") as f:
            conteudo_atualizado.append(f.readline())

            for linha_aluno in f:
                
                #   Lista de cada dado/célula por linha_aluno do arquivo
                aluno_dados = linha_aluno.strip().split(",")

                if aluno.matricula == aluno_dados[1]:
                    linha_aluno_novo_csv = aluno.to_csv()

                    conteudo_atualizado.append(linha_aluno_novo_csv)
                    atualizou = True

                else:
                    conteudo_atualizado.append(linha_aluno)
            
        if atualizou:

            with open("alunos.csv", "w", encoding="utf-8") as f:
                f.writelines(conteudo_atualizado)

            return True
            
        return False


    def cria_temp_aluno(self, dados: dict):
        aluno = Aluno().input_dados(dados)
        return aluno


    def busca_aluno_ativo(self, matri):
        aluno = self.alunos_ativos.get(matri)
        return aluno
    

    def atualiza_aluno_cadastrado(self, aluno: Aluno):
        
        try:
            del self.alunos_ativos[aluno.matricula] 
            self.alunos_ativos[aluno.matricula] = aluno

            return True
        
        except Exception:
            return False


    def lista_alunos_ativos(self):
        return self.alunos_ativos
        

    def aluno_to_dict(self, aluno: Aluno):
        return aluno.to_dict()
    
    
    def processa_opcoes_uffmails(self, dados: dict):
        partes = dados.get("nome").lower().strip().split(" ")
        uffmails = []
        
        uffmails.append(partes[0] + "_" + partes[1] + "@id.uff.br")

        if len(partes) > 2:
            uffmails.append(partes[0] + partes[1][0] + partes[2][0] + "@id.uff.br" )  
            uffmails.append(partes[0] + partes[2] + "@id.uff.br" ) 
            uffmails.append(partes[0][0] + partes[2] + "@id.uff.br" )  
            uffmails.append(partes[0][0] + partes[1] + partes[2] + "@id.uff.br" )
        
        else:
            uffmails.append(partes[0] + partes[1][0] + "@id.uff.br" )  
            uffmails.append(partes[0][0] + partes[1] + "@id.uff.br" ) 

        return uffmails
            
          
    def uffmail_resultante(self, dados: dict, op: int):
        match op:

            case 1:
                return dados.get("uffmails")[0]
            case 2:
                return dados.get("uffmails")[1]
            case 3:
                return dados.get("uffmails")[2]
            case 4:
                return dados.get("uffmails")[3]
            case 5:
                return dados.get("uffmails")[4]
            
            case _:
                return None
            