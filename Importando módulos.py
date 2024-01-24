class Evento:
    id = 1

    def imprime_informações(self):
        print(f"Nome do evento:{self.nome}")
        print(f"Local do evento:{self.local}")
        print(f"Id Da aula: {self.id}")
        print("====================")

     
    
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




ev = EventoOnline ("Aula de python")
ev2 = EventoOnline("Aula de Java")
ev.imprime_informações()
ev2.imprime_informações()

ev = Evento("Aula de Python", "RJ")
ev.imprime_informações()