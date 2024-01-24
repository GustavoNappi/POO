from Heranca import Evento

class EventoOnline(Evento):
    def __init__(self, nome, _=""):
        local = f"salahnappi.com.br//id={EventoOnline.id}"
        super().__init__(nome, local)

    def imprime_informações(self):
        print(f"Id Da aula: {self.id}")
        print(f"Nome do evento:{self.nome}")
        print(f"Link do evento:{self.local}")
        print("====================")