from dataclasses import dataclass, asdict

@dataclass
class Aluno:
    nome : str = ""
    matricula : str = ""
    telefone : str = ""
    email : str = ""
    uffmail : str = ""
    status : str = ""


    @classmethod
    def input_dados(cls, dados: dict):
        safe_dados = { k:v for k, v in dados.items()
                 if k in cls.__annotations__ }
        
        return cls(**safe_dados)
    

    def retorna_dados(self):
        return f"Nome:\t{self.nome}\nMatricula:\t{self.matricula}\nTelefone:\t{self.telefone}\nEmail:\t{self.email}\nUFF_Email:\t{self.uffmail}\nStatus:\t{self.status}"


    def to_dict(self):
        return asdict(self)
    

    def to_csv(self):
        return f"{self.nome},{self.matricula},{self.telefone},{self.email},{self.uffmail},{self.status}\n"