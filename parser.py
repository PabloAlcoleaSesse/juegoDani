from partida import Partida

p = Partida("Jugador1")

p.__dict__

import json

with open('partida_guardada.json', 'w') as file:
    json.dump(p.__dict__, file, indent=4)