import json

class Evento:
    id = 1

    def __init__(self, nome, local=""):
        self.nome = nome
        self.local = local
        self.id = Evento.id
        Evento.id += 1
        
    def imprime_informações(self):
        print(f"ID do evento:{self.id}")
        print(f"Local do nome:{self.nome}")
        print(f"Local do evento: {self.local}")
        print("====================")

    def to_json(self):
        return json.dumps({
            "id": self.id,
            "local":self.local,
            "nome": self.nome,

        })
     
    @staticmethod
    def calculo_pessoas(area):
        if 5 <= area < 10: #deixnado o codigo bem mais limpo tirando o and o python ja le
            return 5
        elif 10 <= area < 20: 
            return 15
        elif area >= 20:
            return 30
        else:
            return 0

