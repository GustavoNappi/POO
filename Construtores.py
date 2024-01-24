class Evento: 
    def __init__(self, nome ):
        self.nome = nome  
        self.local ="Brasil"
        self.pessoa = "Gustavo Nappi"
    
    def altera_nome_evento(self, novo_nome):
        print("alterando nome do evento") 
        self.nome = novo_nome

ev = Evento("AULA DE PYTHON")
ev2 = Evento("AULA JAVASCRIPT")

print(ev.nome)
print(ev.local)
print(ev.pessoa)
print(ev2.nome)
print(ev2.local)
print(ev2.pessoa)