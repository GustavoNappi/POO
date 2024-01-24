from Heranca import Evento
from evento_online import EventoOnline  

ev_online = EventoOnline ("Aula de python")
ev2_online = EventoOnline("Aula de Java")

print(ev_online.to_json())
print(ev2_online.to_json())

ev = Evento("Aula de Python", "RJ")
ev.imprime_informações()