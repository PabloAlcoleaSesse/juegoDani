import json

def getNombreJugador():
    try:
        with open('player.json', 'r', encoding='utf-8') as file:
            datos = json.load(file)
            return datos.get('nombreJugador')
    except FileNotFoundError:
        print("Error: player.json no encontrado")
        return None
    except json.JSONDecodeError:
        print("Error: player.json tiene formato incorrecto")
        return None


def guardarNombreJugador(nombre):
    datos = {'nombreJugador': nombre}
    with open('player.json', 'w', encoding='utf-8') as file:
        json.dump(datos, file, ensure_ascii=False, indent=4)
