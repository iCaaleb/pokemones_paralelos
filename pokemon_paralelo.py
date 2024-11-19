import threading
import requests
import json

def obtener_datos_pokemon(id_pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{id_pokemon}"
    try:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            nombre = datos['name']
            tipos = [tipo['type']['name'] for tipo in datos['types']]
            estadisticas = {stat['stat']['name']: stat['base_stat'] for stat in datos['stats']}

            print(f"Nombre: {nombre}")
            print(f"Tipos: {', '.join(tipos)}")
            print("Estadísticas:")
            for stat, valor in estadisticas.items():
                print(f"  {stat}: {valor}")
            print("-" * 40)
        else:
            print(f"No se pudo obtener el Pokémon con ID {id_pokemon}. Código de estado: {respuesta.status_code}")
    except requests.RequestException as e:
        print(f"Error al obtener datos del Pokémon {id_pokemon}: {e}")


def main():
    numero_pokemones = 50 
    hilos = []

    for i in range(1, numero_pokemones + 1):
        hilo = threading.Thread(target=obtener_datos_pokemon, args=(i,))
        hilos.append(hilo)
        hilo.start()

    for hilo in hilos:
        hilo.join()



if __name__ == "__main__":
    main()