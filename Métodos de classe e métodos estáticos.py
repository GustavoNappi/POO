class Evento: 
    def metodo_instancia(self):
        return("Metodo de instância chamado", self)
    @classmethod
    def metodo_classe(cls):
        return("metodo de classe", cls)
    
    @staticmethod
    def metodo_estatico():
        return "estatico chamado"
    


ev=Evento()

a = ev.metodo_instancia()
print(a)

b = Evento.metodo_classe()
print (b)

c = Evento.metodo_estatico()
print(c)
