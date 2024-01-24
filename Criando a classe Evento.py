class Evento: 
    def __init__(self,nome, local=""):
        self.nome = nome
        self.local = local

    def imprime_informações(self):
        print("Nome do evento:", self.nome)
        print("Local do evento:", self.local)

    @classmethod
    def criador_de_evento(cls,nome):
        evento = cls(nome, local="pudim.com") 
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

ev = Evento ("Aula de python")
ev2 = Evento ("Aula de Java ","Rio de Janeiro") 
ev_aula = Evento.criador_de_evento("Live de Java")
area_pesssoas= Evento.calculo_pessoas


ev_aula.imprime_informações()
print(Evento.calculo_pessoas(5))
