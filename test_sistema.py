import unittest
from sistema import Sistema
from aluno import Aluno

class TestSistema(unittest.TestCase):

    def setUp(self):
        self.sys = Sistema()

    def test_processa_opcoes_uffmails_nome_longo(self):
        dados = {"nome": "Luiza Alves Cardoso"}
        
        resultado = self.sys.processa_opcoes_uffmails(dados)
        
        # Verifica se gera exatamente 5 uffmails
        self.assertEqual(len(resultado), 5) 

        self.assertIn("luiza_alves@id.uff.br", resultado)      
        self.assertIn("luizaac@id.uff.br", resultado)          
        self.assertIn("luizacardoso@id.uff.br", resultado)     
        self.assertIn("lcardoso@id.uff.br", resultado)         
        self.assertIn("lalvescardoso@id.uff.br", resultado)

    # Descomentar quando for adicionar "Iago Neves" no csv

    def test_processa_opcoes_uffmails_nome_curto(self):
        dados = {"nome": "Iago Neves"}
        
        resultado = self.sys.processa_opcoes_uffmails(dados)
        
        # Verifica a adaptação do código para apenas 3 uffmails
        self.assertEqual(len(resultado), 3) 

        self.assertIn("iago_neves@id.uff.br", resultado)
        self.assertIn("ineves@id.uff.br", resultado)
        self.assertIn("iagon@id.uff.br", resultado)


    def test_busca_aluno_ativo(self):
        aluno_mock = Aluno(nome="Victor Dias Barbosa", matricula="108905", status="Ativo")
        self.sys.alunos_ativos["108905"] = aluno_mock
        
        resultado_sucesso = self.sys.busca_aluno_ativo("108905")
        resultado_falha = self.sys.busca_aluno_ativo("999999")
        
        self.assertIsNotNone(resultado_sucesso)
        self.assertEqual(resultado_sucesso.nome, "Victor Dias Barbosa")
        self.assertIsNone(resultado_falha)


if __name__ == "__main__":
    unittest.main()