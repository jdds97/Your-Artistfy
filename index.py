# Importamos los módulos necesarios
import json
import base64
import os
from dotenv import load_dotenv
from requests import post, get

# Cargamos las variables de entorno
load_dotenv()

# Obtenemos las credenciales de Spotify de las variables de entorno
cliente_id = os.getenv("CLIENTE_ID")
cliente_secreto = os.getenv("CLIENTE_SECRETO")

# Función para obtener el token de acceso a Spotify
def obtener_token():
    # Codificamos las credenciales en base64
    auth_string = f"{cliente_id}:{cliente_secreto}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

    # Hacemos una petición POST a la API de Spotify para obtener el token
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {"grant_type": "client_credentials"}
    resultado = post(url, headers=headers, data=data)

    # Parseamos la respuesta y obtenemos el token
    resultado_json = json.loads(resultado.content)
    token = resultado_json["access_token"]
    return token

# Obtenemos el token de acceso a Spotify
token = obtener_token()

# Función para obtener el header de autenticación
def obtener_autentificacion_header(token):
    return {"Authorization": "Bearer " + token}

# Función para buscar un artista en Spotify
def buscar_artista(token, nombre):
    url = "https://api.spotify.com/v1/search"
    headers = obtener_autentificacion_header(token)
    parametros = f"?q={nombre}&type=artist&limit=1"
    parametros_url = url + parametros
    resultado = get(parametros_url, headers=headers)
    resultado_json = json.loads(resultado.content)["artists"]["items"]
    if len(resultado_json) == 0:
        print("No existe ningún artista con el nombre indicado ")
        return None
    id_artista = resultado_json[0]["id"]
    return id_artista

# Función para obtener las top tracks de un artista por su ID
def obtenerTopTracksPorId(token, id_artista):
    top_Tracks = (
        f"https://api.spotify.com/v1/artists/{id_artista}/top-tracks?country=ES"
    )
    headers = obtener_autentificacion_header(token)
    resultado = get(top_Tracks, headers=headers)
    canciones = json.loads(resultado.content)["tracks"]
    listaCanciones = ""
    for num, cancion in enumerate(canciones):
        listaCanciones += f"{num+1} - {cancion['name']}\n"
    return listaCanciones

# Función para crear una lista de reproducción de un artista
def crearListaCanciones(token, nombre_artista):
    id_artista = buscar_artista(token, nombre_artista)
    listaReproduccion = []
    listaReproduccion.append(f"Lista de reproduccion de {nombre_artista}")
    listaReproduccion.append(
        f"Top 10 Mejores éxitos de {nombre_artista}\n\n{obtenerTopTracksPorId(token, id_artista)}"
    )  
    return listaReproduccion

# Función para crear una lista de reproducción de varios artistas
def crearListaReproduccion(token):
    listas_reproduccion = []
    encabezado = input("Dime cómo quieres que se llame la playlist\n")
    listas_reproduccion.insert(0, encabezado)
    salir = False
    while not salir:
        nombre_artista = input("Dime el nombre de tu artista\n")
        lista_reproduccion = obtenerTopTracksPorId(
            token, buscar_artista(token, nombre_artista)
        )
        listas_reproduccion.append(
            f"Top 10 Mejores éxitos de {nombre_artista}\n\n{lista_reproduccion}"
        )
        final = input(
            "¿Has terminado con tus artistas?" + "\n" + "1.Si\n" + "2.No\n"
        ).lower()
        if final == "si" or salir == "1":
            salir = True
        else:
            salir = False

    return listas_reproduccion

# Creamos la lista de reproducción
lista_reproduccion = crearListaReproduccion(token)

# Imprimimos la lista de reproducción
for lista in lista_reproduccion:
    print(lista)