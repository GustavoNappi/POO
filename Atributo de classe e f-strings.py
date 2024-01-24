class Evento:
    id = 1
    def __init__(self,nome, local=""):
        self.nome = nome
        self.local = local
        self.id = Evento.id
        Evento.id += 1 

    def imprime_informações(self):
        print(f"Nome do evento:{self.nome}")
        print(f"Local do evento:{self.local}")
        print(f"Id Da aula: {self.id}")
        print("====================")

    @classmethod
    def criador_de_evento(cls,nome):
        evento = cls(nome, local=f"pudim.com/id={cls.id}") 
        return evento   
    
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

ev = Evento.criador_de_evento ("Aula de python")
ev2 = Evento.criador_de_evento ("Aula de Java")
ev.imprime_informações()
ev2.imprime_informações()