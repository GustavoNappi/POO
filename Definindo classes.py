class Evento: 
    def altera_nome_evento(self, novo_nome):
        print("alterando nome do evento") 
        self.nome = novo_nome

ev = Evento()
ev.nome= "Aula de python"
print(ev.nome)

##miau miau miau miau miau

ev.altera_nome_evento("AULA DE JAVASCRIPT")
print(ev.nome)  